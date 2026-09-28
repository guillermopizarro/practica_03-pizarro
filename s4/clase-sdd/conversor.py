"""Conversor de temperatura - Bloque 3.A (Spec a mano).

Implementación según spec_manual.md
"""

import sys
from typing import Optional, Tuple

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
    """Normaliza el texto de una unidad a 'C', 'F' o 'K'."""
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
    """Convierte la temperatura entre escalas usando las fórmulas exactas sin redondeos intermedios."""
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
    if abs(valor) < 1e-9:
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


def main() -> None:
    """Función principal interactiva."""
    if len(sys.argv) == 4:
        ok, res = procesar_conversion(sys.argv[1], sys.argv[2], sys.argv[3])
        if ok:
            print(f"Resultado: {res}")
        else:
            print(res)
        return

    print("=== Conversor de Temperatura ===")
    print("Unidades permitidas: Celsius (C), Fahrenheit (F), Kelvin (K)")
    print("Escriba 'salir' para terminar el programa.\n")

    while True:
        try:
            resultado: Optional[str] = None

            entrada = input("Ingrese la temperatura: ")
            if entrada.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            partes = entrada.strip().split()
            if len(partes) == 3:
                t_token, o_token, d_token = partes
                ok, msg = procesar_conversion(t_token, o_token, d_token)
                if ok:
                    resultado = msg
                    print(f"Resultado: {resultado}")
                else:
                    print(msg)
                print()
                continue

            valor, err_temp = validar_entrada_temperatura(entrada)
            if err_temp:
                print(err_temp)
                print()
                continue

            entrada_origen = input("Ingrese la unidad de origen (C, F, K): ")
            if entrada_origen.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            u_origen = normalizar_unidad(entrada_origen)
            if not u_origen:
                print("Unidad de origen no válida. Ingrese C, F o K.")
                print()
                continue

            entrada_destino = input("Ingrese la unidad de destino (C, F, K): ")
            if entrada_destino.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            u_destino = normalizar_unidad(entrada_destino)
            if not u_destino:
                print("Unidad de destino no válida. Ingrese C, F o K.")
                print()
                continue

            valido_cero, err_cero = validar_cero_absoluto(valor, u_origen)
            if not valido_cero:
                print(err_cero)
                print()
                continue

            num_res = convertir_temperatura(valor, u_origen, u_destino)
            resultado = formatear_resultado(num_res, u_destino)
            print(f"Resultado: {resultado}")
            print()

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    main()
