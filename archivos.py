from random import choice 
import string
def crear():
	arch = open("contraseñas.txt", "w")
	arch.close

def escribir(lon,vec):
	arch = open("contraseñas.txt", "r")
	listado = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	for i in range(vec):
		contraseña = ""
		contraseña = contraseña.join([choice(listado) for i in range(lon)])
		arch.write(contraseña+"\n")
	arch.close()

def leer():
	arch = open("contraseñas.txt","r")
	linea = arch.readline()
	while linea != "":
		print (linea)
		linea = linea.readline()
	arch.close()