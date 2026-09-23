failed_logins = int(input("Podaj liczbę nieudanych logowań: "))
if failed_logins >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif failed_logins == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")