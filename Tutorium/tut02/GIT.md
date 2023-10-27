# Beispiel Git-Workflow

## SSH-Key generieren und im Git hinzufügen

### Linux & Mac-OS

Generiere einen Key mit

```sh
ssh-keygen -t ed25519 -C "you@mail.com"
```

Gib den Key in die Konsole aus mit

```sh
cat ~/.ssh/id_ed25519.pub
```
Kopiere mit Strg+Shift+C oder Rechtklick den Key aus dem Terminal und fügen ihn im [Git](https://git.laurel.informatik.uni-freiburg.de/user/settings/keys) als SSH Key hinzu.

### Windows

Generiere einen Key und kopiere ihn

```ps
ssh-keygen.exe -t ed25519 -C "you@mail.com"
cat ~/.ssh/id_ed25519.pub | clip
```

fügen dann den Key im [Git](https://git.laurel.informatik.uni-freiburg.de/user/settings/keys) als SSH Key hinzu.

### Mac

Generiere einen Key mit
```sh
ssh-keygen -t ed25519 -C "you@mail.com"
pbcopy < ~/.ssh/id_ed25519.pub
```

fügen dann den Key im [Git](https://git.laurel.informatik.uni-freiburg.de/user/settings/keys) als SSH Key hinzu.

## Das Repository clonen

Erstmal ist es wichtig wie man sich im Terminal überhaupt bewegt und umschaut. Wenn wir das Terminal starten, egal ob in Windows/Linux/Mac landen wir im Home-Verzeichnis often bezeichnet als `~`. Um den ersten Schritt zu gehen müssen wir erstmal wissen was wir hier überhaupt haben. Hierfür haben wir das Programm `ls`, welches den Inhalt in einem (ohne Argumente im aktuellen) Verzeichnis auflistet. Eine Beispielausgabe wäre:

```sh
niru@linux ~> ls
total 16
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Desktop/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:16 Downloads/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Pictures/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Videos/
```

Nun können wir uns in die anderen Verzeichnisse bewegen mit `cd` (change directory).

```sh
niru@sadly-not-linux ~> cd Downloads/
niru@sadly-not-linux ~/Downloads> ls
total 0
-rw-r--r-- 1 niru niru 0 Oct 27 02:19 cat.png
```

mit `cd ..` können wir uns jetzt ein Verzeichnis wieder nach oben bewegen

```sh
niru@sadly-not-linux ~/Downloads> cd ..
niru@sadly-not-linux ~> ls
total 16
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Desktop/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:19 Downloads/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Pictures/
drwxr-xr-x 2 niru niru 4096 Oct 27 02:14 Videos/
```

nun clonen wir das Repository indem wir ins [Git](https://git.laurel.informatik.uni-freiburg.de/2021WS-EiP/) gehen, auf unser persönliches Repository gehen. Und oben bei **SSH** auf **Copy**/**Kopieren** gehen.

Nun müssen wir einfach nur noch folgenden Befehl eingeben

```sh
niru@sadly-not-linux ~> git clone ssh://git@git.laurel.informatik.uni-freiburg.de:2222/2021WS-EiP/np163.git
Cloning into 'np163'...
The authenticity of host '[git.laurel.informatik.uni-freiburg.de]:2222 ([132.230.166.132]:2222)' can't be established.
ED25519 key fingerprint is SHA256:zR3d+3MewcoiAuwVidHYfWcsNjT/OVz5FR6IwIyTNCs.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[git.laurel.informatik.uni-freiburg.de]:2222' (ED25519) to the list of known hosts.
remote: Enumerating objects: 594, done.
remote: Counting objects: 100% (594/594), done.
remote: Compressing objects: 100% (573/573), done.
remote: Total 594 (delta 336), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (594/594), 86.90 KiB | 2.63 MiB/s, done.
Resolving deltas: 100% (336/336), done.
```

nun können wir mit `ls` nachschauen dass ein neuer Ordner erschienen ist, in meinem Fall **np163**.

```sh
niru@sadly-not-linux ~> ls
total 20
drwxr-xr-x  2 niru niru 4096 Oct 27 02:14 Desktop/
drwxr-xr-x  2 niru niru 4096 Oct 27 02:19 Downloads/
drwxr-xr-x  2 niru niru 4096 Oct 27 02:14 Pictures/
drwxr-xr-x  2 niru niru 4096 Oct 27 02:14 Videos/
drwxr-xr-x 17 niru niru 4096 Oct 27 02:24 np163/
```

Nun können wir diesen Ordner in VSCode öffnen und haben einen Workspace um die Übungsaufgaben zu bearbeiten.