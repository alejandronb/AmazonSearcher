#coding: utf-8
import requests
import webbrowser
from lxml import etree
import bottle
import bottlenose

assoc_tag = "htttwicomale-21"

AWS = "AKIAIJKV4RAQKPLTDABQ"

secret_key = "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"

amazon = bottlenose.Amazon(AWS,secret_key,assoc_tag)

#libro = raw_input("Introduce el libro a buscar: ")

respuesta = amazon.ItemSearch(Keywords="Kindle 3G", SearchIndex="All", Service="AWSECommerceService", Version="2011-08-01")

print respuesta



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

