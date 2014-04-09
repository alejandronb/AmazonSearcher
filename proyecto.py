#coding: utf-8
import requests
import webbrowser
from lxml import etree
import bottle

ID_afiliado = "htttwicomale-21"

clave_acceso = ""

clave_secreta = ""

libro = raw_input("Introduce el libro a buscar: ")

@bottle.route('/')
def home_page():
	return "Hola Mundo"
	
bottle.debug(True)
bottle.run(host='localhost')


peticion = requests.get("""Service=AWSECommerceService
Version=2011-08-01
AssociateTag=htttwicomale-21
Operation=ItemSearch
SearchIndex=Books
Keywords=harry+potter
Timestamp=2014-04-09T18:20:56.000Z
AWSAccessKeyId=AKIAIJKV4RAQKPLTDABQ""")

print peticion.text
