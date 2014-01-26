objectivexml
============

objectivexml is a lightweight XML reading library for python 3+. It's designed to be as easy to use as imaginable. It is meant for parsing simple xml documents with well-known structure.

Parse a string or open a file (default encoding is utf-8, specify your own if you need to):

    document=ObjectiveDoc("string"[, encoding='utf-8'])
    document=ObjectiveDoc(filename="filename"[, encoding='utf-8'])

Navigating the document tree
----------------------------

Navigate the document tree by referencing object properties. If the desired node name is not a valid identifier, use the get() method instead.

    node=document.path.to.node
    node=document.path.get("to-but:invalid").node

The get() method supports, in addition to complex node names, filtering using attributes. If the attributes are not valid identifiers, supply them in a dictionary as the filterdict kwarg (you can still use the valid ones as usual). More filters are joined using and.

    node=document.path.get("node", attribute="value")
    node=document.path.get("node", filterdict={"invalid:attr-name": "value"}, attr="value2")

A node is either a list of nodes with the same name, or it's a single node usable on it's own. However, it's always iterable:

    for node in document.path.nodes:
        do_stuff(node)

When attempting to get a node that is not present in the document, False is returned. If you are not sure if at leas one node will be there, check.

The general rule to access a node: If there is a possibility that a node won't be there, check first. If you are sure there'll be only one, use it directly. When there's the slightest possibility that there will be more than one matching node, iterate. It'll work. See example.py for best practices.

Node contents
-------------

Getting single node content (iterate over lists):

    node()

Getting single node attribute:

    node("attribute")

The values are parsed to basic python types: int, bool nad str. Numerals are parsed to int, true|false (case-insensitive) to bool and the rest is left as a string. The original values can be accessed using kwarg raw=True:

    node(raw=True) # '01234'
    node() # 1234

Notes
-----
Please note that objectivexml is not really fit for manipulating huge XML files. Use SAX to process them on the fly instead of storing them in the memory as objects.
