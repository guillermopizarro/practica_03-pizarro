# Resultados de Pruebas — Bloque 3.A (Spec a mano)

Registro de pruebas manuales y automatizadas realizadas sobre la implementación del conversor de temperatura según la especificación en `spec_manual.md`.

## Tabla de Casos de Prueba

| Tipo de caso | Entrada (Temperatura, Origen, Destino) | Resultado esperado | Resultado obtenido | ¿Pasa? |
|---|---|---|---|:---:|
| **Caso normal** | `100`, `C`, `F` | `212.00 F` | `212.00 F` | ✅ |
| **Caso borde de la spec** | `-273.15`, `C`, `K` | `0.00 K` | `0.00 K` | ✅ |
| **Caso no contemplado** | `100`, `c`, `f` (minúsculas) | `212.00 F` | `212.00 F` | ✅ |

---

## Detalle de cada caso

### 1. Caso normal
- **Descripción:** Conversión típica y esperada del punto de ebullición del agua de Celsius a Fahrenheit.
- **Entrada:**
  - Temperatura: `100`
  - Unidad origen: `C`
  - Unidad destino: `F`
- **Fórmula aplicada:** `F = 100 * 9/5 + 32 = 212.0`
- **Resultado obtenido:** `Resultado: 212.00 F`
- **Observación:** El valor numérico se formatea con exactamente dos decimales y la unidad de destino correspondiente.

### 2. Caso borde de la spec
- **Descripción:** Límite exacto del cero absoluto en la escala Celsius (`-273.15 C`) convertido a Kelvin.
- **Entrada:**
  - Temperatura: `-273.15`
  - Unidad origen: `C`
  - Unidad destino: `K`
- **Fórmula aplicada:** `K = -273.15 + 273.15 = 0.0`
- **Resultado obtenido:** `Resultado: 0.00 K`
- **Observación:** La validación de cero absoluto permite el límite exacto (`>= -273.15`), evitando además el formato `-0.00 K` mediante normalización a `0.00 K`.

### 3. Caso no contemplado en la spec
- **Descripción:** El usuario ingresa las unidades en minúsculas (`c` y `f`), o nombres completos, aspecto no especificado explícitamente en `spec_manual.md`.
- **Entrada:**
  - Temperatura: `100`
  - Unidad origen: `c`
  - Unidad destino: `f`
- **Comportamiento del sistema:** El programa normaliza las unidades a mayúsculas de manera tolerante (`c` -> `C`, `f` -> `F`), ejecuta la conversión correctamente y retorna `212.00 F`. Si se introduce una unidad no existente (ej. `X`), el programa informa de forma controlada `Unidad de origen no válida. Ingrese C, F o K.` sin lanzar excepciones no controladas.

---

## Resumen de Validación de Criterios y Casos Borde Adicionales

- **Entrada vacía o espacios:** Al ingresar espacios en blanco `"   "`, muestra `Ingrese una temperatura` y permite un nuevo intento.
- **Texto no numérico:** Al ingresar `"abc"`, muestra `Ingrese un número válido` sin excepciones y sin mostrar resultado previo.
- **Inferior al cero absoluto:** Al ingresar `-300 C`, muestra `Temperatura inferior al cero absoluto`.
- **Misma escala:** `25 C` a `C` retorna `25.00 C`.
- **Persistencia de estado:** Cada conversión o error reinicia el estado; un error no conserva ni muestra resultados de conversiones previas.
