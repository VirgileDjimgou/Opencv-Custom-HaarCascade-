#JUAN PABLO GARCIA
#MAURICIO TORO
#MODULO PREPROCESAMIENTO - Proyecto IA

import ImageFilter, Image, ImageEnhance, math, os, time

def cambios(narchivo,colorbase,tolerancias):
        "Preprocesa una imagen usando el algoritmo de Diego Linares"

        # Tecnicas de procesamiento basadas en filtros de Sobel
        toro = Image.open(narchivo)
        toro = toro.convert("L")
        toro = toro.filter(ImageFilter.SMOOTH)
        toro = toro.filter(ImageFilter.SMOOTH)

        #toro = toro.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #toro = toro.filter(ImageFilter.FIND_EDGES)
        #toro = ImageChops.invert(toro)
        #toro = toro.filter(ImageFilter.SMOOTH)
        #toro = toro.filter(ImageFilter.SMOOTH)
        #toro = toro.filter(ImageFilter.SHARPEN)        
        #toro = toro.filter(ImageFilter.CONTOUR)
        #toro = toro.filter(ImageFilter.SHARPEN)
        #toro = toro.filter(ImageFilter.MedianFilter)        
        #enh = ImageEnhance.Contrast(toro)
        #toro = enh.enhance(2.8)
        toro = toro.filter(ImageFilter.CONTOUR)
        #toro = toro.filter(ImageFilter.CONTOUR)        
        toro = toro.rotate(90)
        listapixels = []
        ancho,alto = toro.size
        tam = min(ancho,alto)
        toro = toro.resize((tam,tam))
        toro = toro.crop((2,2,tam-2,tam-2))
        tam = tam - 4
        intervalos = tam / 9
        torito = toro.convert("RGB")
        vector = [0]*20
        cambiosestado = [0]*20

        for y in range(9): # Lineas horizontales
                puntos = 0
                cambios = 0
                estado = 0
                for x in range(tam):
                        pixel = toro.getpixel((x,y*intervalos))                        
                        if max(pixel-colorbase,0) < tolerancias and pixel != 0:
                                listapixels += [pixel]
                                puntos += 1                                
                                torito.putpixel((x,y*intervalos),(255,0,0))
                                if estado == 0: # si cambia de blanco a azul
                                        cambios += 1
                                estado = 1
                        else:
                                estado = 0
                vector[y] = puntos
                cambiosestado[y] = cambios

        for x in range(8,17): # Lineas Verticales
                puntos = 0
                cambios = 0
                estado = 0
                for y in range(tam):                
                        pixel = toro.getpixel(( (x-8)*intervalos,y ))
                        if max(pixel-colorbase,0) < tolerancias and pixel != 0:
                                listapixels += [pixel]
                                puntos += 1
                                torito.putpixel(((x-8)*intervalos,y),(200,200,0))
                                if estado == 0: # si cambia de blanco a azul
                                        cambios += 1
                                estado = 1
                        else:
                                estado = 0
                vector[x] = puntos
                cambiosestado[x] = cambios    


        puntos = 0
        cambios = 0
        estado = 0
        for x in range(tam): # Linea diagonal 1
                pixel = toro.getpixel((x,tam-x-1))        
                if max(pixel-colorbase,0) < tolerancias and pixel != 0:
                                listapixels += [pixel]
                                puntos += 1
                                torito.putpixel((x,tam-x-1),(0,200,200))                                
                                if estado == 0: # si cambia de blanco a azul
                                        cambios += 1
                                estado = 1
                else:
                                estado = 0
        vector[18] = puntos
        cambiosestado[18] = cambios    


        puntos = 0
        cambios = 0
        estado = 0
        for x in range(tam): # Linea diagonal 2
                pixel = toro.getpixel((x,x))        
                if max(pixel-colorbase,0) < tolerancias and pixel != 0:
                                listapixels += [pixel]
                                puntos += 1
                                torito.putpixel((x,x),(0,255,0))
                                if estado == 0: # si cambia de blanco a negro
                                        cambios += 1
                                estado = 1
                else:
                                estado = 0
        vector[19] = puntos
        cambiosestado[19] = cambios

        # quitar esto        
        #toro.show()
        torito.save("torito.jpg")
        return cambiosestado

def que_color_es(ruta,salida):
    return 0

def que_color_es2(ruta,salida):
    "Utilizando el algoritmo de Toro, encuentra el color"
    toro = Image.open(ruta)
    toro.convert("RGB")
    # Muestas de negro
    a = 131,104,97
    b = 75,56,50
    c = 109,90,83
    d = 91,67,63
    e = 77,57,50
    rojos = [a,b,c,d,e]
    promedios = [0,0,0]
    desviaciones = [0,0,0]
    
    #muestras de negro
    a1 = 71,83,81
    b1 = 28,32,31
    c1 = 22,33,37
    d1 = 36,46,40
    e1 = 27,31,34
    negros = [a1,b1,c1,d1,e1]
    promediosn = [0,0,0]
    desviacionesn = [0,0,0]    

    # Calculo los promedios y desviaciones de las muestras de rojo
    for x in range(3):
        rojosi = map(lambda y: y[x], rojos)    
        promedio = sum(rojosi)/len(rojosi)
        desviacion = math.sqrt(sum(map(lambda x: pow((x - promedio),2),rojosi))/(len(rojosi)-1))
        promedios[x], desviaciones[x] = promedio,desviacion

    #print "rojo",promedios,desviaciones

    # Calculo los promedios y desviaciones de las muestras de negro
    for x in range(3):
        negroi = map(lambda y: y[x], negros)    
        promedio = sum(negroi)/len(negroi)
        desviacion = math.sqrt(sum(map(lambda x: pow((x - promedio),2),negroi))/(len(rojosi)-1))
        promediosn[x],desviacionesn[x] = promedio,desviacion

    #print "negro",promediosn,desviacionesn    

                     
    R,G,B = 0,1,2
    ancho,alto = toro.size
    puntosrojos,puntosnegros = 0,0
    for y in range(1,alto,2):
        for x in range(1,ancho,2):
            pixel = toro.getpixel((x,y))            
            if abs(pixel[R]-promedios[R]) >= abs(pixel[R]-promediosn[R]):            
                puntosnegros += 1
                #toro.putpixel((x,y),(0,255,0))
            elif max(pixel[R] - promedios[R],0) < desviaciones[R] and max(pixel[G] - promedios[G],0) < desviaciones[G] and max(pixel[B] - promedios[B],0) < desviaciones[B]:
                puntosrojos += 1
                toro.putpixel((x,y),(0,255,0))                

    #print ruta
    porcentajerojo = float(puntosrojos)/float((alto*ancho))
    #print "rojo",porcentajerojo
    #print "negro",float(puntosnegros)/float((alto*ancho))
    
    #toro.save("/home/mauriciotoro/Desktop/"+salida)
    #toro.show()
    if porcentajerojo > 0.08:
        #print "es rojo"
        return 0
    else:
        #print "es negro"
        return 10

def preprocesar(x,color,tolerancia):
        "Hace un procesamiento de la imagen devuelve un vector de 21"  
    	cambiesitos = cambios(x,color,tolerancia)
    	cambiesitos += [que_color_es(x,"torito.jpg")]
        return cambiesitos

def generar_punto_pat(ruta,colorbase,tolerancias):
        "Genera los archivos .pat de validacion y entrenamiento dada una carpeta"
        def pasar_a_binario(numero):
            "Pasar numero binario y lo entrega con una cadena de 6 digitos"
            cociente,residuo = numero/2, numero%2
            resp = [residuo]
            while cociente > 1:
                cociente,residuo = cociente/2, cociente%2
                resp += [residuo]
            resp += [cociente]
            tam = len(resp)
            for x in range(6-tam):
                resp += [0]
            resp.reverse()
            respcadena = ""
            for x in resp:
                respcadena += str(x)+" "
            return respcadena

        def generar_una(nombre):
            "Genera un archivo .pat... los basicos son entrenamiento y validacion, pero puede ser otro"
            cartas = os.listdir(ruta+"/"+nombre+"/")
            cartasdict = dict()
            for x in range(len(cartas)):
                cartasdict[cartas[x]] = x
            print cartasdict
            
            arc = open(nombre[:8]+".pat","w")
            i = 0
            arc.write("SNNS pattern definition file V3.2\ngenerated at Mon Feb  26 15:43:27 2006\n\n\nNo. of patterns : 1000\nNo. of input units : 21\nNo. of output units : 6\n\n")
            for carta in cartas:                                           
                    imagenes = os.listdir(ruta+nombre+"/"+carta)                    
                    for x in filter(lambda x: x.split(".")[1] == "jpg" and x != "*.*",imagenes):                        
                            arc.write("# Input pattern %d:\n"%i)                
                            cambiosestado = preprocesar(ruta+nombre+"/"+carta+"/"+x,colorbase,tolerancias)
                            for y in cambiosestado:
                               arc.write("%d "%y)
                            arc.write("\n# Output pattern %d:\n"%i)
                            arc.write(pasar_a_binario(cartasdict[carta])+"\n")                        
                            i += 1;

            arc.close()

        # Concurrentemente entrena y valida    
        pid = os.fork()

        if pid != 0:
            generar_una("entrenamiento")
        else:
            generar_una("validacion")       


def generar_punto_pat_con_nuestras_fotos():
        "Este genera para nuestras imagenes los .pat con el algoritmo de Toro"
        generar_punto_pat("./",3,230)

#ini = time.time()
#generar_punto_pat_con_nuestras_fotos()
#fin = time.time()

#print "tiempito",fin-ini
        
