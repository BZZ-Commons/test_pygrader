import pytest
import os

# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pfad zum zu testenden Skript
file_path = os.path.join(current_directory, 'Teilaufgabe6.py')  # Ersetzen Sie 'IhrSkriptname.py' mit dem Namen Ihrer Datei

def test_import_add_mul_from_calculator():
    """ Überprüft, ob die Funktionen 'add' und 'mul' aus dem Modul 'calculator' im Paket 'math_operations' importiert werden. """
    with open(file_path, 'r') as file:
        contents = file.read()
        assert 'from math_operations.calculator import add, mul' in contents, \
            "Funktionen 'add' und 'mul' werden nicht korrekt aus 'math_operations.calculator' importiert."

# Fügen Sie hier weitere Tests hinzu, falls benötigt
