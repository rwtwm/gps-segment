# This is a sample Python script.
import xml.parsers.expat as xpt
from lxml import etree
from lxml import objectify


def parse_xml():
    my_tcx = open('tcx.tcx', 'r')
    tcx_txt = (my_tcx.read())
    print(tcx_txt)

#Gets the tcx file and creates a parsed representation
def parse_xml2():
    my_tcx = open('tcx.tcx', 'r')
    tree = etree.parse(my_tcx)

    #print(etree.tostring(tree,pretty_print=True) )
    #print(tree.docinfo.xml_version)
    #print(tree.docinfo.doctype)
    root = tree.getroot()
    for child in root[0][0][1]:
        print(child.tag)
        print(child.text)
    #print(etree.tostring(root[0][0][1][5]))
    #print(root[0][0][2][1].text)

#Next step - find a lap and iterate through it



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_xml2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
