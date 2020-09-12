#Crea Usuarios Linux
import os
os.system('clear')
usr = input("Nombre de usuario: ")
os.system('useradd'+usr)
print("Ahora tienes que añadir las contraseñas del usuario "+usr+" :")
os.system('passwd'+usr)