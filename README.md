## Függvény definiálása:

```python
def simple_function():
	print('hello')
```

A függvények definíciója a logika amit a függvény végrehajt ha a kódban meghívjuk. Egy függvény hívása mindig a definíciót követően történhet és sosem előtte:

```python
simple_function()
```


## Paraméterek
Nagyon gyakran a függvényeknek paramétereket kell átadnunk melyekkel dolgozniuk kell. Ezek a paraméterek az un. elvárt (positional) paraméterek:

```python
def say_hello(name):
	print(f'hello {name}')
```

A fenti esetben a függvényt csak úgy hívhatod ha megadod a kért paramétert:
```python
say_hello("Robert")
```

A paraméterlista tetszőleges hosszúságú lehet:
```python
def say_hello(name, address, phone, email):
	print(name, address, phone, email)
```

Az több paraméterrel definiált függvényeknél figyelj a paraméterek sorrendjére a hívásnál!
```python
sayHello("Robert", "Budapest", "062045789", "mail.pythonsuli@gmail.com")
```

## Alapértelmezett (default) paraméterek

A paramétereknek adhatsz egy “default” értéket amit a függvény alkalmaz ha a hívásnál nem adtuk meg:
```python
def addNumbers(a=1, b=2):
	return a+b
```

A függvény hívásnál elég csak az egyik paramétert átadni, a másik megkapja a default értéket:
```python
print( addNumbers(10) )
>>> 12
```

Ha használod a paraméterek neveit (keyword) akkor megoldható az is, hogy a függvény hívásnál felcseréljük a paraméterek sorrendjét:
```python
print( addNumbers(b=10, a=20) )
```

Arra figyelj, hogy a definícióban a default paraméterek mindig a positional paraméterek után következhetnek:
```python
def sayHello(name, address, phone=None, email=None):
	print(name, address)
	if phone: 
        print(phone)
	if email: 
        print(email)
```

## Paraméter annotáció
Egy függvény paramétereit elláthatjuk un. annotációval amivel jelöljük, hogy a a paraméter milyen típusú lehet. 

```python
def say_hello(name: str, age: int, address: str):
    ...
```
Fontos megjegyezni ha a függvénynek mégis más típusú paramétert adunk át azt a python nem fogja vizsgálni.

## Docsrting
A docstring lényegében a függvényhez írt dokumentáció ami olvasható ha meghívjuk a függvényt és egérrel a függvény neve felé állunk. Ezzel jegyzetet készíthetünk azoknak akik a függvényünket használni fogják. 

```python
def say_hello(name, age, address):
    """
    This function prints out the user's data.

    Parameters:
        name (str): This is the username.
        age (int): User's age
        address (str): User's address
    """
```


## Tetszőleges hosszúságú paraméterlista (variable length arguments)

Bizonyos helyzetekben előre nem tudhatjuk, hogy a függvényünk kap e paramétert és hány paramétert kap majd a hívásnál (lásd: dekorátorok). Ilyenkor használjuk az *args speciális paramétert:
```python
def printAll(*args):
	print(args)
```

Figyeld meg, hogy a függvényblokkon belül az `args` minden esetben listaként (tuple) kerül be és így is kell dolgozni vele:
```python
printAll("Robert", "Budapest", "062045789", "robert@gmail.com", 42)
```

Ugyanígy a függvényt fel lehet készíteni az un. keyword paraméterek fogadására is:
```python
def printAll(**kwargs):
	print(kwargs)
```

Figyeld meg a két csillag ** jelölést a paraméternév előtt! A függvény hívása ebben az esetben így néz ki:
```python
printAll(name="robert", address="Budapest", phone="0620458789", mail="robert@gmail.com")
```

A függvény belsejébe a kwargs egy dictionary-ként kerül be.

Természetesen a fent említett két speciális paraméter használható egyszerre is a definícióban, ahogy azt később a dekorátor függvényeknél látni fogod:
```python
def printAll(*args, **kwargs):
	print(args)
	print(kwargs)
```


## A Scope
Egy változó lehet `global` illetve `local` attól függően hogy egy függvényen kívül vagy belül lett deklarálva:

```python
name = "Robert"  # global variable

def printName():
	name = "Tamas"  # local variable
```

A global változók bárhonnan “láthatók” és eléred a bennük tárolt értéket akár egy függvényen belül is. A local változók ezzel szemben csak az adott függvényblokkon belül látszanak. Azok nincsenek semmilyen hatással a global változókra és más függvényekben létrejött, azonos nevű változókra. A függvény belseje egy “védett” tér ahol minden probléma nélkül definiálhatsz változókat a feladat végrehajtása érdekében.

Bizonyos helyzetekben szükséged lehet arra, hogy a global változó értékét egy függvényben átírd.  Mivel a global változókat minden függvény látja, a bennük tárolt adat egy közös megosztott térben van. Gyakran ezt az adatot frissítened kell a kód futása során:
```python
name = "Robert"

def changeName():
	global name
	name = "Tamas"
```

A `global` parancs behozza a változót a függvény belső terébe és ott módosíthatod a benne tárolt adatot. Ezt követően a többi függvényed már az új értéket fogja látni. 

## Return
Függvények különböző részfolyamatokon dolgoznak melynek során olyan adat keletkezhet ami fontos lehet más függvények számára. Az ilyen adatot minden függvény a return paranccsal adja vissza. Az alábbi példában egy függvény készít egy számlistát majd azt adja vissza:
```python
def create_numbers_to_max(max):
	numbers_to_max = list(range(max))
	return numbers_to_max 

print(create_numbers_to_max(10))
```


A return állhat több elemből is:
```python
def multipleReturns(name, address, phone):
	return name, address, phone
```

A fenti esetben a függvény lefutása során egy tuple-t kapunk.

>A Python-ban nem kötelező return sor a függvények végén. Ilyenkor a függvény futása minden esetben None-t ad vissza.

Ha tudjuk, hogy egy függvény hívása után visszakapunk valamilyen eredményt akkor a függvény hívást egy változó deklarálásával kezdjük:

```python
numberList = createList(10)
print(numberList)
```

## Beágyazott (nested) függvények
A beágyazott függvények lényegében csak függvényen belül definiált újabb függvény:

```python
def parent():

   def shild():
       pass
```


A beágyazott függvényekre is igaz az amit a lokális változókról írtam. Ez a függvény csak a lokális térben látszik és csak ott hívható:
```python
def parent():
   print("This is parent")

   def child():
       print("This is child")

   child()

parent()
```


Ha valamilyen külső paramétert kell átadni egy ilyen függvénynek akkor az lehet global változó mert azt minden függvény látja, vagy érkezhet a “parent” függvényen keresztül is mint paraméter:
```python
def parent(name, age):
   print("This is parent")

   def child():
       print("This is child")
       print(name, age)

   child()

parent("Robert", 42)
```

Figyeld meg, hogy a name és age paraméterek csak a mainFunc paraméterein keresztül érkeznek és bekerülnek a local térbe. Így az innerFunc látja és használhatja is ezeket. 


## Függvénytárak (modules)

A komolyabb programok fejlesztésénél nem dolgozhatunk egyetlen fájlban. Szükséges lehet egy külső függvénytár importálására amelyben hasznos, előre megírt függvényeket tárolunk. Eddigi gyakorlatok során használtunk már ilyen külső modulokat. Ilyen volt az os, random vagy a time.
import os, time, random


A python megtalálja ezeket a modulokat mert ezek útvonala tárolva van a környezeti változókban (environment variables) és a Python 3.7 esetében itt találhatóak: `C:\Program Files (x86)\Python37-32\Lib`.

Ha saját függvénytárat akarunk akkor a legegyszerűbb ha azt az aktuális könyvtárban tároljuk a program mellett amelyben be akarjuk importálni:

```
my_library
    __init__.py
    my_functions.py
my_program.py
```

**Fontos:** A modul könyvtárban hozzunk létre egy `__init__.py` fájlt. Így a könyvtárat a Python modulként fogja kezelni.

Ezt követően a my_program.py fájlban így importálhatóak a my_functions.py függvényei:
```python
from my_library.my_functions import my_function
```

Gyakori, hogy egy beimportált modul nevének rövidítést adunk (alias):
```python
from my_library import my_functions as mf

mf.my_function()
```

## Rekurzió
A rekurzió koncepciója azt jelenti, hogy egy függvény saját magát hívja meg a függvényblokkon belül. Két fontos része van egy ilyen függvénynek: Egy termináló és egy rekurziós blokk. A termináló blokk vizsgál egy feltételt és eldönti hogy szükséges e új kört futnia a függvénynek, ha igen, akkor jön a rekurzió. A lenti példában a függvény elszámol 10-ig:
```python
def callMyself(i):
   if i >= 10: # terminalo blokk
       print("I called myself 10 times already... that’s enough!")

   else: # rekurzios blokk
       print(f"I called myself {i} times...")
       callMyself(i+1)

callMyself(1)
```

Egyszerű gyakorlati példa a rekurzióra a fájlok összegyűjtése almappákból. A feladat az, hogy minden mappán és almappán végig kell haladni és listázni az ott található fájlokat:
import os

```python
def get_all_files(root, file_list):
    # minden fájl és mappa az aktuális mappában
    all_content = [os.path.join(root, i) for i in os.listdir(root)]

    subfolders = []
    for i in all_content:
        if os.path.isfile(i):
            file_list.append(i)
        else:
            subfolders.append(i)

    # rekurzios blokk
    for folder in subfolders:
        get_all_files(folder)

files = []
print(get_all_files(r"E:\Photos", files))
```


A fenti esetben nincs termináló blokk hiszen egy idő után kifogyunk az almappákból és a rekurzió megáll.

## Dekorátorok
A dekorátor a python egyik nagyon érdekes funkciója, amellyel egy függvényt “dekorálhatsz” egy másik függvénnyel. A mechanizmus hasonlít a beágyazott függvényekre. A dekorátor függvény egy másik függvényt kap paraméterként majd egy belső un. wrapper függvény segítségével futtatja a dekorált függvényt. Ebben a wrapper-ben írjuk meg a dekorátor logikáját. A legegyszerűbb példa egy timer dekorátor elkészítése, ahol minden függvény futási idejét visszakapjuk a dekorátor segítségével:
```python
import time, random

def my_timer(func):
   def wrapper(*args, **kwargs):
       start = time.time()
       result = func(*args, **kwargs)
       stop = time.time()
       print(f"Time: {stop - start}")
       return result
   return wrapper

@my_timer
def worker():
   time.sleep(random.randint(1,4))

@my_timer
def worker2():
   time.sleep(random.randint(1,4))

@my_timer
def worker3():
   time.sleep(random.randint(1,4))

worker()
worker2()
worker3()
```


Megfigyelheted, hogy egy dekorált függvény előtt szerepel a speciális karakter `@` és a dekorátor neve. Ezt követően jöhet a függvény definíciója. A dekorátor belsejében a `wrapper()` végzi a munkát és futtatja le a paraméterben kapott függvényeket. A `wrapper()` kapja meg az esetleges paramétereket is `(*args, **kwargs)` és adja át a `func()`-nak.

Természetesen dekorátorokat össze is fűzhetsz egy függvény felett (stacked decorators):
```python
import time, random

def my_decorator(func):
   def wrapper(*args, **kwargs):
       print("my_decorator call")
       return func(*args, **kwargs)
   return wrapper

def my_other_decorator(func):
   def wrapper(*args, **kwargs):
       print("my_other_decorator call")
       return func(*args, **kwargs)
   return wrapper

@my_decorator
@my_other_decorator
def worker():
   time.sleep(random.randint(1,4))

worker()
```

## Anonim függvények (lambda)
A `for` ciklusnál láttuk hogy írható fel egyszerűen egy sorban (list comprehension):
```python
fileList = [i for i in os.path.listdir("d:/photos/")]
```

Létezik egysoros a függvényekre is ez pedig a lambda:
```python
mySimpleFunc = lambda x : x+1
```

Az ilyen függvényeket hívjuk anonim függvénynek mégpedig azért mert nincs definíciója. A `lambda` függvényeket rendszerint a fenti formában láthatod. A kifejezést hozzárendeljük egy változóhoz (ez lesz a neve) és később így hívhatod meg:
```python
mySimpleFunc(10)
```

A lambda függvény szerkezetileg két részből áll. A kettőspont bal oldalán a paraméterlista a jobb oldalán pedig a kifejezés áll. A lambda minden esetben visszaadja a kifejezés eredményét. Természetesen itt is lehet több paraméter:
```python
anonimFunc = lambda a,b,c: a+b+c 
```

Az anonim függvényeket gyakran láthatod egy sortolási művelet tagjaként ahol megadhatunk egy speciális kulcsot a sortoló függvénynek amit érvényesít a lista rendberakásánál.
Alább egy példa egy névlista ABC sorrendbe rakásához:
```python
name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna"]

print( sorted(name_list) )
>>>['Kiss Elemér', 'Nagy Adrienn', 'Tóth Barna', 'Vári Róbert']
```

A `sorted()` függvény a lista mellet fogad egy key paramétert is ahol lehetőséged van megváltoztatni a bejövő adatot azért hogy a ortolás a szerint menjen végbe. A következő példa azt mutatja, hogy használok egy lambda függvényt ahhoz, hogy a sortolás a keresztnevek szerint történjen. A lambda függvény lényegében szétvágja a neveket a space karakternél és csak a keresztnevet adja vissza a sortoláshoz:
```python
print( sorted(name_list, key= lambda name: name.split()[-1]) )
>>>['Nagy Adrienn', 'Tóth Barna', 'Kiss Elemér', 'Vári Róbert']
```

## Threading: Több szálon futó folyamatok
Threading azt a folyamatot jelenti, amikor párhuzamosan, egyszerre több szálon indítunk el számításokat. Az eddigi példákban egyetlen szálon indítottam el a függvényeket és minden lépés meg kellett hogy várja az előtte lévő kalkulációkat. Ez az egyszerű működés sok esetben teljesen megfelelő és nincs igény több szálon indított kalkulációkra. Vannak helyzetek viszont, ahol a folyamatok konkurensen, vagyis egyszerre több szálon indulhatnak, hiszen a kapott adatok alapján minden folyamat el tudja végezni a rábízott munkát anélkül hogy várnia kéne egy másik függvény eredményére. Ilyenkor használhatjuk a python threading modulját. 


A következőben egy egyszerű példa két függvény párhuzamos indítására:
```python
import time, threading
def worker1():
   print("worker1 started...")
   time.sleep(10)
   print("worker1 finished!")

def worker2():
   print("worker2 started...")
   time.sleep(9)
   print("worker2 finished!")

t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()
```


A thread-ben futó függvénynek paramétert is át lehet adni az args=[] segítségével:
```python
import threading
import time

def worker_1(numbers):
   print("worker1 started...")
   for number in numbers:
       print("worker1 processing parameter: ", number)
       time.sleep(1)
   print("worker1 finished!")


def worker_2(numbers):
   print("worker2 started...")
   for number in numbers:
       print("worker2 processing parameter: ", number)
       time.sleep(1)
   print("worker2 finished!")


thread_1 = threading.Thread(target=worker_1, args=[range(11, 20)])
thread_2 = threading.Thread(target=worker_2, args=[range(21, 30)])

thread_1.start()
thread_2.start()
```

## Queue
Ha a párhuzamosan futó folyamatoknak közös forrásból (lista) kell dolgozniuk, akkor használjuk a queue-t. Ez lényegében egy “lista” olyan speciális funkciókkal amelyekkel le tudjuk kezelni az egyidőben tőrténő adatkérést és a lista folyamatos frissítését (ürítést) is. 

Egy egyszerű példa erre egy fájlista amelyre egyszerre több szálon akarunk ráengedni egy “worker” függvényt hogy a feldolgozást meggyorsítsuk. Az első lépés minden esetben a queue feltöltése lesz:
```python
import time, os, queue, threading

jobList = queue.Queue()

# load queue
folder = "d:/tmp/"

files = [os.path.join(folder, i) for i in os.listdir(folder) if os.path.isfile(folder + i)]
for i in files:
    jobList.put(i)


A következő lépés a worker definiálása:
def worker():
   while not jobList.empty():
       # file bekerese a queue-bol
       f = jobList.get()
       print("working on", f)
       time.sleep(3)

       print("Work finished on", f)

       # jelezzuk a queue-nek, hogy keszen vagyunk.
       jobList.task_done()
```


Figyeld meg, hogy egy megosztott listából dolgozva minden körben megkérdezhetjük van e még adat a listában a `jobList.empty()` függvénnyel. Ez false amíg maradt még adat amin dolgozni lehet. A `jobList.task_done()` jelzi a queue-felé hogy a korábban kiadott feladat elkészült.

Az utolsó lépésben egy loop-ban elindítunk párhuzamosan 4 thread-et:
```python
for _ in range(4):
    t = threading.Thread(target=worker)
    t.start()
```


Figyeld meg azt, hogy a loop-ban egy speciális “_” karaktert használtam az eddig megszokott i, vagy item helyett. Ennek a karakternek nincs szerepe a loop belsejében ezért általánosan elfogadott gyakorlat, hogy ilyenkor így írjuk fel a loop-ot.

## Event
Az event abban segít, hogy egymástól függetlenül futó folyamatok jelzést adjanak ha elkészültek egy feladattal. A gyakorlatban ennek akkor van jelentősége, ha a függvények több szálon indulnak el de az egyik függvénynek várakoznia kell amíg egy másik befejezi a munkát. 
Tipikus példa erre egy grafikus felületen futó alkalmazás mint pl egy böngésző. A felület kirajzolása mindig a `__main__` thread feladata. Ezt nem lehet blokkolni hiszen a felhasználó azt hiheti, hogy lefagyott a program. Hogy ezt elkerüljük, minden időigényesebb folyamatot “kiszervezünk” egy külön thread-be amíg az ablak, amiben dolgozunk szabadon fut és nem akadályoz minket semmi abban, hogy böngésszük a netet. 
Az event ott jön be a folyamatba, ahol elindítunk egy letöltést a háttérben és a folyamat végén szeretnénk, hogy a fájl a végső helyére kerüljön egy mappába. 
A letöltés egy külön szálon indul el mialatt egy másik függvény, amely a fájlok átmozgatását végzi vár arra az eseményre, amikor a letöltés befejeződött. Eközben persze az ablakban folyamatosan frissíteni kell az esemény státuszát. 

A következő példában ezt a folyamatot szeretném modellezni egy egyszerű programmal.

Először beimportáljuk a szükséges python librar-kat:
```python
import time, threading, random, queue
```


Létrehozok egy download_ready egy copy_ready és egy download_queue változót:
```python
download_ready = threading.Event()
copy_ready = threading.Event()
downloaded_queue = queue.Queue()
```

A `download_ready` és `copy_ready` egy `Event()` osztály. Alapértelmezettként `False` értéket adnak vissza az `.is_set()` lekérdezésre. Ezeket a “zászlókat” fogom használni a két folyamat vezérlésére.


Készítek egy `download_service()` függvényt, amely egy folyamatos `while loop`-ot indít el, viszont az elején megáll mert várja, hogy a `copy_ready` event `True` legyen:
```python
def download_service():
    while True:
        # várjuk a copy_ready eseményt
        copy_ready.wait()

        print("Downloading random_file.jpg")
        time.sleep(random.randint(1,5))

        # adjunk valamit a queue-hoz.
        downloaded_queue.put("random_file.jpg")

        # ha végeztünk állítsuk a download_ready-t True-ra és ezzel egyidőben a copy_ready-t állítsuk alaphelyzetbe így mikor a while ciklus újraindul ismét várakozni fog.

        print("Download ready!")
        time.sleep(1)
        download_ready.set()
        copy_ready.clear()
```

A másik oldalt elindul egy `download_service` amely a következőképp néz ki:
```python
def copy_service():
    while True:
        # várakozunk a download_ready-re
        download_ready.wait()
        
        # queue-ből kiszedjük az adatot
        file = downloaded_queue.get()
        print(f"Copying {file}")
        time.sleep(random.randint(1,5))

        print("Copy is done!")
        time.sleep(1)
        
        # copy_ready jelzi hogy készen van a másolás mehet a következő download kör.
        copy_ready.set()
        
        # download_ready innentől False tehát a belső ciklusunk kénytelen megállni
        download_ready.clear()
```

A két folyamat thread-esítése és elindítása van hátra:
```python
t1 = threading.Thread(target=download_service)
t2 = threading.Thread(target=copy_service)

t1.start()
t2.start()
```

És ne feledd a copy_ready-t True-ra állítani az első kör elindulásához mert a download_service erre fog várni:
```python
copy_ready.set()
```