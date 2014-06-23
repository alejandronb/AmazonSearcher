<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns ="http://www.w3.org/1999/xhtml"xml:lang="es">
	<head>
		<title>Amazon Searcher</title>
		<!-- Bootstrap core CSS -->
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css" rel="stylesheet">
		<link href="/static/estiloresultado.css" rel="stylesheet">
	</head>
	<body>
		<h1>Amazon Searcher</h1>
		<h2>Pulsa sobre el título para mas información</h2>
		<div class="row">
		%cont = 0
		%for i in lista:
            <div class="col-md-3">
                <a href="{{(lista[cont])["ImagenGrande"]}}"><img src="{{(lista[cont])["ImagenMediana"]}}"/></a>
                <div class="texto">
                    <a href= {{(lista[cont])["URLDetalles"]}}>{{(lista[cont])["Titulo"]}}</a>
                </div>
            </div>
			%cont = cont+1
		%end
		</div>
	</body>
</html>
