#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    return a / b

def potenziere(a, b):
    return a ** b

def modulo(a, b):
    return a % b

zahl1 = float(input("Bitte geben Sie die erste Zahl ein: "))
zahl2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
operation = input("Bitte wählen Sie die gewünschte Operation (+, -, *, /, **, %): ")

if operation == "+":
    print(addiere(zahl1, zahl2))
elif operation == "-":
    print(subtrahiere(zahl1, zahl2))
elif operation == "*":
    print(multipliziere(zahl1, zahl2))
elif operation == "/":
    print(dividiere(zahl1, zahl2))
elif operation == "**":
    print(potenziere(zahl1, zahl2))
elif operation == "%":
    print(modulo(zahl1, zahl2))
else:
    print("Ungültige Operation. Bitte wählen Sie +, -, *, /, ** oder %.")