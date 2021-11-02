# python-test

## 0. feladat

Jelen forráskód egy Docker-ből futtatható Flask webalkalmazás. Legelőször fork-old a projektet a saját GitHub felhasználóddal, és hozd létre a következő branch-eket a `main` branch-ből:

- `task-01`
- `task-02`
- `task-03`
- `task-04`

A feladatokat mindig a neki megfelelő branch-en végezd el!

## 1. feladat (task-01)

Futtasd a projektet a saját gépeden Docker segítségével. Hozz létre egy fájlt a gyökérkönyvtárba `app.log` néven, és másold be a konzol tartalmát, mely mutatja, hogy a Flask projekt sikeresen elindult. **Commit-old, majd push-old fel a módosításaidat a saját (fork-olt) git repository-dba.**

## 2. feladat (task-02)

Módosítd a forráskódot, hogy a Flask webalkalmazás böngészőben történő megnyitásakor a következő szöveget jelenítse meg: `task-02`. **Commit-old, majd push-old fel a módosításaidat a saját (fork-olt) git repository-dba.**

## 3. feladat (task-03)

Hozz létre egy `utils.py` fájlt, benne egy függvénnyel: `get_random_number`. Ez a függvény egy 1 és 100 közötti véletlenszerű egész számot adjon vissza. Hozz létre egy `/random` nevű végpontot az `app.py` fáljban, ami egy egyszerű szöveges válaszként ezt a számot adja vissza (vagyis ha újra és újra befrissítjük a `/random` aloldalt a böngészőben, akkor mindig más és más véletlenszerű számot kapunk). **Commit-old, majd push-old fel a módosításaidat a saját (fork-olt) git repository-dba.**

