__author__ = 'martinjr'

from __init__ import ObjectiveDoc

if __name__ == "__main__":
    # example data:
    data="""
    <namespace:root>
        <entry division="sales">
            <id>1</id>
            <name n:attr="value">Martin</name>
            <cars>
                <car id="1A1 1111" used="true">Hyundai i30</car>
                <car id="1A1 1112" used="false">Hyundai ix55</car>
            </cars>
            <occupation>Manager</occupation>
            <occupation>Developer</occupation>
            <paid>true</paid>
            <age>32</age>
            <secure:password>1234</secure:password>
        </entry>
        <entry division="sales">
            <id>2</id>
            <name>Standa</name>
            <cars>
                <car id="1A1 1111" used="true">Skoda Yetti</car>
            </cars>
            <occupation>Manager</occupation>
            <paid>TRUE</paid>
            <age>25</age>
            <secure:password>0000</secure:password>
        </entry>
        <entry division="IT">
            <id>3</id>
            <name>Alice</name>
            <occupation>Developer</occupation>
            <paid>true</paid>
            <age>22</age>
            <secure:password>40T1_V7%Ee</secure:password>
        </entry>
        <entry division="IT">
            <id>5</id>
            <name>Bob</name>
            <cars>
                <car id="1A1 2718" used="true">DeLorean</car>
            </cars>
            <paid>false</paid>
            <age>17</age>
            <secure:password>hatem$</secure:password>
        </entry>
    </namespace:root>
"""

    doc=ObjectiveDoc(data) # parse document
    doc._root.traverse() # print out the structure

    for entry in doc.get("namespace:root").entry: # iterate over all entries
        print("RESULTS FOR %s (id %d)"%(entry.name(), entry.id())) # basic referencing

        if entry.occupation: # check if there is at leas one occupation
            for occ in entry.occupation: # for each occupation
                print("works in %s as %s"%(entry("division"), # entry division param
                                              occ())) # the occupation

        if entry.cars: # check if there are some cars
            for car in entry.cars.car:
                if car("used"): # bool parsing
                    print("uses a %s car (id %s)"%(car(), car("id")))

        if entry.paid():
            print("a paid person uses password '%s'"%(entry.get("secure:password")(raw=True))) # use node.get("sub") when sub uses special characters
        else:
            print("an unpaid person uses password %s"%(entry.get("secure:password")(raw=True))) # use raw=True to prevent '0000' becoming 0

        if entry.age()>23: # int conversion
            print("%s is getting a bit old"%entry.name())

        print()

    for entry in doc.get("namespace:root").get("entry", division="IT"): # filter out entries with division="IT" attribute
        print("IT worker: %s"%entry.name())                             # (again, check when presence is not sure and
                                                                        # iterate when multiple are possible)


