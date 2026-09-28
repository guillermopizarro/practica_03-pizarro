"""Módulo central con lógica pura de conversión, validación y formateo."""

from typing import Optional, Tuple

ABSOLUTE_ZERO: dict[str, float] = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}

UNIDADES_VALIDAS: set[str] = {"C", "F", "K"}

MAPA_UNIDADES: dict[str, str] = {
    "C": "C",
    "CELSIUS": "C",
    "CELSIUS (C)": "C",
    "F": "F",
    "FAHRENHEIT": "F",
    "FAHRENHEIT (F)": "F",
    "K": "K",
    "KELVIN": "K",
    "KELVIN (K)": "K",
}


def normalizar_unidad(unidad: Optional[str]) -> Optional[str]:
    """Normaliza el texto de una unidad a 'C', 'F' o 'K'. Retorna None si no es válida."""
    if not unidad:
        return None
    limpio = unidad.strip().upper()
    return MAPA_UNIDADES.get(limpio)


def validar_entrada_temperatura(entrada: Optional[str]) -> Tuple[Optional[float], Optional[str]]:
    """Valida la entrada de temperatura según los casos borde especificados."""
    if entrada is None or not entrada.strip():
        return None, "Ingrese una temperatura"

    texto = entrada.strip()
    try:
        valor = float(texto)
        return valor, None
    except ValueError:
        if "," in texto and texto.count(",") == 1:
            try:
                valor = float(texto.replace(",", "."))
                return valor, None
            except ValueError:
                pass
        return None, "Ingrese un número válido"


def validar_cero_absoluto(valor: float, unidad_origen: str) -> Tuple[bool, Optional[str]]:
    """Rechaza entradas inferiores al cero absoluto según la unidad de origen."""
    limite = ABSOLUTE_ZERO.get(unidad_origen.upper())
    if limite is not None and valor < limite:
        return False, "Temperatura inferior al cero absoluto"
    return True, None


def convertir_temperatura(valor: float, origen: str, destino: str) -> float:
    """Convierte la temperatura entre escalas usando fórmulas exactas sin redondeos intermedios."""
    u_orig = origen.upper()
    u_dest = destino.upper()

    if u_orig not in UNIDADES_VALIDAS or u_dest not in UNIDADES_VALIDAS:
        raise ValueError(f"Unidades no válidas: {origen} -> {destino}")

    if u_orig == u_dest:
        return valor

    if u_orig == "C":
        if u_dest == "F":
            return valor * 9.0 / 5.0 + 32.0
        elif u_dest == "K":
            return valor + 273.15

    elif u_orig == "F":
        if u_dest == "C":
            return (valor - 32.0) * 5.0 / 9.0
        elif u_dest == "K":
            return (valor - 32.0) * 5.0 / 9.0 + 273.15

    elif u_orig == "K":
        if u_dest == "C":
            return valor - 273.15
        elif u_dest == "F":
            return (valor - 273.15) * 9.0 / 5.0 + 32.0

    raise ValueError(f"Conversión no soportada: {u_orig} -> {u_dest}")


def formatear_resultado(valor: float, unidad_destino: str) -> str:
    """Muestra el resultado con exactamente dos decimales y la unidad de destino."""
    u = unidad_destino.upper()
    if round(valor, 2) == 0.0:
        valor = 0.0
    return f"{valor:.2f} {u}"


def procesar_conversion(temp_str: str, origen_str: str, destino_str: str) -> Tuple[bool, str]:
    """Valida y procesa la conversión completa."""
    valor, err_temp = validar_entrada_temperatura(temp_str)
    if err_temp:
        return False, err_temp

    u_orig = normalizar_unidad(origen_str)
    if not u_orig:
        return False, "Unidad de origen no válida. Ingrese C, F o K."

    u_dest = normalizar_unidad(destino_str)
    if not u_dest:
        return False, "Unidad de destino no válida. Ingrese C, F o K."

    valido_cero, err_cero = validar_cero_absoluto(valor, u_orig)
    if not valido_cero:
        return False, err_cero

    res = convertir_temperatura(valor, u_orig, u_dest)
    return True, formatear_resultado(res, u_dest)
