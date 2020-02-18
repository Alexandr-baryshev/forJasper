import re

xml_string = '''
            < field
name = "Регистрационный номер"


class ="java.lang.Number" >

< fieldDescription > <![CDATA[]] > < / fieldDescription >
< / field >
< field
name = "Время регистрации"


class ="java.util.Date" >

< fieldDescription > <![CDATA[]] > < / fieldDescription >
< / field >
< field
name = "Расшифровка (ОД)"


class ="java.lang.String" >

< fieldDescription > <![CDATA[]] > < / fieldDescription >
< / field >
< field
name = "Наименование"


class ="java.lang.String" >

< fieldDescription > <![CDATA[]] > < / fieldDescription >
< / field >
'''

scanText = r'name = ".+?"'
result = re.findall(scanText, xml_string)

for i in result:
    print(i)