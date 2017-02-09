import sys
import archivos
print ("bienvenido")
print ("su archivo aparecera como -contraseñas.txt-")
archivos.crear()
archivos.escribir(int(sys.argv[1]),int(sys.argv[2]))
archivos.leer()
a = input("")