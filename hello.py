logowania = [
    {"uzytkownik": "jan.kowalski", "ip": "203.0.113.10", "wynik": "nieudane"},
    {"uzytkownik": "anna.nowak", "ip": "198.51.100.25", "wynik": "udane"},
    {"uzytkownik": "jan.kowalski", "ip": "203.0.113.10", "wynik": "nieudane"},
    {"uzytkownik": "piotr.zielinski", "ip": "192.0.2.44", "wynik": "nieudane"},
    {"uzytkownik": "anna.nowak", "ip": "198.51.100.25", "wynik": "udane"}
]
successful_logins = []
podejrzane_logowania = []

for logowanie in logowania:
    if logowanie["wynik"] == "nieudane":
        podejrzane_logowania.append(logowanie)
    else:
        successful_logins.append(logowanie)

nieudane_ip = []

for podejrzane_logowanie in podejrzane_logowania:
    ip = logowanie["ip"]

    if ip not in nieudane_ip:
        nieudane_ip.append(ip)

print("Adresy IP z nieudanymi logowaniami:", nieudane_ip)        

print("Podejrzane logowania:", podejrzane_logowania)
print("Nieudane logowania:", len(podejrzane_logowania))
print("Udane logowania:", len(successful_logins))

if len(podejrzane_logowania) >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif len(podejrzane_logowania) == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")