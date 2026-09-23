failed_logins = int(input("Podaj liczbę nieudanych logowań: "))
if failed_logins >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
else:
    print("brak alertu")