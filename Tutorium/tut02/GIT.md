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
nils@linux ~> ls
total 16
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Desktop/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:16 Downloads/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Pictures/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Videos/
```

Nun können wir uns in die anderen Verzeichnisse bewegen mit `cd` (change directory).

```sh
nils@linux ~> cd Downloads/
nils@linux ~/Downloads> ls
total 0
-rw-r--r-- 1 nils nils 0 Oct 27 02:19 cat.png
```

mit `cd ..` können wir uns jetzt ein Verzeichnis wieder nach oben bewegen

```sh
nils@linux ~/Downloads> cd ..
nils@linux ~> ls
total 16
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Desktop/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:19 Downloads/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Pictures/
drwxr-xr-x 2 nils nils 4096 Oct 27 02:14 Videos/
```

nun clonen wir das Repository indem wir ins [Git](https://git.laurel.informatik.uni-freiburg.de/2021WS-EiP/) gehen, auf unser persönliches Repository gehen. Und oben bei **SSH** auf **Copy**/**Kopieren** gehen.

Nun müssen wir einfach nur noch folgenden Befehl eingeben

```sh
nils@linux ~> git clone ssh://git@git.laurel.informatik.uni-freiburg.de:2222/2021WS-EiP/np163.git
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
nils@linux ~> ls
total 20
drwxr-xr-x  2 nils nils 4096 Oct 27 02:14 Desktop/
drwxr-xr-x  2 nils nils 4096 Oct 27 02:19 Downloads/
drwxr-xr-x  2 nils nils 4096 Oct 27 02:14 Pictures/
drwxr-xr-x  2 nils nils 4096 Oct 27 02:14 Videos/
drwxr-xr-x 17 nils nils 4096 Oct 27 02:24 np163/
```

Nun können wir diesen Ordner in VSCode öffnen und haben einen Workspace um die Übungsaufgaben zu bearbeiten.

## Git

Nun bewegen wir uns ins Git-Verzeichnis mit `cd np163`. Und führen unseren ersten Git-Command aus `git status`

```sh
nils@linux ~/np163 (master)> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

wir sehen, dass aktuell noch nichts im Verzeichnis geändert wurde. Das ändern wir jetzt indem wir in VSCode eine `hello_world.py` erstellen. Und den `git status` wiederholen

```sh
nils@linux ~/np163 (master)> git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello_world.py

nothing added to commit but untracked files present (use "git add" to track)
```

hier schlägt uns Git auch direkt schon vor `git add` zu verwenden um die neue Datei hinzuzufügen.

```sh
nils@linux ~/np163 (master)> git add hello_world.py
nils@linux ~/np163 (master)> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello_world.py
```

nun können wir die Datei in unser Git eintragen indem wir `git commit -m 'meine nachricht'` verwenden.

```sh
nils@linux ~/np163 (master)> git commit -m 'created hello_world.py'
[master 4191d5b] created hello_world.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 hello_world.py
```

und diese Änderung dann mit `git push` hochladen.

```sh
nils@linux ~/np163 (master)> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 285 bytes | 285.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: . Processing 1 references
remote: Processed 1 references in total
To ssh://git.laurel.informatik.uni-freiburg.de:2222/2021WS-EiP/np163.git
   06b6eb7..4191d5b  master -> master
```

Dieser Vorgang kann ganz einfach über die VSCode Ui gemacht werden. Anmerkungen gerne an [meine Mail](mailto:nils@narl.io) um das Git-Tutorial zu verbessern.