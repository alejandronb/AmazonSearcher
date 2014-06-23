#coding: utf-8
import requests
import webbrowser
import bottle
from lxml import etree
import bottlenose
import socket

# timeout = 50
# socket.setdefaulttimeout(timeout)

assoc_tag = "htttwicomale-21"
#Las claves están en otro fichero
AWS = "AKIAITEYKKIRSCQEKTMQ" 
secret_key = "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"
amazon = bottlenose.Amazon(AWS,secret_key,assoc_tag)

@bottle.get('/') # o @bottle.route
def home_page():
	return bottle.template('index.tpl')

@bottle.post('/busqueda')
def busqueda():
	articulo = bottle.request.forms.get("articulo")
	respuesta = amazon.ItemSearch(Keywords=articulo, SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01") #Petición a la API
	raiz = etree.fromstring(respuesta)
	ns = "http://webservices.amazon.com/AWSECommerceService/2011-08-01"
	Items = raiz.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
	lista = []
	for Item in Items:
		diccionario = {}
		for i in Item:
			if i.tag == "{%s}ItemAttributes" % ns:
				for j in i:
					if j.tag == "{%s}Title" % ns:
						diccionario["Titulo"] = j.text #Aquí obtenemos el nombre del producto
			elif i.tag == "{%s}DetailPageURL" %ns:
				diccionario["URLDetalles"] = i.text
			elif i.tag == "{%s}ASIN" % ns:
				respuestaImagenes = amazon.ItemLookup(ItemId=i.text, ResponseGroup="Images") #Aquí pedimos imagen por cada id de producto
				imagenes = etree.fromstring(respuestaImagenes)
				ItemsImagenes = imagenes.xpath("//ns:Item",namespaces={"ns":"http://webservices.amazon.com/AWSECommerceService/2011-08-01"})
				for Item in ItemsImagenes:
					for i in Item:
						if i.tag == "{%s}MediumImage" % ns:
							for j in i:
								if j.tag == "{%s}URL" % ns:
									diccionario["ImagenMediana"] = j.text
						# elif i.tag == "{%s}LargeImage" % ns:
						# 	for j in i:
						# 		if j.tag == "{%s}URL" % ns:
						# 			diccionario["ImagenGrande"] = j.text

		lista.append(diccionario)

	return bottle.template('resultado.tpl', {'lista':lista})

#Esto es para vincular las hojas de estilo
@bottle.route('/static/<filename>')
def server_static(filename):
  return bottle.static_file(filename, root='./static')

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