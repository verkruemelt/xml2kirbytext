from xml.dom import minidom

file = "example.xml"
xmldoc = minidom.parse('example.xml')
itemlist = xmldoc.getElementsByTagName('field')

#print(len(itemlist))
#print(itemlist[0].attributes['name'].value)

f = open(file+".txt","w")
print("Title: " + file)
f.write("Title: " + file + "\n")
print("----")
f.write("----" + "\n")
for s in itemlist:
    print(s.attributes['name'].value + ": " + s.attributes['value'].value)
    f.write(s.attributes['name'].value + ": " + s.attributes['value'].value + "\n")
    print("----")
    f.write("----" + "\n")

f.close()
