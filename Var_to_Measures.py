import clipboard
import re


bas_template = '''
<variable name="ПередачВызСумВрем" class="java.lang.Long" calculation="Sum">
<variableExpression><![CDATA[$F{Время регистрации} != null && $F{Время получения команды на выезд}  != null ?
( $F{Время получения команды на выезд}.getTime() - $F{Время регистрации}.getTime() ) / 1000 : null]]></variableExpression>
</variable>
 '''

template = bas_template.replace("{", "{{").replace("}", "}}").replace("variable", "{0}")

template = re.sub(r'class=".+?"', 'class="{1}', template)

gotovo = template.format("measure", "lang.Object")

print(gotovo)

clipboard.copy(gotovo)


'''
<variable name="ПередачВызСумВрем" class="java.lang.Long" calculation="Sum">
<variableExpression><![CDATA[$F{Время регистрации} != null && $F{Время получения команды на выезд}  != null ?
( $F{Время получения команды на выезд}.getTime() - $F{Время регистрации}.getTime() ) / 1000 : null]]></variableExpression>
</variable>


<measure name="ПередачВызСумВрем" class="java.lang.Object" calculation="Sum">
<measureExpression><![CDATA[$F{Время регистрации} != null && $F{Время получения команды на выезд}  != null ?
( $F{Время получения команды на выезд}.getTime() - $F{Время регистрации}.getTime() ) / 1000 : null]]></measureExpression>
</measure>
'''