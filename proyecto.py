#coding: utf-8
import requests
import webbrowser
import bottle
from lxml import etree
import bottlenose

assoc_tag = "htttwicomale-21"

#Las claves están en otro fichero
AWS = "" 
secret_key = ""

amazon = bottlenose.Amazon(AWS,secret_key,assoc_tag)

@bottle.get('/') # o @bottle.route
def home_page():
	return bottle.template('index.tpl')


@bottle.post('/busqueda')
def busqueda():
	articulo = bottle.request.forms.get("articulo")
	respuesta = amazon.ItemSearch(Keywords=articulo, SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")
	raiz = etree.fromstring(respuesta)
	ns = "{http://webservices.amazon.com/AWSECommerceService/2011-08-01}"
	listaresultados = raiz[1]
	NumResultados = listaresultados.find(ns+"TotalResults").text #Pongo el .text al final para que obtenga directamente el valor de la etiqueta
	#MasResultados = listaresultados.find(ns+"MoreSearchResults").text
	Item = listaresultados.find(ns+"Item")
	URLDetallesProducto = Item.find(ns+"DetailPageURL").text
	ItemLinks = Item.find(ns+"ItemLinks")
	ItemLink = ItemLinks.find(ns+"ItemLink")
	Atributos = Item.find(ns+"ItemAttributes")
	Fabricante = Atributos.find(ns+"Manufacturer").text
	TituloProducto = Atributos.find(ns+"Title").text
	return bottle.template('resultado.tpl', {'articulo':articulo,'NumResultados':NumResultados,'URLDetallesProducto':URLDetallesProducto})


#Mirar lo de la etiqueta MoreSearchResults

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

