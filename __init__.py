__author__="martinjr"

import xml.sax

class ObjectiveDoc:
    def __init__(self, doc="", filename="", encoding='utf-8'):
        print("TEST")
        self._root=Element("root", ())
        if doc:
            self._parse_doc(doc, encoding)
        else:
            self._parse_file(filename, encoding)

    def __getattr__(self, item):
        return self._root.__getattr__(item)

    def __call__(self, *args, **kwargs):
        return self._root.__call__(*args, **kwargs)

    def get(self, item):
        return self.__getattr__(item)

    def _parse_doc(self, doc, encoding):
        xml.sax.parseString(bytes(doc, encoding), SaxHandler(self._root))

    def _parse_file(self, filename, encoding):
        with open(filename, 'r', encoding=encoding) as infile:
            xml.sax.parse(infile, SaxHandler(self._root))

class Element:
    def __init__(self, name, attrs):
        self._content=""
        self._name=name
        self._attrs=attrs

        self._children={}

    def __getattr__(self, item):
        if item in self._children:
            return self._children[item]
        else:
            print("REQUESTING NON-EXISTENT FIELD")
            return False

    def __call__(self, attr=""):
        if not attr:
            return self._content
        elif attr in self._attrs:
            return self._attrs.getValue(attr)
        else:
            print("UNKNOWN ATTRIBUTE "+attr)
            return False

    def __iter__(self):
        yield self

    def get(self, item, **kwargs):
        if kwargs and item in self._children:
            for el in self._children[item]:
                for attr, value in kwargs.items():
                    if el(attr)==value:
                        return el

        else:
            return self.__getattr__(item)

    def add_element(self, element):
        if element._name in self._children:
            if isinstance(self._children[element._name], list):
                self._children[element._name].append(element)
            else:
                self._children[element._name]=[self._children[element._name], element]
        else:
            self._children[element._name]=element

    def traverse(self, d=0):
        if self._children:
            print("  "*d+self._name)
            for name, child in self._children.items():
                for sub in child:
                    sub.traverse(d+1)
        else:
            print("%s%s: %s (%s)"%("  "*d, self._name, self._content, str(self._attrs.getNames())))

class SaxHandler(xml.sax.ContentHandler):
    def __init__(self, root):
        self.path=[root]

    def startElement(self, name, attrs):
        element=Element(name, attrs)
        self.path[-1].add_element(element)
        self.path.append(element)

    def endElement(self, name):
        self.path.pop()

    def characters(self, content):
        self.path[-1]._content+=content.strip()
