
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

## Recomendaciones para completar la documentación:
1. Incluir diagramas UML en `/docs/diseño.md` (puedes generarlos con PlantUML)
2. Añadir una sección de "Ejemplos de Uso" con capturas de pantalla
3. Incluir un "Manual de Instalación" si es necesario
4. Agregar una sección de "Posibles Mejoras" para futuras versiones
5. Documentar los límites conocidos y precisión de los cálculos
