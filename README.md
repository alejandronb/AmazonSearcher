<<<<<<< HEAD
AmazonSearcher
==============

Esta aplicación diseñada en lenguaje Python tendrá como objetivo facilitar al cliente la búsqueda de productos dentro del catálogo de Amazon
y permitirle el acceso a la compra de los artículos disponibles.

#API
Para ello utilizará la siguiente API proporcionada por Amazon:
https://afiliados.amazon.es/gp/advertising/api/detail/main.html
=======
Bottle on OpenShift
===================

This git repository helps you get up and running quickly w/ a Bottle installation
on the Red Hat OpenShift PaaS.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com/

Create a python application

    rhc app create bottle python-2.6

Add this upstream bottle repo

    cd bottle
    git remote add upstream -m master git://github.com/openshift-quickstart/bottle-openshift-quickstart.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://bottle-$yournamespace.rhcloud.com
>>>>>>> 4d49cc3f1cd15855263b06a83528b8f5b6f9c82b

