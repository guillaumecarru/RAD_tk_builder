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


