# Implementación del Código

## Estructura del Proyecto

proyecto_matematico/
├── docs/ # Documentación
├── src/
│   ├── modelo/ # Lógica de cálculos
│   ├── vista/ # Interfaces de usuario
│   └── controlador/ # Coordinación
├── main_consola.py # Entrada consola
└── main_web.py # Entrada web

## Algoritmos Clave

### Cálculo de Factorial

```python
@staticmethod
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
```

### Serie de Taylor para e^x

```python
@staticmethod
def exponencial(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        resultado += CalculadoraMatematica.potencia(x, n) / CalculadoraMatematica.factorial(n)
    return resultado
```

### Manejo de Operaciones en el Controlador

```python
def calcular(self, operacion, valor):
    valor = float(valor)
    if operacion == "exponencial":
        return self.calculadora.exponencial(valor)
    # ... otras operaciones
```

## Validaciones Importantes

- Rango para funciones inversas (-1 ≤ x ≤ 1)
- Manejo de valores no numéricos
- Prevención de desbordamiento en factoriales

## Pruebas Realizadas

- Comparación con valores conocidos:
  - e^1 ≈ 2.71828
  - sen(π/2) ≈ 1
  - cos(π) ≈ -1
- Pruebas de borde:
  - x = 0
  - x = 1 para funciones inversas
  - Valores negativos

## Instrucciones de Uso

### Consola:

- Ejecutar `python main_consola.py`
- Seguir menú interactivo

### Web:

- Ejecutar `python main_web.py`
- Abrir navegador en `http://localhost:5000`
- Seleccionar operación e ingresar valor

## Dependencias

- Flask (solo para versión web)
- Python 3.6+

## Ejemplos de Uso

### Consola

```
Seleccione una operación:
1. Exponencial
2. Seno
...
Ingrese la opción: 1
Ingrese el valor de x: 1
Resultado: 2.71828
```

### Web

Formulario en `http://localhost:5000`:

- Seleccione operación (Dropdown)
- Ingrese valor de x (Input)
- Presione "Calcular"
- Resultado mostrado abajo

## Manual de Instalación

### Requisitos

- Python 3.6 o superior
- Flask (`pip install flask`)

### Pasos

1. Clonar o descargar el repositorio
2. crear el entorno virtual **python -m venv .venv**
3. navegar hasta la carpeta .venv y ejecutar Scripts\Acti
4. Ejecutar **pip install -r requirements.txt**
5. Ejecutar `main_consola.py` para versión consola
6. Ejecutar `main_web.py` para versión web
7. Navegar a `http://localhost:5000` para usar interfaz web

## Límites Conocidos y Precisión

- Las funciones inversas solo admiten entradas en el rango [-1, 1]
- La precisión depende del número de términos en las series de Taylor (por defecto: 20)
- Para valores grandes, el cálculo de factorial puede causar desbordamientos
- Los resultados son aproximados, adecuados para propósitos educativos o demostrativos
