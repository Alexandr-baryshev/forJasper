import uuid
import xml.etree.ElementTree as Etree

tree = Etree.parse('GenJasperTemplate.jrxml')
root = tree.getroot()
print(root)

for child in root:
    print(child.tag)
    if '{http://jasperreports.sourceforge.net/jasperreports}summary' == child.tag:

        b = child.find('{http://jasperreports.sourceforge.net/jasperreports}band')

        tf = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}textField")
        b.insert(1, tf)

        re = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}reportElement")
        re.set("x", "90")
        re.set("y", "50")
        re.set("width", "100")
        re.set("height", "30")
        re.set("uuid", str(uuid.uuid4()))
        tf.insert(1, re)

        tfe = Etree.Element("{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression")
        tfe.text = '"ddd"'
        tf.insert(1, tfe)


tree.write('GenJasper.jrxml')