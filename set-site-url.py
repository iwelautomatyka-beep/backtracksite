# -*- coding: utf-8 -*-
"""
Ustawia publiczny adres strony we wszystkich miejscach naraz.

Adres absolutny jest potrzebny tylko wyszukiwarkom i podgladom linku: canonical, og:url,
og:image, dane strukturalne, robots.txt i sitemap.xml. Cala reszta strony korzysta ze
sciezek wzglednych, wiec dziala pod dowolnym adresem takze bez uruchamiania tego skryptu.

    py set-site-url.py https://j1nek.github.io/backtrack-site/

Skrypt czyta obecny adres z <link rel="canonical"> w index.html i podmienia go wszedzie,
wiec mozna go uruchamiac wielokrotnie - takze po przeniesieniu strony na wlasna domene.
"""
import io, os, re, sys

KAT = os.path.dirname(os.path.abspath(__file__))
PLIKI = ['index.html', 'privacy.html', '404.html', 'robots.txt', 'sitemap.xml']

if len(sys.argv) != 2:
    print(__doc__)
    sys.exit(1)

nowy = sys.argv[1]
if not nowy.startswith('http'):
    sys.exit('Adres musi zaczynac sie od http:// albo https://')
if not nowy.endswith('/'):
    nowy += '/'

index = io.open(os.path.join(KAT, 'index.html'), encoding='utf-8').read()
m = re.search(r'<link rel="canonical" href="([^"]+)"', index)
if not m:
    sys.exit('Nie znalazlem <link rel="canonical"> w index.html')
stary = m.group(1)
if not stary.endswith('/'):
    stary = stary.rsplit('/', 1)[0] + '/'

if stary == nowy:
    print('Adres juz ustawiony:', nowy)
    sys.exit(0)

for nazwa in PLIKI:
    p = os.path.join(KAT, nazwa)
    if not os.path.exists(p):
        continue
    s = io.open(p, encoding='utf-8').read()
    ile = s.count(stary)
    if ile:
        io.open(p, 'w', encoding='utf-8', newline='').write(s.replace(stary, nowy))
    print('%-14s %d' % (nazwa, ile))

print('\n%s  ->  %s' % (stary, nowy))
