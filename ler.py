import xml.etree.ElementTree as ET


tree = ET.parse("lista1b.jff")
automaton = tree.getroot()
#le o estado, mas falta uma forma de procurar a tag 'initial' e 'final'
for elem in automaton[1].iter('state'):
    for subchild in elem.iter('initial'):
        print(" ",elem.attrib)#pegar o id
    for subchild in elem.iter('final'):
        print(" ",elem.attrib)#pegar o id
    #for subchild in elem.iter('y'):
        #print("y ",subchild.text)
    print(elem.tag, elem.attrib)

#le transicoes: (from, to, read)
for elem in automaton[1].iter('transition'):
    print(elem[0].text,elem[1].text,elem[2].text)