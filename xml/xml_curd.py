import xml.etree.ElementTree as ET

tree = ET.parse('students.xml')
root = tree.getroot()

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('students_new.xml')

# Python 有三种方法解析 XML:
# SAX，DOM，以及 ElementTree.
