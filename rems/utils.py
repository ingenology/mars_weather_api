def celsius_to_fahrenheit(celsius, rounded=True):
    fahrenheit = (9.0/5.0)*celsius + 32
    return float("{0:.2f}".format(fahrenheit)) if rounded else fahrenheit

def fahrenheit_to_celsius(fahrenheit, rounded=True):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return float("{0:.2f}".format(celsius)) if rounded else celsius


