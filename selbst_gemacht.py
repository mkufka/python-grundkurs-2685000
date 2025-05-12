#!/usr/bin/env python3

x = 10
y = 5

if x > y:
    print("x ist größer als y")

if x <= y:
    print("x ist kleiner als y")
else:
    print("x ist nicht kleiner als y")

if x == y:
    print("x ist gleich y")
elif x > y:
    print("x ist größer als y")
else:
    print("x ist kleiner als y")

# Aufgabe:
# Legen Sie zwei Variablen mit verschiedenen float Zahlenwerten an.
# Schreiben Sie eine if-else-Bedingung, die prüft, ob die erste Zahl 
# größer gleich oder kleiner der zweiten Zahl ist, und geben Sie das 
# entsprechende Ergebnis aus.

a = 2.0
b = 1.5

if a >= b:
    print("a = " + str(a) + " ist größer gleich b = " + str(b))
else:
    print("a = " + str(a) + " ist kleiner als b = " + str(b))
