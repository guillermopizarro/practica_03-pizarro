"""Módulo de conversión de temperatura entre Celsius, Fahrenheit y Kelvin.

Cumple con la especificación de SDD para la práctica 03.
"""

from typing import Optional, Tuple

# Límites del cero absoluto según la escala
ABSOLUTE_ZERO = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}

UNIDADES_VALIDAS = {"C", "F", "K"}

MAPA_UNIDADES = {
    "C": "C",
    "CELSIUS": "C",
    "F": "F",
    "FAHRENHEIT": "F",
    "K": "K",
    "KELVIN": "K",
}


def normalizar_unidad(unidad: Optional[str]) -> Optional[str]:
    """Normaliza el texto de una unidad (acepta C, F, K en mayúsculas o minúsculas).
    
    Retorna la unidad normalizada ('C', 'F', 'K') o None si es inválida.
    """
    if not unidad:
        return None
    limpio = unidad.strip().upper()
    return MAPA_UNIDADES.get(limpio)


def validar_entrada_temperatura(entrada: Optional[str]) -> Tuple[Optional[float], Optional[str]]:
    """Valida la cadena ingresada como temperatura.
    
    Retorna:
        (valor_float, None) si es válido.
        (None, mensaje_error) si es inválido:
            - 'Ingrese una temperatura' si está vacía o solo contiene espacios.
            - 'Ingrese un número válido' si el texto no es numérico.
    """
    if entrada is None or not entrada.strip():
        return None, "Ingrese una temperatura"
    
    texto = entrada.strip()
    try:
        valor = float(texto)
        return valor, None
    except ValueError:
        # Si se ingresó coma como separador decimal, intentamos verificar si es número
        if "," in texto and texto.count(",") == 1:
            try:
                valor = float(texto.replace(",", "."))
                return valor, None
            except ValueError:
                pass
        return None, "Ingrese un número válido"


def validar_cero_absoluto(valor: float, unidad_origen: str) -> Tuple[bool, Optional[str]]:
    """Verifica si la temperatura está por encima o en el cero absoluto.
    
    Retorna (True, None) si es válida.
    Retorna (False, 'Temperatura inferior al cero absoluto') si es inferior.
    """
    limite = ABSOLUTE_ZERO.get(unidad_origen.upper())
    if limite is not None and valor < limite:
        return False, "Temperatura inferior al cero absoluto"
    return True, None


def convertir_temperatura(valor: float, origen: str, destino: str) -> float:
    """Convierte una temperatura entre Celsius (C), Fahrenheit (F) y Kelvin (K).
    
    Fórmulas utilizadas:
        C = (F - 32) * 5/9
        F = C * 9/5 + 32
        K = C + 273.15
        C = K - 273.15
        F -> K: (F - 32) * 5/9 + 273.15 (sin redondeos intermedios)
        K -> F: (K - 273.15) * 9/5 + 32 (sin redondeos intermedios)
    """
    u_orig = origen.upper()
    u_dest = destino.upper()

    if u_orig not in UNIDADES_VALIDAS or u_dest not in UNIDADES_VALIDAS:
        raise ValueError(f"Unidades deben ser C, F o K. Recibido: {origen} -> {destino}")

    if u_orig == u_dest:
        return valor

    # De Celsius a otras
    if u_orig == "C":
        if u_dest == "F":
            return valor * 9.0 / 5.0 + 32.0
        elif u_dest == "K":
            return valor + 273.15

    # De Fahrenheit a otras
    elif u_orig == "F":
        if u_dest == "C":
            return (valor - 32.0) * 5.0 / 9.0
        elif u_dest == "K":
            # Combinación sin redondeos intermedios
            return (valor - 32.0) * 5.0 / 9.0 + 273.15

    # De Kelvin a otras
    elif u_orig == "K":
        if u_dest == "C":
            return valor - 273.15
        elif u_dest == "F":
            # Combinación sin redondeos intermedios
            return (valor - 273.15) * 9.0 / 5.0 + 32.0

    raise ValueError(f"Conversión no soportada: {u_orig} -> {u_dest}")


def formatear_resultado(valor: float, unidad_destino: str) -> str:
    """Formatea el resultado numérico con exactamente dos decimales y la unidad de destino.
    
    Evita '-0.00' normalizándolo a '0.00'.
    """
    u = unidad_destino.upper()
    if abs(valor) < 1e-9:
        valor = 0.0
    return f"{valor:.2f} {u}"


def procesar_conversion(temp_str: str, origen_str: str, destino_str: str) -> Tuple[bool, str]:
    """Ejecuta el flujo completo de validación y conversión.
    
    Retorna:
        (True, resultado_formateado) si la conversión fue exitosa.
        (False, mensaje_error) si ocurrió algún error de validación.
    """
    # 1. Validar entrada de temperatura
    valor, err_temp = validar_entrada_temperatura(temp_str)
    if err_temp:
        return False, err_temp

    # 2. Validar unidades
    u_orig = normalizar_unidad(origen_str)
    if not u_orig:
        return False, "Unidad de origen no válida. Ingrese C, F o K"

    u_dest = normalizar_unidad(destino_str)
    if not u_dest:
        return False, "Unidad de destino no válida. Ingrese C, F o K"

    # 3. Validar cero absoluto
    valido_cero, err_cero = validar_cero_absoluto(valor, u_orig)
    if not valido_cero:
        return False, err_cero

    # 4. Convertir y formatear
    res = convertir_temperatura(valor, u_orig, u_dest)
    return True, formatear_resultado(res, u_dest)
