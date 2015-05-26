<!DOCTYPE HTML>
<!--
	Iridium by TEMPLATED
    templated.co @templatedco
    Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>SoundSayer - {{nombre}}</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Arimo:400,700' rel='stylesheet' type='text/css'>
		<!--[if lte IE 8]><script src="/static/js/html5shiv.js"></script><![endif]-->
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="/static/js/skel.min.js"></script>
		<script src="/static/js/skel-panels.min.js"></script>
		<script src="/static/js/init.js"></script>
			<link rel="stylesheet" href="/static/css/skel-noscript.css" />
			<link rel="stylesheet" href="/static/css/style.css" />
			<link rel="stylesheet" href="/static/css/style-desktop.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="/static/css/ie/v8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="/static/css/ie/v9.css" /><![endif]-->
	</head>
	<body class="no-sidebar">

		<!-- Header -->
		<div id="header">
			<div class="container"> 
				
				<!-- Logo -->
				<div id="logo">
					<h1><a href="/">SOUNDSAYER</a></h1>
					<span><strong>Conociendo sus gustos</strong></span>
				</div>
				
				<!-- Nav -->
				<nav id="nav">
					<ul>
						<li><a href="/">Homepage</a></li>
					</ul>
				</nav>
			</div>

		<!-- Footer -->
		<div id="featured">
			<div class="container">
				<div class="row">
					<div class="-2u">
						<h2>Encuesta</h2>
						<p>En esta sección le realizaremos suna serie de preguntas para ajustar la lista a sus preferencias.
							<br>Por favor conteste a todas las cuestiones y su lista de reproducción será generada.
							<form name="gustos" action="envio_form" method="POST" accept-charset="utf-8">
								<ul>
									<li><label>Artista</label>
        							<input type="text" name="cantautor" placeholder="Introduzca Cantautor" 
        							required></li>
        							<li><label>Grupo</label>
        							<input type="text" name="Grupo" placeholder="Introduzca Grupo" 
        							required></li>
        							<li><label>Introduzca 5 canciones. Procure que sean de artistas variados.</label>
        							<br>
        							<input type="text" name="Cancion1" placeholder="Canción 1" 
        							required></li>
        							<input type="text" name="Cancion2" placeholder="Canción 2" 
        							required></li>
        							<input type="text" name="Cancion3" placeholder="Canción 3" 
        							required></li>
        							<input type="text" name="Cancion4" placeholder="Canción 4" 
        							required></li>
        							<input type="text" name="Cancion5" placeholder="Canción 5" 
        							required></li>
        							<br>
        							<li><label>Si tuviera que salir por España, que ciudad elijiría</label></li>
        							{{lista}}
        							required>
        							<li><input type="submit" value="Obtener lista de reproducción" class="button"></li>
        						</ul>
        					</form>
						</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Copyright -->
		<div id="copyright">
			<div class="container">
				Design: <a href="http://templated.co">TEMPLATED</a> Images: <a href="http://unsplash.com">Unsplash</a> (<a href="http://unsplash.com/cc0">CC0</a>)
			</div>
		</div>
		
	</body>
</html>