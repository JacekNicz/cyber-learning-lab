logowania = [0, 0, 1, 1, 0, 1]
failed_logins = 0

for wynik in logowania:
    if wynik == 1:
        failed_logins = failed_logins + 1

print("Nieudane logowania:", failed_logins)
if failed_logins >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif failed_logins == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")