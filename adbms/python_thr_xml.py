import xml.etree.ElementTree as ET

# Your XML data
with open('books.xml', 'r') as file:
    xml_data = file.read()

# Parse XML
root = ET.fromstring(xml_data)

# Retrieve all book titles
titles = [book.find('title').text for book in root.findall('.//book')]
print(titles)
