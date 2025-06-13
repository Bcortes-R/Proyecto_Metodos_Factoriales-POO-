''' controlador que conecta las operaciones seleccionadas con las funciones matematicas implemetadas en el modelo'''
#Importamos las funciones previamente creadas en nuestra carpeta model
from model import metFactoriales_model

def calcular (operacion, x):
    # Recibimos el nombre de la operacion y el valor de x y llamamos la funcion correspondiente
    ''' Llamamos a la funcion de acuerdo al nombre asignado en el modelo '''
    #Potencia
    if operacion == 'potencia':
        return metFactoriales_model.potencia(x)
    
    #Factorial
    elif operacion == 'factorial':
        return metFactoriales_model.factorial(x)
    
    #Exponencial
    elif operacion == 'exponencial':
        return metFactoriales_model.exponencial(x)
    
    #Seno
    elif operacion == 'seno':
        return metFactoriales_model.seno(x)
    
    #Coseno
    elif operacion == 'coseno':
        return metFactoriales_model.coseno(x)
    
    #Arcseno
    elif operacion == 'arcsen':
        return metFactoriales_model.arcsen(x)
    
    #Arccoseno
    elif operacion == 'arccos':
        return metFactoriales_model.arccos(x)
    
    #Senohiperbolico
    elif operacion == 'senohiperbolico':
        return metFactoriales_model.senohiperbolico(x)
    
    #Cosenohiperbolico
    elif operacion == 'cosenohiperbolico':
        return metFactoriales_model.cosenohiperbolico(x)
    
    else:
        # Si no se encuentra la operacion, devolvemos un mensaje de error
        return "Operacion no encontrada "  
    
    #Fin del llamado de las funciones matematicas