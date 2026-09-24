logowania = [1, 0, 1, 1, 0, 1]
successful_logins = []
podejrzane_logowania = []

for wynik in logowania:
    if wynik == 1:
        podejrzane_logowania.append(wynik)
    else:
        successful_logins.append(wynik)

print("Podejrzane logowania:", podejrzane_logowania)
print("Nieudane logowania:", len(podejrzane_logowania))
print("Udane logowania:", len(successful_logins))
if len(podejrzane_logowania) >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif len(podejrzane_logowania) == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")