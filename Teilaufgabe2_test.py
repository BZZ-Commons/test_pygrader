import os

# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pfad zum zu testenden Skript
file_path = os.path.join(current_directory, 'Teilaufgabe2.py')

def test_import_calc():
    """ Überprüft, ob das Modul 'calc' korrekt importiert wird. """
    with open(file_path, 'r') as file:
        contents = file.read()
        assert 'import calc as c' in contents, \
               "Import-Statement für 'calc' fehlt oder ist falsch."