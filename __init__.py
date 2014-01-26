__author__="martinjr"

import xml.sax
import re

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
    _rebool=re.compile("^true$|^false$", re.I)
    _redigit=re.compile("^\d+$")

    def __init__(self, name, attrs):
        self._content=""
        self._content_parsed=None
        self._name=name
        self._attrs={key: attrs.getValue(key) for key in attrs.getNames()} if attrs else {}
        self._attrs_parsed={key: self._parse_value(attrs.getValue(key)) for key in attrs.getNames()} if attrs else {}

        self._children={}

    def __getattr__(self, item):
        if item in self._children:
            return self._children[item]
        else:
            print("REQUESTING NON-EXISTENT FIELD")
            return False

    def __call__(self, attr="", raw=False):
        if not attr:
            if self._content_parsed==None:
                self._content_parsed=self._parse_value(self._content)
            return self._content if raw else self._content_parsed

        elif attr in self._attrs:
            return self._attrs[attr] if raw else self._attrs_parsed[attr]

        else:
            print("UNKNOWN ATTRIBUTE "+attr)
            return False

    def __iter__(self):
        yield self

    def get(self, item, filterdict={}, **kwargs):
        if (filterdict or kwargs) and item in self._children:
            ret=[]
            filter=dict(filterdict, **kwargs)
            print(filter)
            for el in self._children[item]:
                ok=True
                for attr, value in filter.items():
                    if el(attr)!=value:
                        ok=False
                        break
                if ok:
                    ret.append(el)

            if ret:
                return ret if len(ret)>1 else ret[0]
            else:
                return False

        else:
            return self.__getattr__(item)

    def _parse_value(self, val):
        if self._redigit.match(val):
            return int(val)
        elif self._rebool.match(val):
            return (val=="true" or val=="True")
        else:
            return val

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
            print("%s%s: %s (%s)"%("  "*d, self._name, self._content, str(self._attrs)))

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
