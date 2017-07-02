import preprocIMCOPIA
import callSNNS


cambios = preprocIMCOPIA.preprocesar("./imagen3.jpg",3,230)
print "La carta es: ",callSNNS.propagar(cambios, 0.6)

