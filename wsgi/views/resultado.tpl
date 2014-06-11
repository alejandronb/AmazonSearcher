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
			<p>Precio más bajo disponible: {{(lista[cont])["Precio"]}}</p>
			<p>Para ver los detalles pulse aquí: <a href= {{(lista[cont])["URLDetalles"]}}>Detalles</a></p>
			<img src="{{(lista[cont])["ImagenMediana"]}}"/>
			%cont = cont+1
		%end
	</body>
</html>
