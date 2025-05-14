#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:
    '''Repräsentiert ein einfaches Bankkonto.'''

    __protokoll = []  # Protokoll für Transaktionen

    def __init__(self, inhaber : str, kontonummer: int):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.__kontostand = 0.0

    def __str__(self) -> str:
        '''Gibt eine benutzerfreundliche Darstellung des Kontos zurück.'''
        return f"Kontoinhaber: {self.inhaber}, Kontonummer: {self.kontonummer}, Kontostand: {self.__kontostand} EUR"

    def einzahlen(self, amount: float):
        '''Fügt einen Betrag zum Kontostand hinzu.'''
        self.__kontostand += amount
        self.__protokoll.append(("einzahlen", amount))

    def abheben(self, amount: float):
        '''Zieht einen Betrag vom Kontostand ab.'''
        if amount > self.__kontostand:
            print("Nicht genügend Guthaben.")
        else:
            self.__kontostand -= amount
            self.__protokoll.append(("abheben", amount))

    def get_kontostand(self) -> float:
        '''Gibt den aktuellen Kontostand zurück.'''
        return self.__kontostand

    def get_protokoll(self) -> list:
        '''Gibt das Protokoll der Transaktionen zurück.'''
        return self.__protokoll

bankkonto = BankAccount("Markus Kufka", 123456789)
bankkonto.einzahlen(1000)
bankkonto.abheben(200)
print(bankkonto.get_kontostand())
print(bankkonto.get_protokoll())
print(bankkonto)
for transaction in bankkonto.get_protokoll():
    print(f"Transaktion: {transaction[0]}, Betrag: {transaction[1]} EUR")