import os
import importlib.util


# Ermitteln des aktuellen Verzeichnispfades
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pfad zum zu testenden Skript und zum calc-Modul
file_path = os.path.join(current_directory, 'Teilaufgabe4.py')
calc_path = os.path.join(current_directory, 'calc.py')

def test_import_addition_multiplication_from_calc():
    """ Überprüft, ob die Funktionen 'add' und 'mul' als 'addition' und 'multiplication' importiert werden. """
    with open(file_path, 'r') as file:
        contents = file.read()
        assert 'from calc import add as addition, mul as multiplication' in contents, \
            "Funktionen 'add' und 'mul' werden nicht korrekt importiert."


def test_main_output(monkeypatch):
    """ Überprüft, ob die Ausgabe der 'main'-Funktion den erwarteten Werten entspricht. """
    spec = importlib.util.spec_from_file_location("main_module", file_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)

    # Erstellen eines StringIO-Objekts, um die Ausgabe von print zu erfassen
    from io import StringIO
    captured_output = StringIO()
    monkeypatch.setattr("sys.stdout", captured_output)

    # Aufrufen der main-Funktion
    main_module.main()

    # Überprüfen der Ausgabe
    expected_output = "10\n25\n10\n25\n"
    assert captured_output.getvalue() == expected_output, \
        f"Fehler in der Ausgabe der 'main'-Funktion. Erwartet: {expected_output}, Erhalten: {captured_output.getvalue()}"