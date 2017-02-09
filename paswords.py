import sys
import archivos
print ("bienvenido")
print ("su archivo aparecera como -contraseñas.txt-")
archivos.crear()
input("hola")
archivos.escribir(sys.argv[1],sys.argv[2])
archivos.leer()
a = input("")