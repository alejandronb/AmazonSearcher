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