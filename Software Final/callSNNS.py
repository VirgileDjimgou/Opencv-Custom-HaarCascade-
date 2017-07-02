import os

def filtrar(x,limite):
	"Filtra los datos flotantes pasando a enteros segun el limite dado"
	if x >= limite:
		return 1
	else:
		return 0

def binario_decimal(binario):
	"Pasa de binario a decimal una lista de ceros y unos"
	cont, resp = len(binario)-1,0 
	for x in binario:
		resp += x*pow(2,cont)
		cont -= 1
	return resp

def striptoro(lista,x):
    "quita los elementos x de una secuencia en general"
    resp = ""
    for y in lista:
        if y != x:
            resp += y
    return resp

def propagar(vector,limite):
    "Permite propagar en la red neuronal dado un limite y un vector"
    in1,out1 = os.popen2("wine ./isnns.exe")
    in1.write("load red.net\n")
    #in1.write("prop 1 8 11 15 11 13 12 8 0 1 9 16 12 12 20 0 0 0 11 14 0\n")
    in1.write("prop "+striptoro(str(vector)[1:-1],",")+"\n")
    in1.close()

    x = out1.read()
    out1.close()
    print "los numeritos\n ",map(lambda x: float(x),x.split("ok> ")[2].split(" ")[:-1])    
    respuesta = map(lambda x: filtrar(float(x),limite),x.split("ok> ")[2].split(" ")[:-1])    
    print "la respuestica binaria: ", respuesta
    print "el numerito de la carta: ",binario_decimal(respuesta)
    archivo = open("hash.txt")
    hashito = eval(archivo.read())
    numero = binario_decimal(respuesta)
    if numero > 53:
	    return "no es válida. Que pena"
    else:	    
	    return hashito[binario_decimal(respuesta)]

