import os

# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pfad zum zu testenden Skript und zum calc-Modul
file_path = os.path.join(current_directory, 'Teilaufgabe5.py')

def test_import_calculator_from_math_operations():
    """ Überprüft, ob das Modul 'calculator' aus dem Paket 'math_operations' importiert wird. """
    with open(file_path, 'r') as file:
        contents = file.read()
        assert 'from math_operations import calculator' in contents, \
            "Modul 'calculator' wird nicht korrekt aus 'math_operations' importiert."
