---
marp: true
paginate: true
class: invert
# theme: uncover
footer: Tutorium 11 - 15.01.2023 - Nils Pukropp - https://s.narl.io/s/tutorium-11
header:
---

# Tutorium 11 - EidP 2024

Dictionary, List-Comprehensions, Funktionen als Objekte

---

## Dictionary

- Eine Ansammlung aus **Keys** und dessen **Werten**
- Ordnet jedem **Key** einen **Wert** zu
- Ein **Key** muss **immutable** sein, also keine `list`, `Objects`, ...
- **Werte** können mutable sein, also eigentlich alles.

---

### Creating a Dictionary

```python
dictionary = {
    <key>: <value>,
    <key>: <value>,
    ...
    <key>: <value>
}
```

---

### Creating a Dictionary

```python
dictionary = {
    <key>: <value>,
    <key>: <value>,
    ...
    <key>: <value>
}
```

#### Beispiel

```python
courses = {
    "eidp": ["np163", "az34", "jf334"],
    "mathe": ["aw331", "pl67"],
    "sdp": []
}
```