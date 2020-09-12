#Documentation_struct
estrucutra_html="""
<!DOCTYPE HTML>			
<html>			
	<head>			
		<meta charset="utf-8">
		<title>
			Titulo de la pestaña
		</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>			
	
	<body>
		<p>texto de la paguina web</p>
	</body>
	
	<script>     
	             
	</script>

</html>
"""
estrucutra_css="""
/* Nombre del Archivo Normalmente Llamado style.css /*
.Class {
  Propiety:Value;
  Propiety:Value;
}
"""
def Ment():
	title="""
  ______     _                   _                     ____            _            
 |  ____|   | |                 | |                   |  _ \          (_)           
 | |__   ___| |_ _ __ _   _  ___| |_ _   _ _ __ __ _  | |_) | __ _ ___ _  ___ __ _  
 |  __| / __| __| '__| | | |/ __| __| | | | '__/ _` | |  _ < / _` / __| |/ __/ _` | 
 | |____\__ \ |_| |  | |_| | (__| |_| |_| | | | (_| | | |_) | (_| \__ \ | (_| (_| | 
 |______|___/\__|_|   \__,_|\___|\__|\__,_|_|  \__,_| |____/ \__,_|___/_|\___\__,_| 
                                                                                    
{0} HTML
{1} CSS

{9} EXIT
"""                                                                                  
	title_chose=input("Opcion: ")

	elif title_chose == "0" or "HTML":
		print(estrucutra_html)
	elif title_chose == "1" or "HTML":
		print(estructura_css)
	elif title_chose == "9" or "HTML":
		exit()
	else:
		Ment()
