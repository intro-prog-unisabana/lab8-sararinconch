"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md

import sys

try:
    if len(sys.argv) != 3:
        raise ValueError
    carga_tot = float(sys.argv[1])
    puntos = float(sys.argv[2])
    if puntos == 0:
        raise ZeroDivisionError
    cargapunto = carga_tot / puntos
    print(f"Load per support point: {cargapunto:.2f} N")

except ValueError:
    print("Error: Invalid input! Enter numeric values only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero! Supports must be greater than zero.")