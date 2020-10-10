# RAD_tk_builder

[Read in French](LEEME.md)

## Welcome to the project RAD_tk_builder !

`RAD_tk_builder` is a [RAD tool](https://en.wikipedia.org/wiki/Rapid_application_development) that generates python code for `tkinter` module.

This project is complementary to [Alejandro Autalán](https://github.com/alejandroautalan)'s project [pygubu-designer](https://github.com/alejandroautalan/pygubu-designer).

`RAD_tk_builder` converts the `xml` file of `pybugu-designer` into python code.

## Installation

RAD_tk_builder requires Python >= 3

### Download tk_builder in a new repo

```
git clone https://github.com/JeanJdkJebuf/RAD_tk_builder.git

```

Install dependancies with pipenv (give your python version instead of x)
```
pipenv install python 3.x
```


## Usage 

`pygubu` contains two modules:

- **interface editor** [pygubu-designer](https://github.com/alejandroautalan/pygubu-designer). that helps you create the xml definition graphically.
- [pygubu core](https://github.com/alejandroautalan/pygubu) that loads and build user interface defined in xml.

`RAD_tk_builder` converts the `xml` file into python code, allowing the programmer to modify elements as he wishes.

Here are the steps to create your tkinter file:
1. You need an xml file, created by `pygubu-designer`.
2. Get in the virtual environment via pipenv, by typing:
```bash
pipenv shell
```
3. Launch the program, using the CLI:
```bash
python main.py newdocument.py --uifile xmlfile.ui --conf_file conf.py
```
Where :
- newdocument.py is the file that's going to be created, and will contain tkinter code
- --uifile takes as argument the uifile
- --conf_file takes as argument the configuration file for newdocument.py

4. You're done ! You can take a look at your new file !

### About the CLI
- Name of files should contain .ui, or .py

- You can launch CLI with only one argument, it will launch a test .ui file

- Default --conf_file name is conf.py. You can launch the CLI without that option if you don't mind.

- CLI won't work if `newdocument.py` (taken from example above) already exists. Same thing with --conf_file option.

## Annex

If you have any question regarding this project, please contact me by mail.
