logowania = [1, 1, 1, 1, 1]
failed_logins = 0
successful_logins = 0
podejrzane_logowania = []

for wynik in logowania:
    if wynik == 1:
        failed_logins = failed_logins + 1
        podejrzane_logowania.append(wynik)
    else:
        successful_logins = successful_logins + 1  
        
print("Podejrzane logowania:", podejrzane_logowania)
print("Nieudane logowania:", failed_logins)
print("Udane logowania:", successful_logins)
if failed_logins >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif failed_logins == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")