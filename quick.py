import urllib.request
from xml.dom import minidom

def ParseValute():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    webFile = urllib.request.urlopen(url)
    data = webFile.read()
    UrlSplit = url.split("/")[-1]
    ExtSplit = UrlSplit.split(".")[1]
    FileName = UrlSplit.replace(ExtSplit, "xml")
    with open(FileName, "wb") as localFile:
        localFile.write(data)
    webFile.close()

def Get_Date():
    doc = minidom.parse("XML_daily.xml")
    root = doc.getElementsByTagName("ValCurs")[0]
    return root.getAttribute('Date')

def PrintAllValutes():
    doc = minidom.parse("XML_daily.xml")
    Valute_Array=doc.getElementsByTagName("Valute")
    for each_Val in Valute_Array:
            value= each_Val.getElementsByTagName("Value")[0]
            name=each_Val.getElementsByTagName("CharCode")[0]
            print("1 ",name.firstChild.data," = ", end=value.firstChild.data)
            print('\n')

ParseValute()

print("Текущий курс валют на ",Get_Date())

PrintAllValutes()