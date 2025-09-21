import xmltodict

xml_str = """
<xml>
    <Name>kenny</Name>
    <age>30</age>
</xml>
"""

xml_dict = xmltodict.parse(xml_str)
print(xml_dict)

xml_dict = {"xml": {"name": "kenny", "age": 32}}

xml_str = xmltodict.unparse(xml_dict, pretty=True)

print(xml_str)
