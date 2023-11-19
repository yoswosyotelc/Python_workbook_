https://python.hotexamples.com/examples/pyautocad/Autocad/-/python-autocad-class-examples.html
https://pyautocad.readthedocs.io/en/latest/
https://github.com/reclosedev/pyautocad/blob/master/docs/example.py

from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print acad.doc.Name

p1 = APoint(0, 0)
p2 = APoint(50, 25)
for i in range(5):
    text = acad.model.AddText(u'Hi %s!' % i, p1, 2.5)
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1, 10)
    p1.y += 10

for obj in acad.iter_objects():
    print obj.ObjectName

for text in acad.iter_objects('Text'):
    print text.TextString, text.InsertionPoint

for obj in acad.iter_objects(['Text', 'Line']):
    print obj.ObjectName

def text_contains_3(text_obj):
    return '3' in text_obj.TextString

text = acad.find_one('Text', predicate=text_contains_3)
print text.TextString

from pyautocad import ACAD

for text in acad.iter_objects('Text'):
    old_insertion_point = APoint(text.InsertionPoint)
    text.Alignment = ACAD.acAlignmentRight
    text.TextAlignmentPoint = old_insertion_point

for line in acad.iter_objects('Line'):
    p1 = APoint(line.StartPoint)
    line.EndPoint = p1 - APoint(20, 0)













import pyautocad
acad = pyautocad.Autocad()
#
#

# collect many codes.. that do iwth python...
to create a drawing...



from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
#print(acad.doc.Name) #for test
#
acad2 = acad.doc.Open() #I want to open saved dwg or dxf file of my computer
#print(acad2.doc.Name)

#from pyautocad.contrib.tables import Table
#
#acad = Autocad()
#
Draw a line
x1 = 0
y1 = 120
x2 = 10
y2 = 10
p1 = APoint(x1,y1)
p2 = APoint(x2,y2)

acad.model.AddLine(p1,p2)



#p1 = APoint(0, 0)
#for i in range(5):
#    obj = acad.model.AddText(u'Hi %s!' % i, p1, 2.5)
#    p1.y += 10
#
#table = Table()
#for obj in acad.iter_objects('Text'):
#    x, y, z = obj.InsertionPoint
#    table.writerow([obj.TextString, x, y, z])
#table.save('data.xls', 'xls')
#
#data = Table.data_from_file('data.xls')
