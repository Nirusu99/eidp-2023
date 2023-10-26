
# Zusammenfassung der Vorlesung

## Variablen und Zuweisungen

```python
variable = 42
print(variable)
print(variable + variable)
```

- Case-Sensitive
- A-z, 0-9, _
- Keine Schlüsselwörte

### Kurzzuweisung

Operationen und Zuweisung können in einem Schritt durchgeführt werden mit `${Operation}=`

```python
number = 42
number **= 42
assert number == 42 ** 42
number += 42
assert number == 42 ** 42 + 42
```

---

## Assert

- Erwartet einen wahren Ausdruck, wenn dieser nicht erfüllt ist gibt es einen Fehler
- Gut um etwas schnell zu testen

```py
number = 42
assert number == 42
bigger_number = number ** number
assert number ** number == bigger_number
```

---

## Typen

```py
number = 42
string = '42'
assert number != string
```

---

## Funktionen

### Standardfunktionen

- Typen konvertieren

```python
>>> int(2.6)
2
>>> float(2)
2.0
>>> str(2.0)
'2.0'
```

- Input/Output

```python
>>> input("Hier Input geben: ")
Hier Input geben: 42
'42'
>>> print(42)
42
```

### Funktionen kombinieren

```python
>>> int(str(2))
2
>>> str(int('2'))
'2'
```

### Neue Funktionen definieren

Mit `def` können neue Funktionen definiert werden

```python
def my_print_func(some_text):
    print(some_text)

def my_add(a, b):
    return a + b

my_print_func(my_add(1, 2)) # prints 3
```

---

## Imports

Mit `import` können Module (andere Python-Datein) importiert und benutzt werden

```python
import math

print(math.cos(math.pi)) # prints -1.0
```

Mit `from` und `import` können Sachen aus einem Modul spezifisch importiert werden

```python
from math import cos, pi

print(cos(pi)) # prints -1.0
```

---

## Scopes

Variabeln existieren in so genannten Scopes, am besten veranschaulicht man sich das einfach:

```python
GLOBAL_X = 42

def my_func():
    x_in_func = 42  # x_in_func wird hier im Scope der Funktion erstellt
    print(GLOBAL_X) # GLOBAL_X ist im globalen Scope, 
                    # also auch hier im Funktions-Scope, weil dieser Scope auch im globalen Scope ist 

print(x_in_func)    # wirft einen Fehler, weil x_in_func nicht im Scope ist
print(GLOBAL_X)     # Global Scope
```
