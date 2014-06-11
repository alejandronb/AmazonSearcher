#coding: utf-8
import requests
import webbrowser
import bottle
from lxml import etree
import bottlenose

assoc_tag = "htttwicomale-21"

#Las claves están en otro fichero
AWS = "AKIAITEYKKIRSCQEKTMQ" 
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
	NumResultados = raiz.xpath("//ns:TotalResults/text()", namespaces={"ns":ns})
	Items = raiz.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
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
				# ASIN = i.text
				respuestaPrecios = amazon.ItemLookup(ItemId=i.text, ResponseGroup="OfferSummary")
				precios = etree.fromstring(respuestaPrecios)
				ItemsPrecio = precios.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
				for Item in ItemsPrecio:
					for i in Item:
						if i.tag == "{%s}OfferSummary" % ns:
							for j in i:
								if j.tag == "{%s}LowestNewPrice" % ns:
									for x in j:
										if x.tag == "{%s}FormattedPrice" % ns:
											diccionario["Precio"] = x.text

				respuestaImagenes = amazon.ItemLookup(ItemId=i.text, ResponseGroup="Images")
				imagenes = etree.fromstring(respuestaImagenes)
				ItemsImagenes = imagenes.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
				for Item in ItemsImagenes:
					for i in Item:
						if i.tag == "{%s}MediumImage" % ns:
							for j in i:
								if j.tag == "{%s}URL" % ns:
									diccionario["ImagenMediana"] = j.text
						elif i.tag == "{%s}LargeImage" % ns:
							for j in i:
								if j.tag == "{%s}URL" % ns:
									diccionario["ImagenGrande"] = j.text

		lista.append(diccionario)

	return bottle.template('resultado.tpl', {'lista':lista})


#Estructura para obtener el precio:
# for Item in ItemsPrecio:
# 	for i in Item:
#         if i.tag == "{%s}OfferSummary" % ns:
#             for j in i:
#                 if j.tag == "{%s}LowestNewPrice" % ns:
#                     for x in j:
#                         if x.tag == "{%s}FormattedPrice" % ns:
#                             print x.text



# Búsqueda de imágenes o precio para un Item:
#response = amazon.ItemLookup(ItemId="B00AWH595M", ResponseGroup="Images")
#response = amazon.ItemLookup(ItemId="B00AWH595M", ResponseGroup="OfferSummary")


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



# Utilización de etree (anterior a xpath)
#	URLDetallesProducto = raiz.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:DetailPageURL/text()",namespaces={"ns":ns})
#	for i in URLDetallesProducto:
#		Resultado1 = URLDetallesProducto[i]
	# URLDetallesProducto = Item.find(ns+"DetailPageURL").text
	#NumResultados = listaresultados.find(ns+"TotalResults").text #Pongo el .text al final para que obtenga directamente el valor de la etiqueta
	# ItemLinks = Item.find(ns+"ItemLinks")
	# ItemLink = ItemLinks.find(ns+"ItemLink")
	# Item = listaresultados.find(ns+"Item")
	# Atributos = Item.find(ns+"ItemAttributes")
	# Fabricante = Atributos.find(ns+"Manufacturer").text
	# TituloProducto = Atributos.find(ns+"Title").text
	# return bottle.template('resultado.tpl', {'articulo':articulo,'NumResultados':NumResultados,'URLDetallesProducto':URLDetallesProducto})
	#listaresultados = raiz.find(ns+"Items") Sustituir el de arriba por este


#Esto es para vincular las hojas de estilo
@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static')

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
from bottle import default_app

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
                                      'app-root/repo/wsgi/views/'))
    
    application=default_app()
else:
    bottle.run(host='localhost', port=8080)





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