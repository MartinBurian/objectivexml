__author__="martinjr"

import xml.sax

class ObjectiveDoc:
    def __init__(self, doc):
        self._root=Element("root", ())
        self._parse_doc(doc)

    def __getattr__(self, item):
        return self._root.__getattr__(item)

    def __call__(self, *args, **kwargs):
        return self._root.__call__(*args, **kwargs)

    def get(self, item):
        return self.__getattr__(item)

    def _parse_doc(self, doc):
        xml.sax.parseString(doc, SaxHandler(self._root))

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

    def __call__(self, attr=""):
        if not attr:
            return self._content
        elif attr in self._attrs:
            return self._attrs.getValue(attr)
        else:
            print("UNKNOWN ATTRIBUTE "+attr)

    def __iter__(self):
        yield self

    def get(self, item):
        return self.__getattr__(item)

    def set_content(self, content):
        self._content=content

    def add_element(self, element):
        if element._name in self._children:
            if isinstance(self._children[element._name], list):
                self._children[element._name].append(element)
            else:
                self._children[element._name]=[self._children[element._name], element]
        else:
            self._children[element._name]=element

    def traverse(self):
        if self._children:
            for name, child in self._children.items():
                print(name)

                if isinstance(child, list):
                    for sub in child:
                        sub.traverse()
                else:
                    child.traverse()
        else:
            print("%s: %s (%s)"%(self._name, self._content, str(self._attrs.getNames())))

class SaxHandler(xml.sax.ContentHandler):
    def __init__(self, root):
        self.root=root
        self.buffer=""
        self.path=[root]

    def startDocument(self):
        pass

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        element=Element(name, attrs)
        self.path[-1].add_element(element)
        self.path.append(element)

    def endElement(self, name):
        self.path.pop().set_content(self.buffer)
        self.buffer=""

    def characters(self, content):
        self.buffer+=content.strip()



if __name__ == "__main__":
    doc=ObjectiveDoc("""<?xml version="1.0" encoding="UTF-8"?><atom:feed xmlns="http://kosapi.feld.cvut.cz/schema/3" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:osearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xml:base="https://kosapi.feld.cvut.cz/api/3" xml:lang="cs"><atom:id>https://kosapi.feld.cvut.cz/api/students/buriama8/parallels</atom:id><atom:updated>2014-01-21T22:40:43.421</atom:updated><atom:entry><atom:id>urn:cvut:kos:parallel:349736000</atom:id><atom:updated>2013-10-02T15:26:39.0</atom:updated><atom:author><atom:name>zichova</atom:name></atom:author><atom:link rel="self" href="parallels/349736000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>22</capacity><capacityOverfill>DENIED</capacityOverfill><code>105</code><course xlink:href="courses/A4B33OPT/">Optimalizace</course><enrollment>ALLOWED</enrollment><occupied>21</occupied><parallelType>TUTORIAL</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/shekhole/">Mgr. Oleksandr Shekhovtsov Ph.D.</teacher><timetableSlot><day>5</day><duration>2</duration><firstHour>5</firstHour><parity>BOTH</parity><room xlink:href="rooms/KN:E-132/">KN:E-132</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:349742000</atom:id><atom:updated>2013-09-19T10:44:40.0</atom:updated><atom:author><atom:name>zichova</atom:name></atom:author><atom:link rel="self" href="parallels/349742000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>140</capacity><capacityOverfill>DENIED</capacityOverfill><code>1</code><course xlink:href="courses/A4B33OPT/">Optimalizace</course><enrollment>DENIED</enrollment><occupied>110</occupied><parallelType>LECTURE</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/wernetom/">Ing. Tomáš Werner Ph.D.</teacher><teacher xlink:href="teachers/xfrancv/">Ing. Vojtěch Franc Ph.D.</teacher><timetableSlot><day>5</day><duration>2</duration><firstHour>3</firstHour><parity>BOTH</parity><room xlink:href="rooms/KN:E-107/">KN:E-107</room></timetableSlot><timetableSlot><day>2</day><duration>2</duration><firstHour>7</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:C3-340/">T2:C3-340</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:355122</atom:id><atom:updated>2013-09-18T14:24:14.0</atom:updated><atom:author><atom:name>brozomar</atom:name></atom:author><atom:link rel="self" href="parallels/355122/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>15</capacity><capacityOverfill>DENIED</capacityOverfill><code>101</code><course xlink:href="courses/A0B04KS2/">Španělská konverzace 2</course><enrollment>ALLOWED</enrollment><occupied>3</occupied><parallelType>TUTORIAL</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/6639906/">Bc. Petra Frimlová</teacher><timetableSlot><day>1</day><duration>2</duration><firstHour>11</firstHour><parity>BOTH</parity><room xlink:href="rooms/Z2:B1-344/">Z2:B1-344</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:346953000</atom:id><atom:updated>2013-09-11T11:18:29.0</atom:updated><atom:author><atom:name>zichova</atom:name></atom:author><atom:link rel="self" href="parallels/346953000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>25</capacity><capacityOverfill>DENIED</capacityOverfill><code>101</code><course xlink:href="courses/AE4B33RPZ/">Pattern Recognition and Machine Learning</course><enrollment>ALLOWED</enrollment><occupied>19</occupied><parallelType>TUTORIAL</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/prittja1/">Ing. James Brandon Pritts</teacher><teacher xlink:href="teachers/aldanjav/">Ing. Javier Alejandro Aldana Iuit</teacher><timetableSlot><day>4</day><duration>2</duration><firstHour>7</firstHour><parity>BOTH</parity><room xlink:href="rooms/KN:E-132/">KN:E-132</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:346955000</atom:id><atom:updated>2013-09-11T14:54:42.0</atom:updated><atom:author><atom:name>zichova</atom:name></atom:author><atom:link rel="self" href="parallels/346955000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>30</capacity><capacityOverfill>DENIED</capacityOverfill><code>1</code><course xlink:href="courses/AE4B33RPZ/">Pattern Recognition and Machine Learning</course><enrollment>DENIED</enrollment><occupied>19</occupied><parallelType>LECTURE</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/matas/">prof.Ing. Jiří Matas Ph.D.</teacher><teacher xlink:href="teachers/xfrancv/">Ing. Vojtěch Franc Ph.D.</teacher><teacher xlink:href="teachers/flachbor/">Boris Flach Dr. rer. nat. habil.</teacher><timetableSlot><day>1</day><duration>2</duration><firstHour>9</firstHour><parity>BOTH</parity><room xlink:href="rooms/KN:G-205/">KN:G-205</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:349039000</atom:id><atom:updated>2013-05-22T13:45:35.0</atom:updated><atom:author><atom:name>filandr</atom:name></atom:author><atom:link rel="self" href="parallels/349039000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>10</capacity><capacityOverfill>DENIED</capacityOverfill><code>3</code><course xlink:href="courses/A2B34MIK/">Mikrokontroléry</course><enrollment>ALLOWED</enrollment><occupied>10</occupied><parallelType>TUTORIAL</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/teplyt1/">Ing. Tomáš Teplý</teacher><timetableSlot><day>3</day><duration>2</duration><firstHour>5</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:B2-s141j/">T2:B2-s141j</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:349047000</atom:id><atom:updated>2013-05-22T13:45:35.0</atom:updated><atom:author><atom:name>filandr</atom:name></atom:author><atom:link rel="self" href="parallels/349047000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>100</capacity><capacityOverfill>DENIED</capacityOverfill><code>1</code><course xlink:href="courses/A2B34MIK/">Mikrokontroléry</course><enrollment>DENIED</enrollment><occupied>56</occupied><parallelType>LECTURE</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/teplyt1/">Ing. Tomáš Teplý</teacher><timetableSlot><day>4</day><duration>2</duration><firstHour>7</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:C3-52/">T2:C3-52</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:349772000</atom:id><atom:updated>2013-05-22T16:43:56.0</atom:updated><atom:author><atom:name>filandr</atom:name></atom:author><atom:link rel="self" href="parallels/349772000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>20</capacity><capacityOverfill>DENIED</capacityOverfill><code>102</code><course xlink:href="courses/A4B34EM/">Elektronika a mikroelektronika</course><enrollment>ALLOWED</enrollment><occupied>9</occupied><parallelType>TUTORIAL</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/janicev/">Ing. Vladimír Janíček Ph.D.</teacher><teacher xlink:href="teachers/jakovenk/">doc.Ing. Jiří Jakovenko Ph.D.</teacher><timetableSlot><day>1</day><duration>2</duration><firstHour>5</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:C3-s143/">T2:C3-s143</room></timetableSlot><timetableSlot><day>1</day><duration>2</duration><firstHour>5</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:B2-s141j/">T2:B2-s141j</room></timetableSlot></atom:content></atom:entry><atom:entry><atom:id>urn:cvut:kos:parallel:349775000</atom:id><atom:updated>2013-05-22T16:43:56.0</atom:updated><atom:author><atom:name>filandr</atom:name></atom:author><atom:link rel="self" href="parallels/349775000/"/><atom:content atom:type="xml" xsi:type="parallel"><capacity>35</capacity><capacityOverfill>DENIED</capacityOverfill><code>1</code><course xlink:href="courses/A4B34EM/">Elektronika a mikroelektronika</course><enrollment>DENIED</enrollment><occupied>9</occupied><parallelType>LECTURE</parallelType><semester xlink:href="semesters/B131/">Zimní 2013/2014</semester><teacher xlink:href="teachers/jakovenk/">doc.Ing. Jiří Jakovenko Ph.D.</teacher><timetableSlot><day>2</day><duration>2</duration><firstHour>9</firstHour><parity>BOTH</parity><room xlink:href="rooms/T2:B2-s141k/">T2:B2-s141k</room></timetableSlot></atom:content></atom:entry><osearch:startIndex>0</osearch:startIndex><osearch:totalResults>9</osearch:totalResults></atom:feed>""".encode('utf-8'))

    entries=doc.get("atom:feed").get("atom:entry")

    for entry in entries:
        print("entry")
        for teacher in entry.get("atom:content").teacher:
            print(teacher("xlink:href"))
