# Comparativa de Resultados de Pruebas: Spec a Mano vs. Spec Kit

Registro comparativo de ejecución de pruebas entre la implementación basada en la especificación manual (`s4/clase-sdd`) y la implementación generada con **Spec Kit** (`s4/mi-proyecto-speckit`).

## Tabla de Casos de Prueba

| Caso | Resultado spec a mano | Resultado Spec Kit |
|---|---|---|
| Caso normal | `212.00 F` (`Resultado: 212.00 F`) | `212.00 F` (`Resultado: 212.00 F`) |
| Caso borde de tu spec | `0.00 K` (`Resultado: 0.00 K`) | `0.00 K` (`Resultado: 0.00 K`) |
| Caso no contemplado | `212.00 F` (`Resultado: 212.00 F`) | `212.00 F` (`Resultado: 212.00 F`) |

---

## Detalle de Ejecución y Comparación

### 1. Caso normal
- **Descripción:** Conversión del punto de ebullición del agua de Celsius a Fahrenheit.
- **Entrada:** `100` en temperatura, unidad de origen `C`, unidad de destino `F`.
- **Fórmula aplicada:** $F = C \times \frac{9}{5} + 32 = 100 \times 1.8 + 32 = 212.0$
- **Resultado spec a mano:** `Resultado: 212.00 F`
- **Resultado Spec Kit:** `Resultado: 212.00 F`
- **Evaluación:** ✅ Ambos entornos producen el resultado idéntico, formateado estrictamente a dos decimales con la unidad de destino.

### 2. Caso borde de tu spec
- **Descripción:** Límite físico exacto del cero absoluto en la escala Celsius (`-273.15 C`) convertido a Kelvin.
- **Entrada:** `-273.15` en temperatura, unidad de origen `C`, unidad de destino `K`.
- **Fórmula aplicada:** $K = C + 273.15 = -273.15 + 273.15 = 0.0$
- **Resultado spec a mano:** `Resultado: 0.00 K`
- **Resultado Spec Kit:** `Resultado: 0.00 K`
- **Evaluación:** ✅ Ambos aceptan el límite exacto del cero absoluto ($-273.15 \ge -273.15$) y normalizan el valor numérico evitando `-0.00 K`.

### 3. Caso no contemplado
- **Descripción:** El usuario ingresa las unidades en minúsculas (`c` y `f`), aspecto no contemplado en la especificación original.
- **Entrada:** `100` en temperatura, unidad de origen `c`, unidad de destino `f`.
- **Comportamiento esperado:** Normalización insensible a mayúsculas/minúsculas.
- **Resultado spec a mano:** `Resultado: 212.00 F`
- **Resultado Spec Kit:** `Resultado: 212.00 F`
- **Evaluación:** ✅ Ambos sistemas normalizan las unidades a mayúsculas (`c` $\rightarrow$ `C`, `f` $\rightarrow$ `F`), completando la conversión sin excepciones.

---

## Casos Adicionales Validados en Spec Kit

| Escenario Adicional | Entrada | Resultado Esperado | Resultado Spec Kit | Estado |
|---|---|---|---|:---:|
| **Entrada vacía / espacios** | `""` o `"   "` | `"Ingrese una temperatura"` | `"Ingrese una temperatura"` | ✅ PASS |
| **Texto no numérico** | `"abc"` | `"Ingrese un número válido"` | `"Ingrese un número válido"` | ✅ PASS |
| **Bajo cero absoluto** | `-300 C -> F` | `"Temperatura inferior al cero absoluto"` | `"Temperatura inferior al cero absoluto"` | ✅ PASS |
| **Misma escala** | `25 C -> C` | `25.00 C` | `Resultado: 25.00 C` | ✅ PASS |
| **Límite F a C** | `-459.67 F -> C` | `-273.15 C` | `Resultado: -273.15 C` | ✅ PASS |
| **Persistencia de estado** | Error tras cálculo previo | Limpieza del resultado previo | Estado reiniciado correctamente | ✅ PASS |