---
marp: true
paginate: true
# class: invert
theme: rose-pine
footer: Tutorium 12 - 19.01.2024 - Nils Pukropp - https://s.narl.io/s/tutorium-12
header:
math: mathjax
---

# Tutorium 12 - 19.01.2024

Musterlösung 11 - Wiederholung Types - Functions!

---

# Type annotations
(Wiederholung)

---

## Type annotations - Was ist das?

---

## Type annotations - Was ist das?

* Jedes **Objekt** lässt sich mindestens einem **Typ** zuordnen
    * Objekte im mathematischen Sinne wie z.B. Variablen, Funktionen, ...
* Dieser **schränkt** den Wertebereich ein
    * z.B. ist eine Variable `x` von Typ `int` eine Ganzzahl
    * ähnlich zur mathematischen Schreibweise $x \in \mathbb{Z}$
* In der Informatik nennt man das **Typisierung**
    * Es gibt verschiedene Arten der Typisierung

---

## Type annotations - Typisierung

- **dynamische Typisierung** überprüft die gegebenen Typen zur **Laufzeit**
    - also erst wenn das Programm *läuft*
- **statische Typisierung** überprüft die gegebenen Typen zur **Übersetzungszeit**
    - also während wir den Quellcode übersetzen

### Was ist nun Python?

---

## Type annotations - Typisierung

- **dynamische Typisierung** überprüft die gegebenen Typen zur **Laufzeit**
    - also erst wenn das Programm *läuft*
- **statische Typisierung** überprüft die gegebenen Typen zur **Übersetzungszeit**
    - also während wir den Quellcode übersetzen

### Was ist nun Python?

- **dynamisch typisiert**
    - wir müssen unsere `.py` Datei ausführen bevor wir wissen ob alles korrekt ist
- **Pylance** ist ein eigenes Programm
    - es soll beim Schreiben bereits **Typverletzungen** erkennen
    - **unvollständige** Typüberprüfung, soll nur den Programmierer unterstützen

---

## Variabeln Typannotieren

* `variable_name: <Type> = ...`
* Beispiele:
    ```python
    x: int = 3
    y: int = 5
    string: str = "Hello World!"

    # aber auch eigene Objekte (OOP)
    point: Point = Point(3, 1)
    ```
* diese Annotation ist für uns **optional**

---

## Funktionen Typannotieren

* `def func_name(param1: <Type>, param2: <Type>, ...) -> <Type>`
* Beispiele:
    ```python
    def add(x: int, y: int) -> int:
        return x + y

    def div(x: float, y: float) -> Optional[float]:
        if y == 0.0:
            return None
        return x / y
    ```
* diese Annotation ist **verpflichtend** und muss so vollständig wie möglich sein

---

## Klassen Typannotieren

* 
    ```
    class ClassName:
        attribute_name1: <Type>
        attribute_name2: <Type>
        ...
    ```
* Beispiel:
    ```python
    @dataclass
    class Point:
        x: int
        y: int
    ```
* diese Annotation ist **verpflichtend** und muss so vollständig wie möglich sein

---

## Methoden Typannotieren

* `def method_name(self, param1: <Type>, ...) -> <Type>`
* Beispiel:
    ```python
    class Point:
        x: int
        y: int

    def distance_from(self, other: 'Point') -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    ```
* `self` muss **nicht** Typannotiert werden, kann aber
* `other` hingegen schon, wegen Python muss in der Klasse mit `'` annotiert werden
* diese Annotation ist **verpflichtend**

---

## Datentypen von Datentypen

* Manche Datentypen bauen sich aus anderen Datentypen auf
* z.B. `list` ist eine Liste von Elementen mit einem Typ
* hierfür verwenden wir `[]` um den Datentyp in `list` zu annotieren
    ```python
    def sum(xs: list[int]) -> int:
        total: int = 0
        for x in xs:
            total += x
        return total
    ```
* hierbei ist es wichtig so genau wie möglich zu annotieren!
* diese Annotation ist **verpflichtend**

---

## Häufige Fehler mit verschachtelten Typen

---

## Fehlerquelle - `tuple[...]`

* Tuple haben eine feste größe
* Tuple sind endlich
* Tuple können Elemente mit unterschiedlichen Typen haben
* Die Datentypen der Elemente werden mit einem `,` in `[]` getrennt
* Beispiel:
    ```python
    tup: tuple[int, int, float, str] = (1, 2, 3.0, "hello world")
    ```
* Diese Annotation ist **verpflichtend**

---

## Fehlerquelle - `dict[...]`

* Dictionary haben genau zwei zu definierende Typen
    * **Key**
    * **Value**
* Beispiel:
    ```python
    number_dictionary: dict[int, str] = {
        0: "zero",
        1: "one",
        2: "two",
    }
    ```
* Diese Annotation ist **verpflichtend**
* Diese kann weiter geschachtelt werden durch z.B. `list` als `Value`: 
    * `dict[int, list[str]]`

---

## Fehlerquelle - Typvariabeln (generische Typen)

* manchmal wollen wir nicht genau wissen welchen Datentypen wir haben
* dieser wird dann implizit von Python erkannt
* wir stellen damit sicher dass eine Typvariable **beliebig** aber **fest** ist
* Beispiel:
    ```python
    def add[T](x: T, y: T) -> T:
        return x + y
    ```
* `T` kann nur ein Datentyp sein, also muss `type(x) == type(y)` gelten
* **außer** wir schrenken `T` mit `|` ein: `T: (int | str)` damit müssen x und y nicht den gleichen Datentypen haben
* `T` lässt sich weiter einschränken durch `T: (int, str)`, hierbei ist `T` entweder ein `int` oder (exklusiv) `str`

---

## Fehlerquelle - Was ist TypeVar?

* `TypeVar` ist aus früheren Python-Versionen
* Typvariablen wurden vor der Python 3.12 so definiert:
    ```python
    T = TypeVar('T')
    ``` 
* sieht dumm aus, ist es auch, benutzt es nicht!

---

## Fragen zu Typannotationen?

---

# Funktionale Programmierung

---

## Funktionale Programmierung - was ist das?

- Funktionen sind äquivalent zu Datenobjekten
- anonyme Funktionen aka Lambdas
- Closures
- Programmablauf mit Verkettung und Komposition von Funktionen

---

## Funktionen sind Datenobjekte

- Jede Funktion hat den Datentyp `Callable`
- Wir können Funktionen wie alle anderen Objekte variabeln zuweisen
```python
def add(a: int, b: int) -> int:
    return a + b

add_but_variable = add

print(add_but_variable(3, 2)) # 5
```

---

## Anonyme Funktionen - `lambda`

- Mit dem `lambda` Keyword lassen sich anonyme Funktionen definieren ohne `def`
- Bietet sich vor allem an für kleine Funktionen und Kompositionen von Funktionen
    ```python
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 10
    ```
- hat als Datentyp auch `Callable`
    ```python
    add: Callable[[int, int], int] = lambda x, y: x + y
    ```

---

## Closures 

- Verkettete Funktionen, bei denen die Variabeln aus vorherigen benutzt werden können
    ```python
    def poly(x: float) -> Callable[[float, float], Callable[[float], float]]:
        return lambda a, b: lambda c: a * x ** 2 + b * x + c

    print(poly(3)(2, 3)(5)) # 2 * 3 ** 2 + 3 * 3 + 5 = 32
    ```
- kein wirklich schönes Beispiel, ein besseres ist `compose` für Kompositionen

---

## Komposition

- Verketten von Funktionen
    ```python
    def compose[T](*funcs: Callable[[T], T]) -> Callable[[T], T]:
        return reduce(lambda f, g: lambda n: f(g(n)), funcs)
        
    f: Callable[[int], int] = lambda n: n + 42
    g: Callable[[int], int] = lambda n: n ** 2
    h: Callable[[int], int] = lambda n: n - 3

    print(compose(f, g, h)(0))
    ```

---

## Higher-Order Functions

- nehmen eine oder mehrere `Callable` als Argument
- geben ein `Callable` zurück

### Higher-Order-Functions - `map`

- Wendet ein `Callable` auf jedes Element in einem `Iterable` an

    ```python
    def map[T, R](func: Callable[[T], R], xs: Iterable[T]) -> Iterable[R]:
        return [func(x) for x in xs]

    numeric_list = list(map(lambda e: int(e), ['1', '2', '3']))
    print(numeric_list) # [1, 2, 3]
    ```

---

### Higher-Order-Functions - `filter`

- `filter` verarbeitet Datenstrukturen anhand eines Prädikats (`Callable`)
- behält nur Elemente die das Prädikat erfüllen
    ```python
    def filter[T](predicate: Callable[[T], bool], xs: Iterable[T]) -> Iterable[T]:
        return [x for x in xs if predicate(x)]
    ```