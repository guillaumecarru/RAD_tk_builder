# RAD_tk_builder

[Read in english](README.md)

## Bienvenue sur le projet RAD_tk_builder !

`RAD_tk_builder` est un outil utilisant la [méthode RAD](https://en.wikipedia.org/wiki/Rapid_application_development) qui permet de générer du code python after le module `tkinter`.

Ce projet reprend l'éditeur d'interface du projet [pygubu-designer](https://github.com/alejandroautalan/pygubu-designer) de l'utilisateur [Alejandro Autalán](https://github.com/alejandroautalan).

`RAD_tk_builder` convertit le fichier `xml` de `pybugu-designer` et le convertit en code python.

## Installation

RAD_tk_builder requiert Python >= 3

### Télécharger le repo dans un nouveau dossier

```
git clone https://github.com/JeanJdkJebuf/RAD_tk_builder.git
```

Installer les dépendances avec pipenv (Ajoutez votre version de python 3 à la place du x)
```
pipenv install python 3.x
```

## Utilisation

`pygubu` contient deux versions :

- **l'éditeur d'interface** [pygubu-designer](https://github.com/alejandroautalan/pygubu-designer). qui vous permet de créer le fichier xml de manière graphique.
- [pygubu core](https://github.com/alejandroautalan/pygubu) qui permet de charger et afficher le fichier xml.

`RAD_tk_builder` permet quant à lui convertit le fichier xml en code python, permettant au développeur de modifier les éléments à sa guise.

Voici les étapes nécessaires pour la création de votre fichier tkinter:
1. Vous devez avoir un fichier xml, écrit par `pygubu-designer`
2. Il faut être dans l'environnement virtuel du projet, donc à la racine de ce dernier, écrivez:
```bash
pipenv shell
```
3. Pour lancer le programme, utilisez le CLI fourni avec ce programme:
```bash
python main.py newdocument.py --uifile xmlfile.ui --conf_file conf.py
```
Ou:
- newdocument.py est le fichier qui va être créé, et qui contiendra le code tkinter.
- --uifile prend le fichier xml en argument.
- --conf_file prend en argument le fichier de configuration du fichier newdocument.py, qui va être créé en même temps que ce dernier.

4. Voila, c'était tout ! Vous pouvez regarder votre nouveau fichier !

### A propos du CLI
-  Le nom des fichiers doivent contenir .ui ou .py

-  Vous pouvez lancer le CLI seulement avec `newdocument.py`, il lancera alors un fichier.ui de démonstration.

- Le fichier par défault de --conf_file est conf.py. Vous pouvez le CLI sans cette option si le nom de ce fichier vous convient.

- Le launcher ne marchera pas si le fichier `newdocument.py` (dans l'exemple plus haut) existe déjà au sein de la racine du projet. Même chose pour l'option --conf_file.

## Annexe

Si vous avez une question concernant ce projet, n'hésitez pas à me contacter par mail.
