
# Análisis del Proyecto

## Requisitos Funcionales
1. Implementar cálculos matemáticos sin usar funciones nativas de Python:
   - Exponencial (e^x)
   - Funciones trigonométricas (seno, coseno)
   - Funciones trigonométricas inversas (arcoseno, arcocoseno)
   - Funciones hiperbólicas (seno hiperbólico, coseno hiperbólico)

2. Desarrollar dos interfaces de usuario:
   - Interfaz de consola
   - Interfaz web

3. Estructurar el proyecto bajo el patrón MVC

## Requisitos No Funcionales
- Código claro con nombres descriptivos
- Documentación adecuada
- Validación de entradas
- Precisión en cálculos matemáticos

## Enfoque de Solución
Se utilizarán series de Taylor para aproximar las funciones matemáticas:
- e^x = Σ(x^n/n!)
- sen(x) = Σ((-1)^n * x^(2n+1)/(2n+1)!)
- cos(x) = Σ((-1)^n * x^(2n)/(2n)!)
- arcsen(x) = Σ((2n)!/(4^n*(n!)^2*(2n+1)))*x^(2n+1)

Para las funciones hiperbólicas:
- senh(x) = (e^x - e^-x)/2
- cosh(x) = (e^x + e^-x)/2

## Limitaciones
- Precisión limitada por el número de términos en las series
- Rangos limitados para funciones inversas (-1 ≤ x ≤ 1)
- Rendimiento en cálculos iterativos
