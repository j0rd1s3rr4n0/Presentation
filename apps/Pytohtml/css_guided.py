print("""
 (0)  font-weight        (3)  font-variant       (6)  color              (9)  font-family
 (1)  text-decoration    (4)  letter-spacing     (7)  font-size          
 (2)  text-transofrom    (5)  background-color   (8)  font-style            

			""")
guided_mode = input(str("Class Name: "))
	
		
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
(8)  font-style"""+" "+res
sss_nueve="""
(9) font-family"""+" "+res

################################################
################################################
################################################
def SVS_zero():
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

def SVS_uno():
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

def SVS_dos():
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

def SVS_tres():
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

def SVS_cuatro():
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

def SVS_cinco():
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

def SVS_seis():
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

def SVS_siete():
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

def SVS_ocho():
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
		eigh0tpropiety = input("Propiety: ")
		mode_0 = sel+font_weight+ont_w":"+eigh0tpropiety+";"+sel

	elif mode_0 == "n" or "N":
		sel="/*"
		res="{ X }"
		eigh0tpropiety = " "
		mode_0 = sel+font_weight+ont_w":"+eigh0tpropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		eigh0tpropiety = " "
		mode_0 = sel+font_weight+ont_w":"+eigh0tpropiety+";"+sel
SVS_zero()
###############################################################################################

mode_1 = input("Do you want to add "+font_variant+" to you css file? y/N")
	if mode_1 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { normal / small-caps | inherit / initial / unset }
			""")
		aria1ntpropiety = input("Propiety: ")
		mode_1 = sel+font_variant+nt_v":"+aria1ntpropiety+";"+sel

	elif mode_1 == "n" or "N":
		sel="/*"
		res="{ X }"
		aria1ntpropiety = " "
		mode_1 = sel+font_variant+nt_v":"+aria1ntpropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		aria1ntpropiety = " "
		mode_1 = sel+font_variant+nt_v":"+aria1ntpropiety+";"+sel

SVS_uno()
###############################################################################################

mode_2 = input("Do you want to add "+color+" to you css file? y/N")
	if mode_2 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { Name Color or Color Code with # before }
			""")
		ropi2ety = input("Propiety: ")
		mode_2 = sel+color+ sel+colorp":"+ropi2ety+";"+sel

	elif mode_2 == "n" or "N":
		sel="/*"
		res="{ X }"
		ropi2ety = " "
		mode_2 = sel+color+ sel+colorp":"+ropi2ety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		ropi2ety = " "
		mode_2 = sel+color+ sel+colorp":"+ropi2ety+";"+sel

SVS_dos()
###############################################################################################

mode_3 = input("Do you want to add "+font_family+" to you css file? y/N")
	if mode_3 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
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
		amil3ypropiety = input("Propiety: ")
		mode_3 = sel+font_family+ont_f":"+amil3ypropiety+";"+sel

	elif mode_3 == "n" or "N":
		sel="/*"
		res="{ X }"
		amil3ypropiety = " "
		mode_3 = sel+font_family+ont_f":"+amil3ypropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		amil3ypropiety = " "
		mode_3 = sel+font_family+ont_f":"+amil3ypropiety+";"+sel

SVS_tres()
###############################################################################################

mode_4 = input("Do you want to add "+text_decoration+" to you css file? y/N")
	if mode_4 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { line-through overline underline | Dashed / Dotted / Double / None / Solid / Wavy }
			""")
		ecor4ationpropiety = input("Propiety: ")
		mode_4 = sel+text_decoration+d":"+ecor4ationpropiety+";"+sel

	elif mode_4 == "n" or "N":
		sel="/*"
		res="{ X }"
		ecor4ationpropiety = " "
		mode_4 = sel+text_decoration+d":"+ecor4ationpropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		ecor4ationpropiety = " "
		mode_4 = sel+text_decoration+d":"+ecor4ationpropiety+";"+sel

SVS_cuatro()
###############################################################################################

mode_5 = input("Do you want to add "+letter_spacing+" to you css file? y/N")
	if mode_5 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { normal / 5 px / 5 cm / 5 mm / 5 rem }
			""")
		_spa5cingpropiety = input("Propiety: ")
		mode_5 = sel+letter_spacing+er":"+_spa5cingpropiety+";"+sel

	elif mode_5 == "n" or "N":
		sel="/*"
		res="{ X }"
		_spa5cingpropiety = " "
		mode_5 = sel+letter_spacing+er":"+_spa5cingpropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		_spa5cingpropiety = " "
		mode_5 = sel+letter_spacing+er":"+_spa5cingpropiety+";"+sel

SVS_cinco()
###############################################################################################

mode_6 = input("Do you want to add "+font_size+" to you css file? y/N")
	if mode_6 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { xx-large / x-large / larger / large / medium / small / smaller / x-small / xx-small }
			""")
		izep6ropiety = input("Propiety: ")
		mode_6 = sel+font_size++font_s":"+izep6ropiety+";"+sel

	elif mode_6 == "n" or "N":
		sel="/*"
		res="{ X }"
		izep6ropiety = " "
		mode_6 = sel+font_size++font_s":"+izep6ropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		izep6ropiety = " "
		mode_6 = sel+font_size++font_s":"+izep6ropiety+";"+sel

SVS_seis()
###############################################################################################

mode_7 = input("Do you want to add "+text_transofrom+" to you css file? y/N")
	if mode_7 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { Capitalize / Lowercase / Uppercase | None }
				""")
		rans7ofrompropiety = input("Propiety: ")
		mode_7 = sel+text_transofrom+t":"+rans7ofrompropiety+";"+sel

	elif mode_7 == "n" or "N":
		sel="/*"
		res="{ X }"
		rans7ofrompropiety = " "
		mode_7 = sel+text_transofrom+t":"+rans7ofrompropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		rans7ofrompropiety = " "
		mode_7 = sel+text_transofrom+t":"+rans7ofrompropiety+";"+sel

SVS_siete()
###############################################################################################

mode_8 = input("Do you want to add "+background_color+" to you css file? y/N")
	if mode_8 == "y" or "Y":
		sel=" "	
		res="{ OK }"
		os.system('cls')
		print("""
 { Name Color or Color Code with # before }
			""")
		ound8_colorpropiety = input("Propiety: ")
		mode_8 = sel+background_color+":"+ound8_colorpropiety+";"+sel

	elif mode_8 == "n" or "N":
		sel="/*"
		res="{ X }"
		ound8_colorpropiety = " "
		mode_8 = sel+background_color+":"+ound8_colorpropiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		mode_8 = sel+background_color+se

SVS_ocho()
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
		mode_9 = sel+font_style+font_s":"+tyle9propiety+";"+sel

	elif mode_9 == "n" or "N":
		sel="/*"
		res="{ X }"
		tyle9propiety = " "
		mode_9 = sel+font_style+font_s":"+tyle9propiety+";"+sel

	else:
		sel="/*"
		res="{ X }"
		tyle9propiety = " "
		mode_9 = sel+font_style+font_s":"+tyle9propiety+";"+sel
SVS_nueve()
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
clase=input"Clase: "
add_contentcss="."+clase+"{"+"""
"""+mode_1+"""
"""+mode_2+"""
"""+mode_3+"""
"""+mode_4+"""
"""+mode_5+"""
"""+mode_6+"""
"""+mode_7+"""
"""+mode_8+"""
"""+mode_9+"""
}"""