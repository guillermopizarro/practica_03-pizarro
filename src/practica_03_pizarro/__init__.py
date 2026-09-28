"""Paquete practica_03_pizarro - Conversor de temperatura."""

import sys
from typing import Optional

from .converter import (
    ABSOLUTE_ZERO,
    UNIDADES_VALIDAS,
    convertir_temperatura,
    formatear_resultado,
    normalizar_unidad,
    procesar_conversion,
    validar_cero_absoluto,
    validar_entrada_temperatura,
)

__all__ = [
    "ABSOLUTE_ZERO",
    "UNIDADES_VALIDAS",
    "convertir_temperatura",
    "formatear_resultado",
    "normalizar_unidad",
    "procesar_conversion",
    "validar_cero_absoluto",
    "validar_entrada_temperatura",
    "main",
]


def ejecutar_interactivo() -> None:
    """Ejecuta el bucle interactivo de conversión de temperaturas."""
    print("=== Conversor de Temperatura ===")
    print("Unidades permitidas: Celsius (C), Fahrenheit (F), Kelvin (K)")
    print("Escriba 'salir' para terminar el programa.\n")

    while True:
        try:
            # Estado limpio en cada iteración
            resultado: Optional[str] = None

            entrada = input("Ingrese la temperatura: ")
            if entrada.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            # Si el usuario ingresó todo en una sola línea (ej. '100 C F')
            partes = entrada.strip().split()
            if len(partes) == 3:
                temp_token, orig_token, dest_token = partes
                exito, mensaje = procesar_conversion(temp_token, orig_token, dest_token)
                if exito:
                    resultado = mensaje
                    print(f"Resultado: {resultado}")
                else:
                    print(mensaje)
                print()
                continue

            # Paso 1: Validar temperatura
            valor, error_temp = validar_entrada_temperatura(entrada)
            if error_temp:
                print(error_temp)
                print()
                continue

            # Paso 2: Unidad de origen
            entrada_origen = input("Ingrese la unidad de origen (C, F, K): ")
            if entrada_origen.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            u_origen = normalizar_unidad(entrada_origen)
            if not u_origen:
                print("Unidad de origen no válida. Ingrese C, F o K.")
                print()
                continue

            # Paso 3: Unidad de destino
            entrada_destino = input("Ingrese la unidad de destino (C, F, K): ")
            if entrada_destino.strip().lower() in ("salir", "exit", "quit", "q"):
                print("Programa finalizado.")
                break

            u_destino = normalizar_unidad(entrada_destino)
            if not u_destino:
                print("Unidad de destino no válida. Ingrese C, F o K.")
                print()
                continue

            # Paso 4: Validar límite del cero absoluto
            valido_cero, error_cero = validar_cero_absoluto(valor, u_origen)
            if not valido_cero:
                print(error_cero)
                print()
                continue

            # Paso 5: Conversión y formateo
            num_res = convertir_temperatura(valor, u_origen, u_destino)
            resultado = formatear_resultado(num_res, u_destino)
            print(f"Resultado: {resultado}")
            print()

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


def main() -> None:
    """Punto de entrada de la aplicación."""
    # Si se pasan argumentos por línea de comandos (ej. practica-03-pizarro 100 C F)
    if len(sys.argv) == 4:
        temp_arg, orig_arg, dest_arg = sys.argv[1], sys.argv[2], sys.argv[3]
        exito, mensaje = procesar_conversion(temp_arg, orig_arg, dest_arg)
        if exito:
            print(f"Resultado: {mensaje}")
        else:
            print(mensaje)
        return

    ejecutar_interactivo()


if __name__ == "__main__":
    main()
