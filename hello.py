logowania = [
    {"uzytkownik": "jan.kowalski", "ip": "203.0.113.10", "wynik": "nieudane"},
    {"uzytkownik": "anna.nowak", "ip": "198.51.100.25", "wynik": "udane"},
    {"uzytkownik": "jan.kowalski", "ip": "203.0.113.10", "wynik": "nieudane"},
    {"uzytkownik": "piotr.zielinski", "ip": "192.0.2.44", "wynik": "nieudane"},
    {"uzytkownik": "anna.nowak", "ip": "198.51.100.25", "wynik": "udane"},
    {"uzytkownik": "jan.kowalski", "ip": "203.0.113.10", "wynik": "nieudane"},
]
successful_logins = []
podejrzane_logowania = []

for logowanie in logowania:
    if logowanie["wynik"] == "nieudane":
        podejrzane_logowania.append(logowanie)
    else:
        successful_logins.append(logowanie)

nieudane_ip = []
nieudane_na_uzytkownika = {}
nieudane_na_ip = {}

for podejrzane_logowanie in podejrzane_logowania:
    ip = podejrzane_logowanie["ip"]
    uzytkownik = podejrzane_logowanie["uzytkownik"]

    if ip not in nieudane_ip:
        nieudane_ip.append(ip)

    if ip not in nieudane_na_ip:
        nieudane_na_ip[ip] = 0

    if uzytkownik not in nieudane_na_uzytkownika:
        nieudane_na_uzytkownika[uzytkownik] = 0

    nieudane_na_uzytkownika[uzytkownik] = nieudane_na_uzytkownika[uzytkownik] + 1
    nieudane_na_ip[ip] = nieudane_na_ip[ip] + 1

for uzytkownik, liczba_nieudanych in nieudane_na_uzytkownika.items():
    if liczba_nieudanych >= 3:
        print("ALERT: możliwy atak na konto:", uzytkownik)

for ip, liczba_nieudanych in nieudane_na_ip.items():
    if liczba_nieudanych >= 3:
        print("ALERT: wiele nieudanych logowań z IP:", ip)

print("Szczegóły podejrzanych logowań:")

for podejrzane_logowanie in podejrzane_logowania:
    print(
        f'Użytkownik: {podejrzane_logowanie["uzytkownik"]} | '
        f'IP: {podejrzane_logowanie["ip"]} | '
        f'Wynik: {podejrzane_logowanie["wynik"]}'
    )

print(f'Nieudane logowania według użytkownika: {nieudane_na_uzytkownika}')
print(f'Nieudane logowania według IP: {nieudane_na_ip}')
print(f'Adresy IP z nieudanymi logowaniami: {nieudane_ip}')        
# print("Podejrzane logowania:", podejrzane_logowania)
print(f'Nieudane logowania: {len(podejrzane_logowania)}')
print(f'Udane logowania: {len(successful_logins)}')

if len(podejrzane_logowania) >= 5:
    print("ALERT: wysoka liczba nieudanych logowań")
elif len(podejrzane_logowania) == 4:
    print("OSTRZEŻENIE: zbliżasz się do progu alertu")
else:
    print("brak alertu")
