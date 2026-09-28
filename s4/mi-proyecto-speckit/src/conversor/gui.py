"""Interfaz Gráfica de Usuario (GUI) en Tkinter para el conversor de temperatura."""

import sys
import tkinter as tk
from tkinter import ttk
from typing import Optional

from conversor.core import procesar_conversion


class ConversorTemperaturaApp:
    """Controlador y vista de la aplicación de conversión de temperatura en Tkinter."""

    OPCIONES_UNIDAD = ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"]

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Conversor de Temperatura")
        self.root.geometry("420x340")
        self.root.resizable(False, False)

        # Variables de estado
        self.temp_var = tk.StringVar(value="")
        self.origen_var = tk.StringVar(value=self.OPCIONES_UNIDAD[0])
        self.destino_var = tk.StringVar(value=self.OPCIONES_UNIDAD[1])
        self.resultado_var = tk.StringVar(value="")
        self.error_var = tk.StringVar(value="")

        self._crear_widgets()

    def _crear_widgets(self) -> None:
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        lbl_titulo = ttk.Label(
            main_frame,
            text="Conversor de Temperatura",
            font=("Segoe UI", 14, "bold"),
        )
        lbl_titulo.pack(pady=(0, 15))

        # Campo: Temperatura
        frame_input = ttk.Frame(main_frame)
        frame_input.pack(fill=tk.X, pady=5)
        lbl_temp = ttk.Label(frame_input, text="Temperatura:", width=18, anchor="w")
        lbl_temp.pack(side=tk.LEFT)
        self.entry_temp = ttk.Entry(frame_input, textvariable=self.temp_var)
        self.entry_temp.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_temp.focus()

        # Selector: Unidad Origen
        frame_origen = ttk.Frame(main_frame)
        frame_origen.pack(fill=tk.X, pady=5)
        lbl_origen = ttk.Label(frame_origen, text="Unidad de origen:", width=18, anchor="w")
        lbl_origen.pack(side=tk.LEFT)
        self.combo_origen = ttk.Combobox(
            frame_origen,
            textvariable=self.origen_var,
            values=self.OPCIONES_UNIDAD,
            state="readonly",
        )
        self.combo_origen.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Selector: Unidad Destino
        frame_destino = ttk.Frame(main_frame)
        frame_destino.pack(fill=tk.X, pady=5)
        lbl_destino = ttk.Label(frame_destino, text="Unidad de destino:", width=18, anchor="w")
        lbl_destino.pack(side=tk.LEFT)
        self.combo_destino = ttk.Combobox(
            frame_destino,
            textvariable=self.destino_var,
            values=self.OPCIONES_UNIDAD,
            state="readonly",
        )
        self.combo_destino.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Botón Convertir
        self.btn_convertir = ttk.Button(
            main_frame,
            text="Convertir",
            command=self.ejecutar_conversion,
        )
        self.btn_convertir.pack(pady=15)

        # Etiquetas de Resultado y Error
        self.lbl_resultado = ttk.Label(
            main_frame,
            textvariable=self.resultado_var,
            font=("Segoe UI", 11, "bold"),
            foreground="#107C41",
            anchor="center",
        )
        self.lbl_resultado.pack(fill=tk.X, pady=2)

        self.lbl_error = ttk.Label(
            main_frame,
            textvariable=self.error_var,
            font=("Segoe UI", 10),
            foreground="#D83B01",
            anchor="center",
        )
        self.lbl_error.pack(fill=tk.X, pady=2)

        # Atajo Enter
        self.root.bind("<Return>", lambda event: self.ejecutar_conversion())

    def ejecutar_conversion(self) -> None:
        """Limpia cualquier estado previo y procesa la nueva conversión."""
        # Limpieza estricta de estado previo (US5)
        self.resultado_var.set("")
        self.error_var.set("")

        temp_str = self.temp_var.get()
        origen_str = self.origen_var.get()
        destino_str = self.destino_var.get()

        ok, mensaje = procesar_conversion(temp_str, origen_str, destino_str)
        if ok:
            self.resultado_var.set(f"Resultado: {mensaje}")
        else:
            self.error_var.set(mensaje)


def main() -> None:
    root = tk.Tk()
    app = ConversorTemperaturaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
