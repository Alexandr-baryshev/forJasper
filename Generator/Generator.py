import re
import uuid
import clipboard
import xml.etree.ElementTree as Etree

tree = Etree.parse('GenJasperTemplate.jrxml')
root = tree.getroot()
print(root)

for child in root:
    print(child.tag)
    if '{http://jasperreports.sourceforge.net/jasperreports}summary' == child.tag:
        # print(child.attrib)
        # child.set('example', 'vl')
        # print(child.attrib)
        b = child.find('{http://jasperreports.sourceforge.net/jasperreports}band')

        # < textField >
        tf = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}textField")
        b.insert(1, tf)

        # < reportElement
        # x = "90"
        # y = "50"
        # width = "100"
        # height = "30"
        # uuid = "923859d3-ad08-4ba1-b4cc-816c28228d14" / >
        re = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}reportElement")
        re.set("x", "90")
        re.set("y", "50")
        re.set("width", "100")
        re.set("height", "30")
        re.set("uuid", str(uuid.uuid4()))
        tf.insert(1, re)

        # < textFieldExpression > <![CDATA["Text Field"]] > < / textFieldExpression >
        tfe = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression")
        tfe.text = '"ddd"'
        tf.insert(1, tfe)



tree.write('GenJasper.jrxml')


