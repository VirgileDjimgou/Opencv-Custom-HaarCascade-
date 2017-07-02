import preprocIMCOPIA
import callSNNS
import os

os.system("sudo ln -s /dev/video0 /dev/video")
os.system("vgrabbj -l 1 > imagen2.jpg") # Arranca el demonio de captura

for x in range(40):
    archivo = open("imagen2.jpg")
    lectura = ""
    temp = archivo.readline()
    while temp != "":        
        lectura += temp
        temp = archivo.readline()        
    archivo.close()
    apreproc = open("entrada.jpg","w")
    apreproc.write(lectura)
    apreproc.close()
    try:
        cambios = preprocIMCOPIA.preprocesar("./entrada.jpg",3,230)
        toro = callSNNS.propagar(cambios, 0.8)
        print "La carta es: ", toro
        esperar = raw_input("...")
    except:
        print "captura no valida"
        esperar = raw_input("...")
 
   

os.system("killall vgrabbj")
