<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns ="http://www.w3.org/1999/xhtml" xml:lang="es">
	<head>
		<title>Amazon Searcher</title>
		<!-- <link rel="stylesheet" type="text/css" href="style/estilo.css"> -->
		<style type="text/css">
  			h1 { color: red;  font-family: Arial;   font-size: large;  }
 			p  { color: gray; font-family: Verdana; font-size: medium; }
 			body { background: #16a085; }
		</style>
	</head>
	<body>
		<h1>Amazon Searcher</h1>
		<form action = '/busqueda' method='POST'>
			<p>Bienvenido, introduce el artículo a buscar.</p>
			<input type = 'text' name='articulo' size='50'/>
			<input type = 'submit' value='Buscar'/>
		</form>
	</body>
</html>





