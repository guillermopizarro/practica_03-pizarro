# Feature Specification: Conversor de Temperatura

**Feature Branch**: `001-temp-converter`

**Created**: 2026-09-28

**Status**: Draft

**Input**: User description: "Crear un conversor de temperatura entre Celsius, Fahrenheit y Kelvin. Los requisitos del proyecto son: # Especificación manual Conversor de temperatura ## Objetivo Convertir una temperatura entre Celsius, Fahrenheit y Kelvin para consultar su equivalencia en otra escala. ## Criterios de aceptación - Permite ingresar una temperatura y seleccionar las unidades de origen y destino entre Celsius (C), Fahrenheit (F) y Kelvin (K). - Convierte entre las tres escalas usando C = (F - 32) * 5/9, F = C * 9/5 + 32, K = C + 273.15 y C = K - 273.15; para F <-> K combina esas fórmulas sin redondeos intermedios. Referencias verificables: 0 C -> 32.00 F; 32 F -> 0.00 C; 0 C -> 273.15 K; 273.15 K -> 0.00 C; 32 F -> 273.15 K; 273.15 K -> 32.00 F. - Muestra cada resultado válido con exactamente dos decimales y la unidad de destino; por ejemplo, 100 C -> 212.00 F. - Rechaza entradas inferiores al cero absoluto según la unidad de origen: C < -273.15, F < -459.67 o K < 0. Muestra 'Temperatura inferior al cero absoluto' y no presenta un resultado de conversión. - Después de una conversión o un error, permite realizar otra conversión sin reiniciar el programa y sin conservar un resultado anterior como si correspondiera a la entrada actual. ## Casos borde - Entrada vacía o formada únicamente por espacios -> mostrar 'Ingrese una temperatura' y no convertir. - Texto no numérico, como abc -> mostrar 'Ingrese un número válido', sin una excepción sin controlar y sin presentar un resultado. - Límite y negativos válidos -> aceptar exactamente -273.15 C, -459.67 F y 0 K; -273.15 C -> 0.00 K. Aceptar también -40 C -> -40.00 F. - Misma unidad de origen y destino -> conservar el valor si es válido y aplicar el formato de dos decimales; por ejemplo, 25 C -> 25.00 C. Mantener la validación del cero absoluto."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Conversión de temperaturas entre diferentes escalas (Priority: P1)

Como usuario que necesita conocer la equivalencia de una temperatura, quiero ingresar un valor numérico y elegir las escalas de origen y destino (Celsius, Fahrenheit, Kelvin) para obtener el valor convertido con alta precisión y con formato a dos decimales junto con la unidad de destino.

**Why this priority**: Es la funcionalidad esencial del sistema. Sin la capacidad de calcular y mostrar conversiones directas e indirectas entre las escalas especificadas, el sistema carece de utilidad operativa.

**Independent Test**: Puede probarse de manera aislada ingresando temperaturas conocidas (por ejemplo, puntos de congelación o ebullición del agua) entre pares de unidades distintas y verificando que el resultado coincida exactamente con las fórmulas físicas estándar redondeado a dos decimales.

**Acceptance Scenarios**:

1. **Given** una temperatura de 0 en escala Celsius (C), **When** el usuario solicita convertir a Fahrenheit (F), **Then** el sistema muestra "32.00 F".
2. **Given** una temperatura de 32 en escala Fahrenheit (F), **When** el usuario solicita convertir a Celsius (C), **Then** el sistema muestra "0.00 C".
3. **Given** una temperatura de 0 en escala Celsius (C), **When** el usuario solicita convertir a Kelvin (K), **Then** el sistema muestra "273.15 K".
4. **Given** una temperatura de 273.15 en escala Kelvin (K), **When** el usuario solicita convertir a Celsius (C), **Then** el sistema muestra "0.00 C".
5. **Given** una temperatura de 32 en escala Fahrenheit (F), **When** el usuario solicita convertir a Kelvin (K), **Then** el sistema combina las transformaciones sin redondeos intermedios y muestra "273.15 K".
6. **Given** una temperatura de 273.15 en escala Kelvin (K), **When** el usuario solicita convertir a Fahrenheit (F), **Then** el sistema combina las transformaciones sin redondeos intermedios y muestra "32.00 F".
7. **Given** una temperatura de 100 en escala Celsius (C), **When** el usuario solicita convertir a Fahrenheit (F), **Then** el sistema muestra "212.00 F".
8. **Given** una temperatura de -40 en escala Celsius (C), **When** el usuario solicita convertir a Fahrenheit (F), **Then** el sistema muestra "-40.00 F".

---

### User Story 2 - Conversión con misma unidad de origen y destino (Priority: P1)

Como usuario, quiero poder seleccionar la misma unidad como escala de origen y destino para verificar o normalizar una temperatura válida, obteniendo el mismo valor con el formato estándar de dos decimales.

**Why this priority**: Garantiza consistencia en el comportamiento del conversor ante selecciones homogéneas de unidades, evitando errores lógicos o inconsistencias de formato.

**Independent Test**: Puede probarse de forma aislada seleccionando la misma unidad para origen y destino con un valor válido (por ejemplo, 25 C a C) y comprobando que el resultado mantenga el valor con formato a dos decimales ("25.00 C").

**Acceptance Scenarios**:

1. **Given** una temperatura válida de 25 en escala Celsius (C), **When** el usuario selecciona Celsius (C) como unidad de destino, **Then** el sistema conserva el valor y presenta "25.00 C".
2. **Given** una temperatura de -273.15 en escala Celsius (C), **When** el usuario selecciona Celsius (C) como unidad de destino, **Then** el sistema presenta "-273.15 C".

---

### User Story 3 - Validación de límites físicos y cero absoluto (Priority: P1)

Como usuario del conversor, quiero que el sistema rechace cualquier valor de temperatura que esté por debajo del cero absoluto según la escala de origen seleccionada, mostrando un mensaje de error claro y evitando la presentación de cálculos inválidos.

**Why this priority**: Las temperaturas inferiores al cero absoluto son físicamente imposibles en estas escalas. Prevenir cálculos espurios es crucial para la integridad de los datos y la confiabilidad del sistema.

**Independent Test**: Puede probarse de forma independiente suministrando valores inmediatamente inferiores a los límites del cero absoluto para cada una de las tres escalas (-273.16 C, -459.68 F, -0.01 K) y verificando el rechazo y el mensaje exacto, así como suministrando los valores límite exactos (-273.15 C, -459.67 F, 0 K) y verificando su aceptación.

**Acceptance Scenarios**:

1. **Given** una temperatura menor a -273.15 en Celsius (ej. -273.16 C), **When** el usuario intenta la conversión, **Then** el sistema rechaza la entrada, muestra "Temperatura inferior al cero absoluto" y no muestra ningún resultado de conversión.
2. **Given** una temperatura menor a -459.67 en Fahrenheit (ej. -459.68 F), **When** el usuario intenta la conversión, **Then** el sistema rechaza la entrada, muestra "Temperatura inferior al cero absoluto" y no muestra ningún resultado de conversión.
3. **Given** una temperatura menor a 0 en Kelvin (ej. -1 K), **When** el usuario intenta la conversión, **Then** el sistema rechaza la entrada, muestra "Temperatura inferior al cero absoluto" y no muestra ningún resultado de conversión.
4. **Given** la temperatura límite exacta de -273.15 en Celsius (C), **When** el usuario solicita convertir a Kelvin (K), **Then** el sistema acepta la temperatura y muestra "0.00 K".
5. **Given** la temperatura límite exacta de -459.67 en Fahrenheit (F), **When** el usuario solicita convertir a Celsius (C), **Then** el sistema acepta la temperatura y muestra "-273.15 C".
6. **Given** la temperatura límite exacta de 0 en Kelvin (K), **When** el usuario solicita convertir a Celsius (C), **Then** el sistema acepta la temperatura y muestra "-273.15 C".
7. **Given** una temperatura menor al cero absoluto con misma unidad de origen y destino (ej. -300 C a C), **When** el usuario intenta la conversión, **Then** el sistema rechaza la entrada, muestra "Temperatura inferior al cero absoluto" y no muestra resultado.

---

### User Story 4 - Validación y manejo de datos de entrada no válidos (Priority: P2)

Como usuario, quiero recibir indicaciones claras cuando el valor ingresado esté vacío o no sea un número válido, sin que la aplicación falle inesperadamente ni muestre resultados incorrectos.

**Why this priority**: Evita bloqueos y fallos del sistema ante entradas erróneas o inadvertidas del usuario, garantizando robustez y usabilidad.

**Independent Test**: Puede probarse introduciendo cadenas vacías, espacios en blanco, o caracteres alfanuméricos y símbolos, verificando que se muestren los mensajes de retroalimentación esperados sin que ocurra ninguna excepción no controlada.

**Acceptance Scenarios**:

1. **Given** una entrada vacía o que contiene únicamente caracteres de espacio en blanco, **When** el usuario intenta convertir, **Then** el sistema muestra "Ingrese una temperatura" y no realiza conversión ni muestra resultado.
2. **Given** una entrada de texto no numérico (por ejemplo, "abc" o "12.a"), **When** el usuario intenta convertir, **Then** el sistema muestra "Ingrese un número válido", sin fallos no controlados y sin presentar ningún resultado.

---

### User Story 5 - Conversiones sucesivas independientes sin persistencia de estados previos (Priority: P2)

Como usuario, quiero realizar múltiples conversiones consecutivas, tanto exitosas como después de un error, sin necesidad de reiniciar la aplicación y con la seguridad de que los resultados anteriores no se reutilizan ni interfieren con la entrada actual.

**Why this priority**: Permite un flujo de trabajo ágil y confiable cuando se consultan múltiples valores en una misma sesión.

**Independent Test**: Puede probarse ejecutando una conversión válida (ej. 100 C -> 212.00 F), seguida inmediatamente por una entrada inválida (ej. "abc"), comprobando que el resultado anterior desaparezca y se muestre solo el error correspondiente; luego ejecutando otra conversión válida y verificando que el nuevo cálculo corresponda únicamente a los nuevos datos.

**Acceptance Scenarios**:

1. **Given** que se realizó previamente una conversión exitosa que mostró un resultado, **When** el usuario introduce una entrada con error (ej. vacía o menor al cero absoluto), **Then** el sistema no conserva ni muestra el resultado anterior y presenta únicamente el mensaje de error correspondiente.
2. **Given** que ocurrió un error en una operación previa, **When** el usuario ingresa nuevos datos válidos y solicita la conversión, **Then** el sistema procesa la nueva solicitud y muestra el resultado correcto correspondiente a la nueva entrada sin necesidad de reiniciar la aplicación.

---

### Edge Cases

- **Valores límite del cero absoluto**:
  - Exactamente -273.15 en Celsius debe ser aceptado y resultar en 0.00 K y -459.67 F.
  - Exactamente -459.67 en Fahrenheit debe ser aceptado y resultar en 0.00 K y -273.15 C.
  - Exactamente 0 en Kelvin debe ser aceptado y resultar en -273.15 C y -459.67 F.
  - Inmediatamente por debajo (-273.150001 C, -459.670001 F, -0.000001 K) debe rechazarse con "Temperatura inferior al cero absoluto".
- **Punto de cruce Celsius-Fahrenheit**:
  - -40 C debe ser convertido exactamente a -40.00 F, y -40 F a -40.00 C.
- **Entradas con espacios adicionales**:
  - Entradas compuestas únicamente por espacios o tabulaciones deben tratarse como entrada vacía mostrando "Ingrese una temperatura".
  - Entradas numéricas válidas con espacios iniciales o finales (ej. "  25  ") deben ser aceptadas y procesadas correctamente como el valor numérico 25.
- **Precisión en conversiones compuestas**:
  - La conversión directa entre Fahrenheit y Kelvin debe mantener precisión en cálculos intermedios (sin truncar ni redondear prematuramente a dos decimales antes de llegar a la escala de destino), garantizando que 32 F equivalga exactamente a 273.15 K y 273.15 K equivalga a 32.00 F.
- **Identidad de escalas**:
  - Convertir de una escala a sí misma (C -> C, F -> F, K -> K) debe conservar el valor exacto formateado con dos decimales (ej. 25 C -> 25.00 C), validando que no sea inferior al cero absoluto.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema DEBE permitir al usuario ingresar un valor de temperatura numérico.
- **FR-002**: El sistema DEBE permitir al usuario seleccionar una unidad de origen entre Celsius (C), Fahrenheit (F) y Kelvin (K).
- **FR-003**: El sistema DEBE permitir al usuario seleccionar una unidad de destino entre Celsius (C), Fahrenheit (F) y Kelvin (K).
- **FR-004**: El sistema DEBE validar si la entrada está vacía o formada únicamente por espacios en blanco, mostrando en dicho caso el mensaje "Ingrese una temperatura" sin realizar conversión.
- **FR-005**: El sistema DEBE validar si la entrada contiene caracteres no numéricos inválidos, mostrando en dicho caso el mensaje "Ingrese un número válido" sin presentar un resultado ni generar excepciones no controladas.
- **FR-006**: El sistema DEBE validar que la temperatura ingresada no sea inferior al cero absoluto de acuerdo con la escala de origen:
  - Para Celsius: no permitir valores menores a -273.15.
  - Para Fahrenheit: no permitir valores menores a -459.67.
  - Para Kelvin: no permitir valores menores a 0.
- **FR-007**: Cuando la temperatura sea inferior al cero absoluto, el sistema DEBE mostrar el mensaje "Temperatura inferior al cero absoluto" y no DEBE presentar ningún resultado de conversión.
- **FR-008**: El sistema DEBE aceptar como válidos los valores exactamente iguales al cero absoluto (-273.15 C, -459.67 F y 0 K).
- **FR-009**: El sistema DEBE realizar conversiones de temperatura utilizando las fórmulas matemáticas estándar:
  - De Fahrenheit a Celsius: $C = (F - 32) \times \frac{5}{9}$
  - De Celsius a Fahrenheit: $F = C \times \frac{9}{5} + 32$
  - De Celsius a Kelvin: $K = C + 273.15$
  - De Kelvin a Celsius: $C = K - 273.15$
- **FR-010**: Para conversiones entre Fahrenheit y Kelvin (F $\leftrightarrow$ K), el sistema DEBE combinar las fórmulas correspondientes sin realizar redondeos intermedios en pasos previos al resultado final.
- **FR-011**: Cuando la unidad de origen y la unidad de destino sean idénticas, el sistema DEBE mantener el valor ingresado siempre que cumpla con la validación de cero absoluto.
- **FR-012**: El sistema DEBE presentar cada resultado de conversión exitosa formateado con exactamente dos cifras decimales, acompañado de la unidad de destino (ejemplo: "100 C -> 212.00 F" o "212.00 F").
- **FR-013**: El sistema DEBE permitir realizar sucesivas conversiones sin necesidad de reiniciar el programa.
- **FR-014**: El sistema DEBE asegurar que tras un error o una nueva solicitud de conversión, ningún resultado previo sea presentado como si correspondiera a la entrada actual.

### Key Entities *(include if feature involves data)*

- **Escala de Temperatura (TemperatureScale)**: Representa las unidades de medida soportadas: Celsius (C), Fahrenheit (F) y Kelvin (K). Posee un límite inferior físico (cero absoluto) asociado a su escala.
- **Solicitud de Conversión (ConversionRequest)**: Representa los datos ingresados para una operación: valor de temperatura ingresado, unidad de origen seleccionada y unidad de destino seleccionada.
- **Resultado de Conversión (ConversionResult)**: Representa la salida producida tras procesar una solicitud válida, conteniendo el valor numérico calculado con precisión y formateado a dos decimales junto con la unidad de destino.
- **Mensaje de Validación (ValidationFeedback)**: Representa las condiciones de error o retroalimentación generadas por entradas inválidas ("Ingrese una temperatura", "Ingrese un número válido", "Temperatura inferior al cero absoluto").

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de las conversiones de prueba con referencias estándar verificables (0 C $\rightarrow$ 32.00 F; 32 F $\rightarrow$ 0.00 C; 0 C $\rightarrow$ 273.15 K; 273.15 K $\rightarrow$ 0.00 C; 32 F $\rightarrow$ 273.15 K; 273.15 K $\rightarrow$ 32.00 F; -40 C $\rightarrow$ -40.00 F) coinciden exactamente con los valores esperados.
- **SC-002**: El 100% de los resultados válidos se presentan formateados con exactamente dos decimales y el identificador de la escala de destino.
- **SC-003**: El 100% de los intentos de ingresar temperaturas estrictamente inferiores al cero absoluto son rechazados, mostrando "Temperatura inferior al cero absoluto" sin presentar resultados de conversión.
- **SC-004**: El 100% de los casos con entradas vacías, de solo espacios o de texto no numérico muestran su mensaje de validación correspondiente ("Ingrese una temperatura" o "Ingrese un número válido") sin producir fallos o cierres no controlados.
- **SC-005**: Los usuarios pueden ejecutar múltiples conversiones seguidas de forma continua e independiente, garantizando que el 100% de las conversiones muestren únicamente la información pertinente a la entrada activa.

## Assumptions

- Se asume el uso del punto decimal (.) como separador estándar para valores numéricos con decimales.
- Se asume que las unidades de temperatura se representan y reconocen mediante sus nombres completos o sus símbolos estándar (C / Celsius, F / Fahrenheit, K / Kelvin).
- Se asume que la aplicación puede operar en una interfaz de usuario interactiva (consola, web o gráfica) donde el usuario introduce datos y visualiza resultados de forma inmediata.
- No se requiere almacenamiento persistente a largo plazo (base de datos o historial en disco) de las conversiones realizadas.
