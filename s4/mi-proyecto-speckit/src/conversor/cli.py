"""Interfaz de Línea de Comandos (CLI) para el conversor de temperatura.

Totalmente compatible con la interfaz del Bloque 3.A.
"""

import sys
from typing import Optional
from conversor.core import (
    convertir_temperatura,
    formatear_resultado,
    normalizar_unidad,
    procesar_conversion,
    validar_cero_absoluto,
    validar_entrada_temperatura,
)


def main() -> None:
    """Función principal para ejecución por argumentos o interactiva en consola."""
    # Modo argumentos directos: conversor <temp> <origen> <destino>
    if len(sys.argv) == 4:
        ok, res = procesar_conversion(sys.argv[1], sys.argv[2], sys.argv[3])
        if ok:
            print(f"Resultado: {res}")
        else:
            print(res)
        return

    # Modo interactivo en bucle continuo
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

            # Atajo de 3 tokens en una sola línea (ej. "100 C F")
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
