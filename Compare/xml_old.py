var_old = '''
<?xml version="1.0" encoding="UTF-8"?>
<jasperPrint xmlns="http://jasperreports.sourceforge.net/jasperreports/print" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/print http://jasperreports.sourceforge.net/xsd/jasperprint.xsd" name="Шаблон" pageWidth="595" pageHeight="842" topMargin="15" leftMargin="15" bottomMargin="15" rightMargin="15" locale="ru_RU" timezone="Europe/Moscow">
	<property name="net.sf.jasperreports.export.xml.start.page.index" value="0"/>
	<property name="net.sf.jasperreports.export.xml.end.page.index" value="0"/>
	<property name="net.sf.jasperreports.export.xml.page.count" value="1"/>
	<property name="net.sf.jasperreports.export.xml.start.page.index" value="0"/>
	<property name="net.sf.jasperreports.export.xml.end.page.index" value="0"/>
	<property name="net.sf.jasperreports.export.xml.page.count" value="1"/>
	<origin group="Идентификатор" band="groupHeader"/>
	<origin group="Идентификатор" band="groupFooter"/>
	<origin band="background"/>
	<origin band="title"/>
	<origin band="detail"/>
	<origin band="summary"/>
	<style name="ДатаВремя" mode="Opaque" forecolor="#053250" hTextAlign="Left" vTextAlign="Middle" fontName="Verdana" fontSize="8">
		<paragraph leftIndent="3"/>
	</style>
	<style name="Ячейка_C_root" mode="Opaque" forecolor="#323232" backcolor="#FFFFFF" hTextAlign="Center" vTextAlign="Middle" fontName="Arial" fontSize="8" isBold="false">
		<box padding="1">
			<pen lineWidth="0.5" lineColor="#464646"/>
		</box>
	</style>
	<style name="Ячейка_C_b" style="Ячейка_C_root" isBold="true"/>
	<page>
		<text textHeight="9.722656">
			<reportElement uuid="53f700c4-3591-410d-b967-97018205acba" style="ДатаВремя" x="15" y="15" width="270" height="15" origin="3" srcId="2" printId="1"/>
			<textContent><![CDATA[С 01.01.2020 00:00:00 по 01.01.2020 01:00:00]]></textContent>
		</text>
		<text textHeight="9.722656" valueClass="java.util.Date" pattern="dd.MM.yy H:mm">
			<reportElement uuid="1ec3a2d6-4492-4b5d-bca4-daaa6d75e4d9" style="ДатаВремя" x="465" y="15" width="90" height="15" origin="3" srcId="3" printId="1"/>
			<paragraph leftIndent="5"/>
			<textContent><![CDATA[02.03.20 6:15]]></textContent>
		</text>
		<text textHeight="9.722656">
			<reportElement uuid="2e1747ce-eaf2-4cef-a25b-a4eaecc0fc96" style="ДатаВремя" x="355" y="15" width="90" height="15" origin="3" srcId="4" printId="1"/>
			<paragraph leftIndent="5"/>
			<textContent><![CDATA[НЕ ЗАДАНО]]></textContent>
		</text>
		<text textHeight="9.722656">
			<reportElement uuid="7d7b6fd9-3643-47b4-847f-0237622fb97e" style="ДатаВремя" x="445" y="15" width="20" height="15" origin="3" srcId="5" printId="1"/>
			<font isItalic="true"/>
			<textContent><![CDATA[до:]]></textContent>
		</text>
		<text textHeight="9.722656">
			<reportElement uuid="6e113643-f51f-4c23-a423-50a488de1bf3" style="ДатаВремя" x="300" y="15" width="55" height="15" origin="3" srcId="6" printId="1"/>
			<font isItalic="true"/>
			<textContent><![CDATA[Период с:]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="50" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="1"/>
			<textContent><![CDATA[ID > 927058]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="65" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="2"/>
			<textContent><![CDATA[ID > 927182]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="80" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="3"/>
			<textContent><![CDATA[ID > 927185]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="95" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="4"/>
			<textContent><![CDATA[ID > 927190]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="110" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="5"/>
			<textContent><![CDATA[ID > 927195]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="125" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="6"/>
			<textContent><![CDATA[ID > 927197]]></textContent>
		</text>
				<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="125" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="6"/>
			<textContent><![CDATA[ID > 927197]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="140" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="7"/>
			<textContent><![CDATA[ID > 927205]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="155" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="8"/>
			<textContent><![CDATA[ID > 927207]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="170" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="9"/>
			<textContent><![CDATA[ID > 927210]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="185" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="10"/>
			<textContent><![CDATA[ID > 927212]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="200" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="11"/>
			<textContent><![CDATA[ID > 927213]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="215" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="12"/>
			<textContent><![CDATA[ID > 927215]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="230" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="13"/>
			<textContent><![CDATA[ID > 927217]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="245" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="14"/>
			<textContent><![CDATA[ID > 927218]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="260" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="15"/>
			<textContent><![CDATA[ID > 927219]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="275" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="16"/>
			<textContent><![CDATA[ID > 927220]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="290" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="17"/>
			<textContent><![CDATA[ID > 927224]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="305" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="18"/>
			<textContent><![CDATA[ID > 927225]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="320" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="19"/>
			<textContent><![CDATA[ID > 927229]]></textContent>
		</text>
		<text textHeight="9.199219" lineSpacingFactor="1.1499023" leadingOffset="-1.5644531">
			<reportElement uuid="eada5b21-ad9b-42d9-a29f-579cc615aa48" style="Ячейка_C_root" x="15" y="335" width="70" height="15" backcolor="#F3FCF2" origin="4" srcId="7" printId="20"/>
			<textContent><![CDATA[ID > 927230]]></textContent>
		</text>
		<text textHeight="9.722656">
			<reportElement uuid="8ddae862-80c7-465b-91d6-163771d79fe9" style="ДатаВремя" x="15" y="355" width="45" height="20" backcolor="#F3FCF2" origin="5" srcId="8" printId="1"/>
			<font isItalic="true"/>
			<textContent><![CDATA[ID count:]]></textContent>
		</text>
		<text textHeight="9.722656" valueClass="java.lang.Long">
			<reportElement uuid="57386786-8d9c-4f51-a683-77b0edf83a52" style="ДатаВремя" x="205" y="355" width="50" height="20" backcolor="#F7E9E9" origin="5" srcId="9" printId="1"/>
			<font isBold="true"/>
			<textContent><![CDATA[20]]></textContent>
		</text>
		<text textHeight="9.722656">
			<reportElement uuid="d6f519af-5d36-4cb0-baec-83e0b0da1713" style="ДатаВремя" x="140" y="355" width="65" height="20" backcolor="#F7E9E9" origin="5" srcId="10" printId="1"/>
			<font isItalic="true"/>
			<textContent><![CDATA[ID dist. count:]]></textContent>
		</text>
		<text textHeight="9.722656" valueClass="java.lang.Long">
			<reportElement uuid="8abb19fd-ff0c-4b89-a08e-734973d0918c" style="ДатаВремя" x="60" y="355" width="50" height="20" backcolor="#F3FCF2" origin="5" srcId="11" printId="1"/>
			<font isBold="true"/>
			<textContent><![CDATA[20]]></textContent>
		</text>
	</page>
</jasperPrint>
'''