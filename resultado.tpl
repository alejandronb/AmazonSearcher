<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns ="http://www.w3.org/1999/xhtml"xml:lang="es">
	<head>
		<title>Amazon Searcher</title>
	</head>
	<body>
		<h1>Amazon Searcher</h1>
<!-- 		<p>Estos son los resultados de: {{articulo}}</p>
		<p>Número de resultados: {{NumResultados}}</p>
		<p>Para ver los detalles del producto: <a href={{URLDetallesProducto}}>Detalles</a></p> -->
			{% for i in range({cantidad}) %}
				<p>Detalles del producto: {{URLDetallesProducto}}</p>
			{% endfor %}
	</body>
</html>
