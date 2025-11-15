#generatory

def licz_do(n):
    for i in range(n):
        yield i         # yield - zwraca liste wartosci inaczej niz return; yield generuje zwrot i dalej dziala w funkcj a return konczy, generator
                            # dzieki yield mozna zrobic tiu petle, return by zakonczyl po jednym wywolaniu, po pierwszej iteracji                
for liczba in licz_do(5):
    print(liczba)

print()


def kwadraty(n):
    for i in range(n):
        yield i**2

for l in kwadraty(5):
    print(l)

print()

gen = (x * 2 for x in range(10)) # skrocony zapis generatora

for x in gen:
    print(x)

print()


def licznik():
    for i in range(3):
        yield i

gene = licznik()
print(next(gene)) #0 
print(next(gene)) #1
print(next(gene)) #2 to robi ten next

print("--- --- ---")


#domknięcia: clousers - ang.

def mnoznik(n):
    def mnoz(x):
        return x * n
    return mnoz

podwoj = mnoznik(2)
potroj = mnoznik(3)

print(podwoj(5)) 
print(potroj(5))

print("--- --- ---")


def licznikWywolan():
    liczba = 0
    def zwieksz():
        nonlocal liczba #nonlocal sluzy do obslugi zmiennych w funkcjach zagniezdzonych
        liczba += 1
        return liczba
    return zwieksz


licz = licznikWywolan()
print(licz()) # funkcje te mają jakby pamieć dlatego w wwyniku jest 1,2,3 a nie 1,1,1, to sie przydaje
print(licz())
print(licz())

print("--- --- ---")

def logger(prefix):
    def log(msg):
        print(f"[{prefix}] {msg}")
    return log

info = logger("INFO")
error = logger("ERROR")

info("Aplikacja wystartowala")
error("Brak pliku konfiguracyjnego")


#rekurencja

def silnia(n):  # funkcja wywoluje samą siebie = rekurencja
    if n == 0:
        return 1
    return n * silnia(n - 1)
    

print(silnia(5))

print("---")


def odlicz(n):
    if n == 0:
        print("Start")
    else:
        print(n)
        odlicz(n - 1)

odlicz(5)


def fib(n): #fibonnacci rekurencyjnie
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(10)])


#dekoratory...



