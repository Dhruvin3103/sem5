import xml.etree.ElementTree as et

tree = et.parse('book2.xml')

for i in tree.iter('book'):
    print(i.find('name').text)
    print(i.attrib['id'])




# # Agar Html code na likhna ho aur python me likhna ho to ye karo 
# import xml.etree.ElementTree as et


# import xml.etree.ElementTree as et
# import pandas as pd

# author = []
# title = []
# genre = []
# price = []
# publish_date = []
# description = []
# b_id = []

# tree = et.parse('books.xml')
# root = tree.getroot()

# # print(root.iter('book').find('title').text)

# for book in root.iter('book'):
#     b_id.append(book.attrib['id'])
#     title.append(book.find('title').text)
#     genre.append(book.find('genre').text)
#     price.append(book.find('price').text)
#     publish_date.append(book.find('publish_date').text)
#     description.append(book.find('description').text)

# print(description)
# data = pd.DataFrame({'id':b_id, 'title': title, 'genre': genre, 'price': price, 'publish_date': publish_date, 'description': description})
# print(data)