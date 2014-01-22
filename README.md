objectivexml
============

objectivexml is a lightweight XML reading library for python 3+. It's designed to be as easy to use as imaginable. It is meant for parsing simple xml documents with well-known structure. Complex (=huge) documents can suffer from performance issues. Parsing 21MB file with 3 level structure took about 1-2s on an ordinary computer.

    document=ObjectiveDoc("string"[, encoding='utf-8'])
    document=ObjectiveDoc(filename="filename"[, encoding='utf-8'])

Parse a string or open a file (default encoding is unicode, specify your own if you need to)

    node=document.path.to.node
    node=document.path.get("to-but:invalid").node

node is either a list of nodes with the same name, or it's a single node usable on it's own. It's always iterable:

    for node in document.path.nodes:
        do_stuff(node)

getting node content (str):

    node()

getting node attribute (str):

    node("attribute")

Please note that objectivexml is not really fit for manipulating huge XML files. Use SAX to process them on the fly instead of storing them in the memory as objects.
