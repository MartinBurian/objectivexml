__author__ = 'martinjr'


from __init__ import ObjectiveDoc

if __name__ == "__main__":
    # example data:
    data="""<atom:feed xml:base="https://kosapi.feld.cvut.cz/api/3" xml:lang="cs">
  <atom:id>https://kosapi.feld.cvut.cz/api/students/buriama8/parallels</atom:id>
  <atom:updated>2014-01-22T01:44:03.743</atom:updated>
  <atom:entry>
    <atom:id>urn:cvut:kos:parallel:349736000</atom:id>
    <atom:updated>2013-10-02T15:26:39.0</atom:updated>
    <atom:author>
      <atom:name>zichova</atom:name>
    </atom:author>
    <atom:link rel="self" href="parallels/349736000/"/>
    <atom:content atom:type="xml" xsi:type="parallel">
      <capacity>22</capacity>
      <capacityOverfill>DENIED</capacityOverfill>
      <code>105</code>
      <course xlink:href="courses/A4B33OPT/">Optimalizace</course>
      <enrollment>ALLOWED</enrollment>
      <occupied>21</occupied>
      <parallelType>TUTORIAL</parallelType>
      <semester xlink:href="semesters/B131/">Zimní 2013/2014</semester>
      <teacher xlink:href="teachers/shekhole/">Mgr. Oleksandr Shekhovtsov Ph.D.</teacher>
      <timetableSlot>
        <day>5</day>
        <duration>2</duration>
        <firstHour>5</firstHour>
        <parity>BOTH</parity>
        <room xlink:href="rooms/KN:E-132/">KN:E-132</room>
      </timetableSlot>
    </atom:content>
  </atom:entry>
  <atom:entry>
    <atom:id>urn:cvut:kos:parallel:349772000</atom:id>
    <atom:updated>2013-05-22T16:43:56.0</atom:updated>
    <atom:author>
      <atom:name>filandr</atom:name>
    </atom:author>
    <atom:link rel="self" href="parallels/349772000/"/>
    <atom:content atom:type="xml" xsi:type="parallel">
      <capacity>20</capacity>
      <capacityOverfill>DENIED</capacityOverfill>
      <code>102</code>
      <course xlink:href="courses/A4B34EM/">Elektronika a mikroelektronika</course>
      <enrollment>ALLOWED</enrollment>
      <occupied>9</occupied>
      <parallelType>TUTORIAL</parallelType>
      <semester xlink:href="semesters/B131/">Zimní 2013/2014</semester>
      <teacher xlink:href="teachers/janicev/">Ing. Vladimír Janíček Ph.D.</teacher>
      <teacher xlink:href="teachers/jakovenk/">doc.Ing. Jiří Jakovenko Ph.D.</teacher>
      <timetableSlot>
        <day>1</day>
        <duration>2</duration>
        <firstHour>5</firstHour>
        <parity>BOTH</parity>
        <room xlink:href="rooms/T2:C3-s143/">T2:C3-s143</room>
      </timetableSlot>
      <timetableSlot>
        <day>1</day>
        <duration>2</duration>
        <firstHour>5</firstHour>
        <parity>BOTH</parity>
        <room xlink:href="rooms/T2:B2-s141j/">T2:B2-s141j</room>
      </timetableSlot>
    </atom:content>
  </atom:entry>
  <atom:entry>
    <atom:id>urn:cvut:kos:parallel:349775000</atom:id>
    <atom:updated>2013-05-22T16:43:56.0</atom:updated>
    <atom:author>
      <atom:name>filandr</atom:name>
    </atom:author>
    <atom:link rel="self" href="parallels/349775000/"/>
    <atom:content atom:type="xml" xsi:type="parallel">
      <capacity>35</capacity>
      <capacityOverfill>DENIED</capacityOverfill>
      <code>1</code>
      <course xlink:href="courses/A4B34EM/">Elektronika a mikroelektronika</course>
      <enrollment>DENIED</enrollment>
      <occupied>9</occupied>
      <parallelType>LECTURE</parallelType>
      <semester xlink:href="semesters/B131/">Zimní 2013/2014</semester>
      <teacher xlink:href="teachers/jakovenk/">doc.Ing. Jiří Jakovenko Ph.D.</teacher>
      <timetableSlot>
        <day>2</day>
        <duration>2</duration>
        <firstHour>9</firstHour>
        <parity>BOTH</parity>
        <room xlink:href="rooms/T2:B2-s141k/">T2:B2-s141k</room>
      </timetableSlot>
    </atom:content>
  </atom:entry>
  <osearch:startIndex>0</osearch:startIndex>
  <osearch:totalResults>9</osearch:totalResults>
</atom:feed>
""".encode('utf-8')

    doc=ObjectiveDoc(data) # parse document
    doc._root.traverse() # print out the structure

    entries=doc.get("atom:feed").get("atom:entry") # get entries

    for entry in entries:
        content=entry.get("atom:content")

        for teacher in entry.get("atom:content").teacher: # iterate over all teachers
            print(teacher("xlink:href"))

        print("parallel code: %s"%entry.get("atom:content").code()) # print the code (unique tag, needn't be iterated)

        print("parallel resource: %s"%(entry.get("atom:link", rel="self")("href"))) # filter out atom:links with rel="self" (assume only one per entry)

