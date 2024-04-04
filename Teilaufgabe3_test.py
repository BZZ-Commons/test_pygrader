import os

# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pfad zum zu testenden Skript und zum calc-Modul
file_path = os.path.join(current_directory, 'Teilaufgabe3.py')

def test_import_add_mul_from_calc():
    """ Überprüft, ob die Funktionen 'add' und 'mul' aus dem Modul 'calc' importiert werden. """
    with open(file_path, 'r') as file:
        contents = file.read()
        assert 'from calc import add, mul' in contents, \
               "Funktionen 'add' und 'mul' werden nicht korrekt aus 'calc' importiert."
