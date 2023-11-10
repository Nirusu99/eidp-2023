# Tutorium 04 - 10.11.2023

## [Exercise 02](https://proglang.informatik.uni-freiburg.de/teaching/info1/2023/exercise/sheet02.pdf) und [Exercise 03](https://proglang.informatik.uni-freiburg.de/teaching/info1/2023/exercise/sheet03.pdf)

### Punkteverteilung Exercise 02

![image not found](points_ex2.png)

### Punkteverteilung Exercise 03

![image not found](points_ex3.png)

### Häufige Fehler

- **Schaut genau was muss ausgegeben werden!!!**
- Achtet auf den Build-Output
  - **Linter-Error?** (-0.5 Punkte pro Datei)
  - **Syntax-Error?** (0 Punkte ab Exercise 4)
  - **Stunden eingetragen?** (-0.5 Punkte)
- lest euch die Aufgaben genau durch
- kommentiert keinen Quellcode aus, lasst ihn weg, oder lasst ihn stehen
- Testet euren Code mit `assert`
  - später lernen wir noch bessere Tests kennen
  - lasst eure `assert` nicht einfach in der Logik stehen!

    ```py
    def some_function(arg):
        assert arg <= 360 # WRONG!
        return calculate(arg)
    ```

    ```py
    def some_function(arg) -> float:
        return calculate(arg)

    if __name__ == "__main__":
        # Right! Nur testen ob alles tut, mehr nicht
        # und in __main__ packen, damit nicht jeder import die asserts aufruft
        assert some_function(0.69)  <= 42
        assert some_function(0.420) <= 1337
    ```

## Vorstellen/Vorrechnen

- mz242
- vb205

## [Exercise 04](https://proglang.informatik.uni-freiburg.de/teaching/info1/2023/exercise/sheet04.pdf)

- Abgabe Montag 9:00 im [Git](https://git.laurel.informatik.uni-freiburg.de/)
- Typannotationen jetzt wichtig.
- `min` Funktion darf in 4.1 nicht benutzt werden.
- Aufgabenteile werden mit **0 Punkten bewertet**, wenn:
  - Dateien und Funktionen nicht so benannt sind, wie im Aufgabentext gefordert;
  - Dateien falsche Formate haben, z.B. PDF statt plaintext;
  - Pythonskripte wegen eines Syntaxfehlers nicht ausführbar sind.
  - Verwenden Sie nur Befehle und Programmiertechniken, die Inhalt der bisherigen Vorlesungen (bis zum Abgabetermin) und Übungsblättern waren. (Ausnahme: f-Strings)
- Fragen?
