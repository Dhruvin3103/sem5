import re 
file = open('sampletext.txt')
text = file.read()
email_pat = r'[a-zA-Z0-9\.\+_]+@[a-zA-Z0-9\.\+]+.com'
mob_pat = r'[0-9]+[#\-*]*[0-9]+[0-9]+[#\-*]*[0-9]'
url_pat = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
name_pat = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+'

print(f"Emails in text fiel are : {re.findall(email_pat,text)}\nPhone numbers are : {re.findall(mob_pat,text)}\nNames are : {re.findall(name_pat,text)}")
