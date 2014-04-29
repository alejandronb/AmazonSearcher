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
 	return bottle.template('resultado.tpl', {'articulo':articulo})
 	respuesta = amazon.ItemSearch(Keywords=articulo, SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")
 	arbol = etree.fromstring(respuesta)
 	raiz = arbol.find("ItemSearchResponse")
 	listaitems = raiz.find("Items")
 	NumResultados = listaitems.find("TotalResults")



 # respuesta = amazon.ItemSearch(Keywords="Kindle", SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")
 # arbol = etree.fromstring(respuesta)
 # raiz = arbol.find("ItemSearchResponse")
 # listaitems = raiz.find("Items")
 # NumResultados = listaitems.find("TotalResults")








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

