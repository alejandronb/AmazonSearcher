#coding: utf-8
import requests
import webbrowser
import bottle
from lxml import etree
import bottlenose

assoc_tag = "htttwicomale-21"

#Las claves están en otro fichero
AWS = "AKIAJIUVGW6DQQEB42PA" 
secret_key = "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"

amazon = bottlenose.Amazon(AWS,secret_key,assoc_tag)

@bottle.get('/') # o @bottle.route
def home_page():
	return bottle.template('index.tpl')

# @bottle.route('/style/<filename>')
# def server_static(filename):
#   return bottle.static_file(filename, root='./style')

@bottle.post('/busqueda')
def busqueda():
	articulo = bottle.request.forms.get("articulo")
	respuesta = amazon.ItemSearch(Keywords=articulo, SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")
	raiz = etree.fromstring(respuesta)
	ns = "http://webservices.amazon.com/AWSECommerceService/2011-08-01"
	#listaresultados = raiz[1]
	#NumResultados = raiz.xpath("//ns:ItemSearchResponse/ns:ItemSearch/ns:TotalResults/text()", namespaces={"ns":ns})
	NumResultados = raiz.xpath("//ns:TotalResults/text()", namespaces={"ns":ns})
	#NumResultados = listaresultados.find(ns+"TotalResults").text #Pongo el .text al final para que obtenga directamente el valor de la etiqueta
	Items = raiz.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
	# Item = listaresultados.find(ns+"Item")
	#cantidad = len(Items) #Esta es la cantidad que tenemos que utilizar para enviar por ejemplo 10 detalles del producto al template
	lista = []
	for Item in Items:
		diccionario = {}
		for i in Item:
			if i.tag == "{%s}ItemAttributes" % ns:
				for j in i:
					if j.tag == "{%s}Title" % ns:
						diccionario["Titulo"] = j.text
			elif i.tag == "{%s}DetailPageURL" %ns:
				diccionario["URLDetalles"] = i.text
			elif i.tag == "{%s}ASIN" % ns:
				ASIN = i.tag
		lista.append(diccionario)


# Búsqueda imágenes para un Item:
#response = amazon.ItemLookup(ItemId="1449372422", ResponseGroup="Images")
# Sintaxis para añadir datos a un diccionario y luego añadir éste a un diccionario:
	# for Item in Items:
	# 	for i in Item:
	# 		diccionario = {}
	# 		if i.tag == "{%s}DetailPageURL" % ns:
	# 			#print i.text
	#  			diccionario["URLDetallesProducto"] = i.text
	#  		elif i.tag == "{%s}ItemAttributes" % ns:
	#  			diccionario["url"] = 
	# 		lista.append(diccionario)
	return bottle.template('resultado.tpl', {'lista':lista})
#	URLDetallesProducto = raiz.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:DetailPageURL/text()",namespaces={"ns":ns})
#	for i in URLDetallesProducto:
#		Resultado1 = URLDetallesProducto[i]
	# URLDetallesProducto = Item.find(ns+"DetailPageURL").text
	# ItemLinks = Item.find(ns+"ItemLinks")
	# ItemLink = ItemLinks.find(ns+"ItemLink")
	# Atributos = Item.find(ns+"ItemAttributes")
	# Fabricante = Atributos.find(ns+"Manufacturer").text
	# TituloProducto = Atributos.find(ns+"Title").text
	# return bottle.template('resultado.tpl', {'articulo':articulo,'NumResultados':NumResultados,'URLDetallesProducto':URLDetallesProducto})
	#listaresultados = raiz.find(ns+"Items") Sustituir el de arriba por este

#Mirar lo de la etiqueta MoreSearchResults
	#MasResultados = listaresultados.find(ns+"MoreSearchResults").text
 
 # respuesta = amazon.ItemSearch(Keywords="Kindle", SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")
 # arbol = etree.fromstring(respuesta)
 # raiz = arbol.find("ItemSearchResponse")
 # listaitems = raiz.find("Items")
 # NumResultados = listaitems.find("TotalResults")





# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
                                      'runtime/repo/wsgi/views/'))
    
    application=default_app()
else:
    bottle.run(host='localhost', port=8080)




#respuesta = cliente.service.GetStatusLinea("%s" % linea)
#raiz = etree.fromstring(respuesta.encode("utf-8"))
#raiz2 = raiz[0][0]
#ns = "{http://tempuri.org/}"
#print etree.tostring(raiz2, pretty_print=True)




#Posible formato de Timestamp:
	#Timestamp=2014-04-10T16:25:07.000Z
	
	
#busqueda = amazon.ItemSearch(SearchIndex=SearchIndex,
#ResponseGroup=ResponseGroup,
#Keywords=Keywords)

#datos = {"Service":"AWSECommerceService","Version":"2011-08-01","AssociateTag":"htttwicomale-21","Operation":"ItemSearch","SearchIndex":"Books","Keywords":"harry+potter","Timestamp":"2014-04-10T06:54:42.000Z","AWSAccessKeyId":"AKIAIJKV4RAQKPLTDABQ"}

#```python
# Required
#amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

# Search for a Specific Item
#response = amazon.ItemLookup(ItemId="B007OZNUCE")

# Search for Items by Keywords
#response = amazon.ItemSearch(Keywords="Kindle 3G", SearchIndex="All")

# Search for Images for an item
#response = amazon.ItemLookup(ItemId="1449372422", ResponseGroup="Images")

# Search for Similar Items
#response = amazon.SimilarityLookup(ItemId="B007OZNUCE")