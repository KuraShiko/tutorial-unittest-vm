def sumar(a, b):
    """
    Esta función toma dos números como argumentos y devuelve su suma.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números")
    return a + b
