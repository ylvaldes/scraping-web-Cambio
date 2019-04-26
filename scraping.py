from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
 
try:
    html = urlopen("https://www.brou.com.uy/")
except HTTPError as e:
    print(e)
except URLError:
    print("Servidor caido o dominio incorrecto")
else:
    res = BeautifulSoup(html.read(),features="lxml")
    tags= res.find("div", {"class": "cuerpo"}).select("")
    if res.title is None:
        print("No se encuentra la etiqueta")
    else:
        print(res.title)
        for tag in tags:
            print(tag.getText())