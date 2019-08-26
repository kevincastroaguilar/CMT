# Ejemplo 1
# Se importa la libreria "os" para poder acceder al sistema
import os

# os.getcwd es una funcion de la libreria "os" capaz de obtener la direccion donde esta ubicado el codigo
# Le asigna esta informacion a la variable "path"
# Luego imprimo en consola un mensaje + la direccion obtenida

path = os.getcwd()
print ("El directorio donde se encuentra el codigo es %s" % path)

#----------------------------------------------------------------------------------------------------------

# Ejemplo 2
# Primero tenemos que hacer un codigo que se adapte a diferentes computadoras o usuarios
# En vez de tener una direccion exacta como: C:\Users\kjcastro\Desktop\CMT\ColectorDeDatos
# Usaremos una funcion de python para obtener el usuario que este ejecutando el codigo en ese momento

# Importamos la libreria getpass y luego usamos su funcion .getuser para obtener el usuario del sistema
import getpass

usuario = getpass.getuser()   

# Al String del directorio le añadimos el usuario que obtuvimos en la variable usuario
directorioParaDatos='C:\\Users\\'+usuario+'\\Desktop\\CMT\\Datos\\'

# Definimos el nombre del folder que vamos a crear
nombreFolder = 'Estante04'
direccionCompleta=directorioParaDatos+nombreFolder

# Revisamos si ya existe el folder dentro de esa direccion, si no, crea el folder con el nombre asignado a la variable "nombreFolder"

if not os.path.exists(direccionCompleta):
    os.makedirs(direccionCompleta)
else : 
    print("Folder ya existe en %s " % directorioParaDatos)

