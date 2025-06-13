
# Diseño del Sistema

## Diagrama de Arquitectura MVC
[Texto alternativo: Diagrama MVC con tres componentes principales: Modelo (CalculadoraMatematica), Vista (Consola y Web), Controlador (ControladorCalculadora), mostrando las interacciones entre ellos]

## Diseño del Modelo
Clase CalculadoraMatematica:

- Métodos estáticos para cada operación matemática
- Implementación manual usando bucles y operaciones básicas
- Factorial y potencia como métodos auxiliares

## Diseño del Controlador
Clase ControladorCalculadora:

- Mediador entre vista y modelo
- Traduce solicitudes de la vista a operaciones del modelo
- Maneja errores y validaciones

## Diseño de las Vistas

### Consola:
- Menú interactivo
- Entrada/salida simple
- Validación básica

### Web:
- Aplicación Flask minimalista
- Formulario HTML simple
- Muestra resultados en la misma página

## Flujo de Datos
1. Vista recibe entrada del usuario
2. Vista envía solicitud al controlador
3. Controlador invoca método del modelo
4. Modelo realiza cálculo y devuelve resultado
5. Controlador pasa resultado a vista
6. Vista muestra resultado al usuario
