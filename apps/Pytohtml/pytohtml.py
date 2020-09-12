#Ment()
import os
import time
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
"""
def Ment():
	title="""
#  ______     _                   _                     ____            _            
# |  ____|   | |                 | |                   |  _ \          (_)           
# | |__   ___| |_ _ __ _   _  ___| |_ _   _ _ __ __ _  | |_) | __ _ ___ _  ___ __ _  
# |  __| / __| __| '__| | | |/ __| __| | | | '__/ _` | |  _ < / _` / __| |/ __/ _` | 
# | |____\__ \ |_| |  | |_| | (__| |_| |_| | | | (_| | | |_) | (_| \__ \ | (_| (_| | 
# |______|___/\__|_|   \__,_|\___|\__|\__,_|_|  \__,_| |____/ \__,_|___/_|\___\__,_| 
#                                                                                    
#{0} HTML
#{1} CSS
#
#{9} EXIT
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
"""

sel=" "
res=" "
os.system('cls')
print('HTML')
print("""
	(0) GUIDED MODE
	(1) OUR OWN         
	(2) HTML                
	(3) CSS                 
	(9) CREADOR             
	""")
menu = input(str("OPTION NUMBER: "))

cod_textc = " "
title_namec = " "
name_cssc = " "

def escritura():
	filename = input("Escriba nombre del arhivo: ")
	extension = input("Extension: (example: txt ")
	add_content = "asd"
	fichero = open(filename+"."+extension,"w")
	fichero.write(add_content)
	fichero.close()
	os.system("\""+filename+"."+extension+"\"")



add_content=" "
	

def Menu():
	res = "{ OK }"
	if menu == "0":
	
		font_weight = "font-weight"
		font_variant = "font-variant"
		color = "color"
		font_family = "font-family"
		text_decoration = "text-decoration"
		letter_spacing = "letter-spacing"
		font_size = "font-size"
		text_transofrom = "text-transofrom"
		background_color = "background-color"
		font_style = "font-style"

		print("""
 (0)  font-weight
 (1)  text-decoration
 (2)  text-transofrom
 (3)  font-variant
 (4)  letter-spacing
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)


		sss_zero="""
(0) font-weight"""+" "+res
		sss_uno="""
(1) text-decoration"""+" "+res
		sss_dos="""
(2) text-transofrom"""+" "+res
		sss_tres="""
(3) font-variant"""+" "+res
		sss_cuatro="""
(4) letter-spacing"""+" "+res
		sss_cinco="""
(5) background-color"""+" "+res
		sss_seis="""
(6) color"""+" "+res
		sss_siete="""
(7) font-size"""+" "+res
		sss_ocho="""
(8) font-style"""+" "+res
		sss_nueve="""
(9) font-family"""+" "+res


	


	
################################################
################################################
################################################


###############################################################################################

		mode_0 = input("Do you want to add "+font_weight+" to you css file? y/N") 
		if mode_0 == "y" or "Y": 
			sel=" " 
			res="{ OK }" 
			os.system('cls') 
			print(""" 
		 { bolder / bold / normal / light / lighter | inherit / initial / unset / 500 / 600 / 700 / 800 / 900} 
					""") 
			font_weigh0tpropiety = input("Propiety: ") 
			mode_0 = sel+font_weight+":"+font_weigh0tpropiety+";"+sel 
		 
		elif mode_0 == "n" or "N": 
			sel="/*" 
			res="{ X }" 
			font_weigh0tpropiety = " " 
			mode_0 = sel+font_weight+":"+font_weigh0tpropiety+";"+sel 
		 
		else: 
			sel="/*" 
			res="{ X }" 
			font_weigh0tpropiety = " " 
			mode_0 = sel+font_weight+":"+font_wfont_weigh0tpropiety+";"+sel 
			print("""
"""+sss_uno+"""
 (1)  text-decoration
 (2)  text-transofrom
 (3)  font-variant
 (4)  letter-spacing
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)

		############################################################################################### 
		 
		mode_1 = input("Do you want to add "+font_variant+" to you css file? y/N") 
		if mode_1 == "y" or "Y": 
			sel=" "	 
			res="{ OK }" 
			os.system('cls') 
			print(""" 
		 { normal / small-caps | inherit / initial / unset } 
					""") 
			nt_varia1ntpropiety = input("Propiety: ") 
			mode_1 = sel+font_variant+":"+nt_varia1ntpropiety+";"+sel 
		 
		elif mode_1 == "n" or "N": 
			sel="/*" 
			res="{ X }" 
			nt_varia1ntpropiety = " " 
			mode_1 = sel+font_variant+":"+nt_varia1ntpropiety+";"+sel 
		
		else:
			sel="/*"
			res="{ X }"
			nt_varia1ntpropiety = " "
			mode_1 = sel+font_variant+":"+nt_varia1ntpropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
 (2)  text-transofrom
 (3)  font-variant
 (4)  letter-spacing
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)
		###############################################################################################
		
		mode_2 = input("Do you want to add "+color+" to you css file? y/N")
		if mode_2 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { Name Color or Color Code with # before }
					""")
			colorpi2ety = input("Propiety: ")
			mode_2 = sel+color+ sel+":"+colorpi2ety+";"+sel
		
		elif mode_2 == "n" or "N":
			sel="/*"
			res="{ X }"
			colorpi2ety = " "
			mode_2 = sel+color+ sel+":"+colorpi2ety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			colorpi2ety = " "
			mode_2 = sel+color+ sel+":"+colorpi2ety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
 (3)  font-variant
 (4)  letter-spacing
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)

		###############################################################################################
		
		mode_3 = input("Do you want to add "+font_family+" to you css file? y/N")
		if mode_3 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 Arial, sans-serif	
		 Helvetica, sans-serif	
		 Verana, sans-serif	
		 Treuchet MS, sans-serif	
		 Gill Sans, sans-serif	
		 Noo Sans, sans-serif	
		 Avntgarde, TeX Gyre Adventor, URW Gothic L, sans-serif	
		 Opima, sans-serif	
		 Aral Narrow, sans-serif	
		 sas-serif
		 Times, Times New Roman, serif	
		 Diot, serif	
		 Gergia, serif	
		 Paatino, URW Palladio L, serif	
		 Bokman, URW Bookman L, serif	
		 Ne Century Schoolbook, TeX Gyre Schola, serif	
		 American Typewriter, serif	
		 serif	
		 Andale Mono, monospace	
		 Courier New, monospace	
		 Courier, monospace	
		 FreeMono, monospace	
		 OCR A Std, monospace	
		 DejaVu Sans Mono, monospace	
		 monospace	
		 Comic Sans MS, Comic Sans, cursive	
		 Apple Chancery, cursive	
		 Bradley Hand, cursive	
		 Brush Script MT, Brush Script Std, cursive	
		 Snell Roundhand, cursive	
		 URW Chancery L, cursive	
		 cursive	
		 Impact, fantasy	
		 Luminari, fantasy	
		 Chalkduster, fantasy	
		 Jazz LET, fantasy	
		 Blippo, fantasy	
		 Stencil Std, fantasy	
	 Marker Felt, fantasy	
		 Trattatello, fantasy											
		 fantasy""")
			font_famil3ypropiety = input("Propiety: ")
			mode_3 = sel+font_family+":"+font_famil3ypropiety+";"+sel
		
		elif mode_3 == "n" or "N":
				sel="/*"
				res="{ X }"
				font_famil3ypropiety = " "
				mode_3 = sel+font_family+":"+font_famil3ypropiety+";"+sel
		
		else:
				sel="/*"
				res="{ X }"
				font_famil3ypropiety = " "
				mode_3 = sel+font_family+":"+font_famil3ypropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
 (4)  letter-spacing
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)

		###############################################################################################
		
		mode_4 = input("Do you want to add "+text_decoration+" to you css file? y/N")
		if mode_4 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { line-through overline underline | Dashed / Dotted / Double / None / Solid / Wavy }
					""")
			decor4ationpropiety = input("Propiety: ")
			mode_4 = sel+text_decoration+":"+decor4ationpropiety+";"+sel
		
		elif mode_4 == "n" or "N":
			sel="/*"
			res="{ X }"
			decor4ationpropiety = " "
			mode_4 = sel+text_decoration+":"+decor4ationpropiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			decor4ationpropiety = " "
			mode_4 = sel+text_decoration+":"+decor4ationpropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
 (5)  background-color
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)
		###############################################################################################
		
		mode_5 = input("Do you want to add "+letter_spacing+" to you css file? y/N")
		if mode_5 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { normal / 5 px / 5 cm / 5 mm / 5 rem }
					""")
			er_spa5cingpropiety = input("Propiety: ")
			mode_5 = sel+letter_spacing+":"+er_spa5cingpropiety+";"+sel
		
		elif mode_5 == "n" or "N":
			sel="/*"
			res="{ X }"
			er_spa5cingpropiety = " "
			mode_5 = sel+letter_spacing+":"+er_spa5cingpropiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			er_spa5cingpropiety = " "
			mode_5 = sel+letter_spacing+":"+er_spa5cingpropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
"""+sss_cinco+"""
 (6)  color
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)
		###############################################################################################
		
		mode_6 = input("Do you want to add "+font_size+" to you css file? y/N")
		if mode_6 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { xx-large / x-large / larger / large / medium / small / smaller / x-small / xx-small }
					""")
			font_sizep6ropiety = input("Propiety: ")
			mode_6 = sel+font_size+":"+font_sizep6ropiety+";"+sel
		
		elif mode_6 == "n" or "N":
			sel="/*"
			res="{ X }"
			font_sizep6ropiety = " "
			mode_6 = sel+font_size++":"+font_sizep6ropiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			font_sizep6ropiety = " "
			mode_6 = sel+font_size++":"+font_sizep6ropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
"""+sss_cinco+"""
"""+sss_seis+"""
 (7)  font-size
 (8)  font-style
 (9)  font-family
 """)
		###############################################################################################
		
		mode_7 = input("Do you want to add "+text_transofrom+" to you css file? y/N")
		if mode_7 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { Capitalize / Lowercase / Uppercase | None }
						""")
			trans7ofrompropiety = input("Propiety: ")
			mode_7 = sel+text_transofrom+":"+trans7ofrompropiety+";"+sel
		
		elif mode_7 == "n" or "N":
			sel="/*"
			res="{ X }"
			trans7ofrompropiety = " "
			mode_7 = sel+text_transofrom+":"+trans7ofrompropiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			trans7ofrompropiety = " "
			mode_7 = sel+text_transofrom+":"+trans7ofrompropiety+";"+sel
		
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
"""+sss_cinco+"""
"""+sss_seis+"""
"""+sss_siete+"""
 (8)  font-style
 (9)  font-family
 """)
		###############################################################################################
		
		mode_8 = input("Do you want to add "+background_color+" to you css file? y/N")
		if mode_8 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { Name Color or Color Code with # before }
					""")
			ound8_ropiety = input("Propiety: ")
			mode_8 = sel+background_color+":"+ound8_ropiety+";"+sel
		
		elif mode_8 == "n" or "N":
			sel="/*"
			res="{ X }"
			ound8_ropiety = " "
			mode_8 = sel+background_color+":"+ound8_ropiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			mode_8 = sel+background_color+se
		print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
"""+sss_cinco+"""
"""+sss_seis+"""
"""+sss_siete+"""
"""+sss_ocho+"""
 (9)  font-family
""")
		###############################################################################################
		
		mode_9 = input("Do you want to add "+font_style+" to you css file? y/N")
		if mode_9 == "y" or "Y":
			sel=" "	
			res="{ OK }"
			os.system('cls')
			print("""
		 { italic / normal / oblique | inherit / initial / unset }
					""")
			tyle9propiety = input("Propiety: ")
			mode_9 = sel+font_style+":"+tyle9propiety+";"+sel
		
		elif mode_9 == "n" or "N":
			sel="/*"
			res="{ X }"
			tyle9propiety = " "
			mode_9 = sel+font_style+":"+tyle9propiety+";"+sel
		
		else:
			sel="/*"
			res="{ X }"
			tyle9propiety = " "
			mode_9 = sel+font_style+":"+tyle9propiety+";"+sel
			print("""
"""+sss_zero+"""
"""+sss_uno+"""
"""+sss_dos+"""
"""+sss_tres+"""
"""+sss_cuatro+"""
"""+sss_cinco+"""
"""+sss_seis+"""
"""+sss_siete+"""
"""+sss_ocho+"""
"""+sss_nueve)

			os.system('cls')
			print(mode_1)
			print(mode_2)
			print(mode_3)
			print(mode_4)
			print(mode_5)
			print(mode_6)
			print(mode_7)
			print(mode_8)
			print(mode_9)
		
		
		################################################
		################################################
		################################################
		
		
		
		
		clis=input("Clase: ")
		css_addcontent="""
		<style>
		"""+"."+clis+"{"+"""
		"""+mode_1+"""
		"""+mode_2+"""
		"""+mode_3+"""
		"""+mode_4+"""
		"""+mode_5+"""
		"""+mode_6+"""
		"""+mode_7+"""
		"""+mode_8+"""
		"""+mode_9+"""
		}
		</style>"""
		filename = input("Filename: ")
		extension = input("Extension: ")
		title_namec = input("Title: ")
		cod_textc = input("Codification: ")
		html_ini="<html>"
		head_ini="<head>"
		title="<title>"+title_namec+"</title>"
		cod_body="<meta charset=\""+"\""+cod_textc+"\">"""
		contenido_body="""</head>
		<body>
		<!-- Enter your content code here -->
		<!-- Example content code -->
		<h1>Example title</h1>
		<font class="""+clis+""">EXAMPLE</font> <font class="class2">TEXT</font>
		<!-- End Example content code -->
		</body>
		</html>
		"""
		print(" ") 
		print(html_ini) 
		print(head_ini) 
		print(title) 
		print(cod_body) 
		print(css_addcontent) 
		print(contenido_body) 
		add_content=str((html_ini+ """ 
			 """+head_ini+""" 
			 """+title+""" 
			 """+cod_body+""" 
			 """+css_addcontent+""" 
			 """+contenido_body))	
			 
			#crea el archivo y lo guarda 
		print(add_content) 
		fichero = open(filename+"."+extension,"w") 
		fichero.write(add_content) 
		fichero.close() 
		os.system("\""+filename+"."+extension+"\"") 

if menu =="1":
	filename = input("Escriba nombre del arhivo: ")
	extension = input("Extension: (example: txt ")
	print("DOC "+filename+" - "+" 50 Lines Maximum")
	os.system("\""+Documentation_css+"\"")
	os.system("\""+Documentation_html+"\"")
	os.system("\""+Documentation_struct+"\"")
	line_1 = input(str(" 1 "))
	line_2 = input(str(" 2 "))
	line_3 = input(str(" 3 "))
	line_4 = input(str(" 4 "))
	line_5 = input(str(" 5 "))
	line_6 = input(str(" 6 "))
	line_7 = input(str(" 7 "))
	line_8 = input(str(" 8 "))
	line_9 = input(str(" 9 "))
	line10 = input(str("10 "))
	line11 = input(str("11 "))
	line12 = input(str("12 "))
	line13 = input(str("13 "))
	line14 = input(str("14 "))
	line15 = input(str("15 "))
	line16 = input(str("16 "))
	line17 = input(str("17 "))
	line18 = input(str("18 "))
	line19 = input(str("19 "))
	line20 = input(str("20 "))
	line21 = input(str("21 "))
	line22 = input(str("22 "))
	line23 = input(str("23 "))
	line24 = input(str("24 "))
	line25 = input(str("25 "))
	line26 = input(str("26 "))
	line27 = input(str("27 "))
	line28 = input(str("28 "))
	line29 = input(str("29 "))
	line30 = input(str("30 "))
	line31 = input(str("31 "))
	line32 = input(str("32 "))
	line33 = input(str("33 "))
	line34 = input(str("34 "))
	line35 = input(str("35 "))
	line36 = input(str("36 "))
	line37 = input(str("37 "))
	line38 = input(str("38 "))
	line39 = input(str("39 "))
	line40 = input(str("40 "))
	line41 = input(str("41 "))
	line42 = input(str("42 "))
	line43 = input(str("43 "))
	line44 = input(str("44 "))
	line45 = input(str("45 "))
	line46 = input(str("46 "))
	line47 = input(str("47 "))
	line48 = input(str("48 "))
	line49 = input(str("49 "))
	line50 = input(str("50 "))
	os.system('cls')
	add_content=str("""
	"""+" "+line_1
		+"""
	"""+" "+line_2
		+"""
	"""+" "+line_3
		+"""
	"""+" "+line_4
		+"""
	"""+" "+line_5
		+"""
	"""+" "+line_6
		+"""
	"""+" "+line_7
		+"""
	"""+" "+line_8
		+"""
	"""+" "+line_9
		+"""
	"""+" "+line10
		+"""
	"""+" "+line11
		+"""
	"""+" "+line12
		+"""
	"""+" "+line13
		+"""
	"""+" "+line14
		+"""
	"""+" "+line15
		+"""
	"""+" "+line16
		+"""
	"""+" "+line17
		+"""
	"""+" "+line18
		+"""
	"""+" "+line19
		+"""
	"""+" "+line20
		+"""
	"""+" "+line21
		+"""
	"""+" "+line22
		+"""
	"""+" "+line23
		+"""
	"""+" "+line24
		+"""
	"""+" "+line25
		+"""
	"""+" "+line26
		+"""
	"""+" "+line27
		+"""
	"""+" "+line28
		+"""
	"""+" "+line29
		+"""
	"""+" "+line30
		+"""
	"""+" "+line31
		+"""
	"""+" "+line32
		+"""
	"""+" "+line33
		+"""
	"""+" "+line34
		+"""
	"""+" "+line35
		+"""
	"""+" "+line36
		+"""
	"""+" "+line37
		+"""
	"""+" "+line38
		+"""
	"""+" "+line39
		+"""
	"""+" "+line40
		+"""
	"""+" "+line41
		+"""
	"""+" "+line42
		+"""
	"""+" "+line43
		+"""
	"""+" "+line44
		+"""
	"""+" "+line45
		+"""
	"""+" "+line46
		+"""
	"""+" "+line47
		+"""
	"""+" "+line48
		+"""
	"""+" "+line49
		+"""
	"""+" "+line50)
	print(add_content)
	fichero = open(filename+"."+extension,"w")
	fichero.write(add_content)
	fichero.close()
	os.system("\""+filename+"."+extension+"\"")

elif menu =="2":
	def CssName():
		name_cssc = input("CSS FILE NAME: ")
		print("Insert HTML TITLE")
		title_namec = input("TITLE: ")

	def COD_TEXT():
		cod_textc = input (''' Which coding do you want to use?
			ASCII    ANSI    ISO-8859-1    UTF-8
 Codification Name: ''')
	CssName()
	title_namec = input("File title: ")
	cod_textc = input("Codification: ")
	name_cssc = input("Css file Name: ")
	html_ini="<html>"
	head_ini="<head>"
	title="<title>"+title_namec+"</title>"
	cod_body="<meta charset=\""+"\""+cod_textc+"\">"""
	link_body="""<link rel=\"stylesheet\" type=\"text/css\" href=\""""+name_cssc+".css"+"\""+">"""
	contenido_body="""</head>
		<body>
		<!-- Enter your content code here -->
		<!-- Example content code -->
		<h1>Example title</h1>
		<font class="class1">EXAMPLE</font> <font class="class2">TEXT</font>
		<!-- End Example content code -->
		</body>
		</html>
		"""
	print(" ")
	print(html_ini)
	print(head_ini)
	print(title)
	print(cod_body)
	print(link_body)
	print(contenido_body)
	add_content=str((html_ini+"""
		 """+head_ini+"""
		 """+title+"""
		 """+cod_body+"""
		 """+link_body+"""
		 """+contenido_body))
	filename = input("Escriba nombre del arhivo: ")
	extension = input("Extension: (example: txt ")
	os.system('cls')
	print(add_content)
	fichero = open(filename+"."+extension,"w")
	fichero.write(add_content)
	fichero.close()
	os.system("\""+filename+"."+extension+"\"")


elif menu =="3":
	print("""
 (0)  font-weight        (3)  font-variant       (6)  color              (9)  font-family
 (1)  text-decoration    (4)  letter-spacing     (7)  font-size          
 (2)  text-transofrom    (5)  background-color   (8)  font-style            

			""")

	propiety_instyle = input(str(" Propiety Name: "))
		#Propiedades

	if propiety_instyle == "font-weight":
			print("""
 { bolder / bold / normal / light / lighter | inherit / initial / unset / 500 / 600 / 700 / 800 / 900}
			""")

	elif propiety_instyle == "text-decoration":
			print("""
 { line-through overline underline | Dashed / Dotted / Double / None / Solid / Wavy }
			""")
	elif propiety_instyle == "text-transform":
			print("""
 { Capitalize / Lowercase / Uppercase | None }
				""")

	elif propiety_instyle == "font-variant" :
			print("""
 { normal / small-caps | inherit / initial / unset }
			""")

	elif propiety_instyle == "letter-spacing" :
			print("""
 { normal / 5 px / 5 cm / 5 mm / 5 rem }
			""")

	elif propiety_instyle == "background-color":
			print("""
 { Name Color or Color Code with # before }
			""")

	elif propiety_instyle == "color":
			print("""
 { Name Color or Color Code with # before }
			""")

	elif propiety_instyle == "font-size":
			print("""
 { xx-large / x-large / larger / large / medium / small / smaller / x-small / xx-small }
			""")


	elif propiety_instyle == "font-style" :
			print("""
 { italic / normal / oblique | inherit / initial / unset }
			""")

	elif propiety_instyle == "font-family":
			print("""
 Arial, sans-serif	
 Helvetica, sans-serif	
 Verdana, sans-serif	
 Trebuchet MS, sans-serif	
 Gill Sans, sans-serif	
 Noto Sans, sans-serif	
 Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif	
 Optima, sans-serif	
 Arial Narrow, sans-serif	
 sans-serif
 Times, Times New Roman, serif	
 Didot, serif	
 Georgia, serif	
 Palatino, URW Palladio L, serif	
 Bookman, URW Bookman L, serif	
 New Century Schoolbook, TeX Gyre Schola, serif	
 American Typewriter, serif	
 serif	
 Andale Mono, monospace	
 Courier New, monospace	
 Courier, monospace	
 FreeMono, monospace	
 OCR A Std, monospace	
 DejaVu Sans Mono, monospace	
 monospace	
 Comic Sans MS, Comic Sans, cursive	
 Apple Chancery, cursive	
 Bradley Hand, cursive	
 Brush Script MT, Brush Script Std, cursive	
 Snell Roundhand, cursive	
 URW Chancery L, cursive	
 cursive	
 Impact, fantasy	
 Luminari, fantasy	
 Chalkduster, fantasy	
 Jazz LET, fantasy	
 Blippo, fantasy	
 Stencil Std, fantasy	
 Marker Felt, fantasy	
 Trattatello, fantasy											
 fantasy""")

	propiety_instyle_1 = input(str(" Propiety Code: "))
	os.system('cls')
	print(propiety_instyle+":"+propiety_instyle_1+";")
	print("""
 (0)  font-weight        (3)  font-variant       (6)  color              (9)  font-family
 (1)  text-decoration    (4)  letter-spacing     (7)  font-size          
 (2)  text-transofrom    (5)  background-color   (8)  font-style            

			""")
	propiety_instyle_2 = input(str(" Propiety Name: "))

	if propiety_instyle_2 == "font-weight":
				print("""
 { bolder / bold / normal / light / lighter | inherit / initial / unset / 500 / 600 / 700 / 800 / 900}
			""")

	elif propiety_instyle_2 == "text-decoration":
				print("""
 { line-through overline underline | Dashed / Dotted / Double / None / Solid / Wavy }
			""")
	elif propiety_instyle_2 == "text-transform":
			print("""
 { Capitalize / Lowercase / Uppercase | None }
				""")
	elif propiety_instyle_2 == "font-variant" :
			print("""
 { normal / small-caps | inherit / initial / unset }
			""")

	elif propiety_instyle_2 == "letter-spacing" :
			print("""
 { normal / 5 px / 5 cm / 5 mm / 5 rem }
			""")

	elif propiety_instyle_2 == "background-color":
				print("""
 { Name Color or Color Code with # before }
			""")

	elif propiety_instyle_2 == "color":
				print("""
 { Name Color or Color Code with # before }
			""")

	elif propiety_instyle_2 == "font-size":
			print("""
 { xx-large / x-large / larger / large / medium / small / smaller / x-small / xx-small }
			""")


	elif propiety_instyle_2 == "font-style" :
			print("""
 { italic / normal / oblique | inherit / initial / unset }
			""")

	elif propiety_instyle_2 == "font-family":
			print("""
 Arial, sans-serif	
 Helvetica, sans-serif	
 Verdana, sans-serif	
 Trebuchet MS, sans-serif	
 Gill Sans, sans-serif	
 Noto Sans, sans-serif	
 Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif	
 Optima, sans-serif	
 Arial Narrow, sans-serif	
 sans-serif
 Times, Times New Roman, serif	
 Didot, serif	
 Georgia, serif	
 Palatino, URW Palladio L, serif	
 Bookman, URW Bookman L, serif	
 New Century Schoolbook, TeX Gyre Schola, serif	
 American Typewriter, serif	
 serif	
 Andale Mono, monospace	
 Courier New, monospace	
 Courier, monospace	
 FreeMono, monospace	
 OCR A Std, monospace	
 DejaVu Sans Mono, monospace	
 monospace	
 Comic Sans MS, Comic Sans, cursive	
 Apple Chancery, cursive	
 Bradley Hand, cursive	
 Brush Script MT, Brush Script Std, cursive	
 Snell Roundhand, cursive	
 URW Chancery L, cursive	
 cursive	
 Impact, fantasy	
 Luminari, fantasy	
 Chalkduster, fantasy	
 Jazz LET, fantasy	
 Blippo, fantasy	
 Stencil Std, fantasy	
 Marker Felt, fantasy	
 Trattatello, fantasy											
 fantasy""")
	propiety_instyle_2_2 = input(str(" Propiety Code: "))
	os.system('cls')
	print(" ")
	print(" "+propiety_instyle+":"+propiety_instyle_1+";")
	print(" "+propiety_instyle_2+":"+propiety_instyle_2_2+";")
	spam = input('Press Enter To Continue')
	os.system('cls')
	un = (" Contenido del documento style.css")
	dos=(" "+propiety_instyle+":"+propiety_instyle_1+";")
	tres=("   "+propiety_instyle_2+":"+propiety_instyle_2_2+";")
	quatre ="  }"
	print(un)
	print(dos)
	print(tres)
	print(quatre)
	spam = input('Press Enter To Continue')
	os.system('cls')
	add_content="""
	 """+un+"""
	 """+dos+"""
	 """+tres+"""
	 """+quatre

	
elif menu =="4":
	escritura()
		
elif menu =="9":
	print('Created By Jordi Serrano')

else:
		print("PARAMETRO NO FUNCIONAL")

Menu()
