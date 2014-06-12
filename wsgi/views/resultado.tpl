<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns ="http://www.w3.org/1999/xhtml"xml:lang="es">
	<head>
		<title>Amazon Searcher</title>
	</head>
	<body>
		<h1>Amazon Searcher</h1>
		%cont = 0
		%for i in lista:
			<p>Producto: {{(lista[cont])["Titulo"]}}</p>
			<p>Para ver los detalles pulse aquí: <a href= {{(lista[cont])["URLDetalles"]}}>Detalles</a></p>
			<a href="{{(lista[cont])["ImagenGrande"]}}"><img src="{{(lista[cont])["ImagenMediana"]}}"/></a>
			%cont = cont+1
		%end
	</body>
</html>
