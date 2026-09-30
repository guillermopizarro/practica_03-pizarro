# Comparación Final: Spec a Mano vs. Spec Kit

Este documento consolida la evaluación comparativa realizada entre el desarrollo guiado por especificación manual (**Bloque 3.A — `clase-sdd`**) y el desarrollo estructurado mediante **Spec Kit** (**Bloque 3.B — `mi-proyecto-speckit`**) para el **Conversor de Temperatura** (Práctica 03).

---

## 1. Tabla de los 3 Casos de Ambos Bloques (Lado a Lado)

A continuación se presentan los resultados obtenidos al evaluar los tres casos representativos en ambas implementaciones:

| Caso | Entrada (Temperatura, Origen, Destino) | Resultado esperado | Resultado Spec a mano (`clase-sdd`) | Resultado Spec Kit (`mi-proyecto-speckit`) | ¿Pasa / Coinciden? |
|---|---|---|---|---|:---:|
| **Caso normal** | `100`, `C`, `F` | `212.00 F` | `212.00 F` (`Resultado: 212.00 F`) | `212.00 F` (`Resultado: 212.00 F`) | ✅ Coinciden |
| **Caso borde de la spec** | `-273.15`, `C`, `K` | `0.00 K` | `0.00 K` (`Resultado: 0.00 K`) | `0.00 K` (`Resultado: 0.00 K`) | ✅ Coinciden |
| **Caso no contemplado** | `100`, `c`, `f` *(unidades en minúsculas)* | `212.00 F` | `212.00 F` (`Resultado: 212.00 F`) | `212.00 F` (`Resultado: 212.00 F`) | ✅ Coinciden |

### Detalle de comportamiento observado:
1. **Caso normal (`100 C -> F`):**
   - Ambos sistemas aplican la transformación física estándar $F = 100 \times \frac{9}{5} + 32 = 212.0$, formateando la salida exactamente a dos decimales (`212.00 F`) junto con la unidad de destino.
2. **Caso borde (`-273.15 C -> K`):**
   - Ambos sistemas reconocen el límite físico exacto del cero absoluto como valor válido ($K = -273.15 + 273.15 = 0.0$), normalizando la salida numérica para evitar representaciones anómalas como `-0.00 K`.
3. **Caso no contemplado (`100 c -> f`):**
   - A pesar de que la especificación manual no explicitaba tolerancia a minúsculas o variaciones de entrada, ambas implementaciones normalizan automáticamente los símbolos de escala (`c` $\rightarrow$ `C`, `f` $\rightarrow$ `F`) y devuelven el resultado esperado sin generar excepciones no controladas.

---

## 2. Tabla Comparativa de Aspectos

| Aspecto | Spec a mano | Spec Kit |
|---|---|---|
| **¿Cubrió los mismos casos borde?** | **Sí**, cubrió los casos borde contemplados explícitamente en `spec_manual.md`: validación de entradas vacías o compuestas solo por espacios, entradas no numéricas (`abc`), límites exactos de cero absoluto (-273.15 C, -459.67 F, 0 K), punto de cruce Celsius-Fahrenheit (-40 C $\leftrightarrow$ -40 F) y conversión a la misma unidad. Sin embargo, no contempló formalmente casos de frontera infinitesimal (-273.150001 C) ni saneamiento sistemático de espacios periféricos (*whitespace trimming*), dejándolos a la heurística del modelo. | **Sí, y con mayor rigor y exhaustividad**. Cubrió la totalidad de los casos de la spec manual y profundizó en escenarios adicionales: rechazo estricto de valores inmediatamente inferiores al cero absoluto (ej. `-273.150001 C`), saneamiento de entradas con espacios iniciales o finales (ej. `"  25  "` $\rightarrow$ `25.00`), validación bidireccional en conversiones compuestas ($F \leftrightarrow K$) sin pérdida de precisión intermedia, y reinicio estricto del estado de la interfaz tras cualquier error. |
| **¿Qué generó Spec Kit que tú no habías escrito?** | Una especificación concisa y minimalista de 18 líneas estructurada en Objetivo, Criterios de aceptación (5 ítems) y Casos borde (4 puntos). No se generaron contratos formales, ni modelo de entidades, ni desglose de tareas previas a la codificación. | Generó un ecosistema completo de artefactos de ingeniería de software:<br>1. **Especificación formal (`spec.md`):** Historias de usuario priorizadas (P1/P2) con criterios de aceptación en formato Gherkin (*Given-When-Then*), requisitos funcionales formalmente codificados (FR-001 a FR-014), entidades de dominio (`TemperatureScale`, `ConversionRequest`, etc.) y criterios de éxito medibles (SC-001 a SC-005).<br>2. **Plan y Contratos (`plan.md`, `contracts/`):** Contratos de interfaz CLI y GUI (`cli-interface.md`, `gui-interface.md`), API del convertidor (`converter-api.md`), modelo de datos y reglas constitucionales del proyecto.<br>3. **Desglose de tareas (`tasks.md`):** Plan de trabajo secuencial y paralelizable con dependencias y criterios de verificación unitaria.<br>4. **Arquitectura modular y tests:** Separación limpia de responsabilidades en módulos independientes (`core.py`, `cli.py`, `gui.py`) y una suite de 24 pruebas automatizadas (cubriendo lógica de cálculo y lógica de UI). |
| **¿Qué se sintió más rápido de arrancar?** | **Spec a mano**. El arranque fue casi instantáneo. En menos de 15 minutos se redactó el archivo Markdown inicial y el agente comenzó a escribir código inmediatamente sin requerir configuraciones previas ni herramientas especializadas. | **Fue más lento y con mayor sobrecarga inicial**. Requirió instalar la herramienta `specify-cli`, inicializar el proyecto (`specify init`), y seguir paso a paso un flujo ceremonial de comandos (`/speckit-specify` $\rightarrow$ `/speckit-plan` $\rightarrow$ `/speckit-tasks` $\rightarrow$ `/speckit-implement`), generando múltiples documentos de soporte antes de producir la primera línea de código ejecutable. |
| **¿Cuál te generó más confianza en el resultado?** | **Menor confianza relativa**. Aunque el resultado final fue funcional y pasó las pruebas manuales, la falta de contratos de interfaz explícitos y la ausencia de un plan técnico formal dejan margen para que el modelo tome decisiones de diseño arbitrarias, aumentando el riesgo de inconsistencias o regresiones al ampliar el proyecto. | **Spec Kit generó una confianza notablemente superior**. Al formalizar los requisitos en contratos, modelar las entidades y desglosar el desarrollo en tareas pequeñas con verificación incremental, se eliminan las ambigüedades y alucinaciones del modelo. El código resultante posee una arquitectura limpia, desacoplamiento entre lógica de negocio y presentación (CLI / GUI Tkinter), y una cobertura de pruebas exhaustiva. |

---

## 3. Frase de Cierre y Siguiente Paso

### Frase de Cierre:
> **"La próxima vez que tenga un proyecto de tamaño pequeño o un script puntual, elegiría spec a mano porque su arranque es instantáneo y suficiente para requerimientos directos; pero para proyectos de tamaño mediano o grande con múltiples módulos e interfaces, elegiría Spec Kit porque sus contratos formales, desglose de tareas y suite de pruebas garantizan una arquitectura sólida, verificable y mantenible."**

### Siguiente Paso (Sesión 5):
El trabajo desarrollado en ambas ramas de `s4/` (`clase-sdd` y `mi-proyecto-speckit`) queda preservado como base funcional verificada. En la siguiente sesión se retomará esta base para incorporar pruebas automatizadas adicionales, análisis estático y una revisión de seguridad básica sobre los componentes implementados.
