# Pelican

**Author:** Bobby Yang

## General
This program is used to parse documents from source code files and write output content into a MarkDown format file

Master Build Status: [![Build Status](https://travis-ci.org/glyif/pelican.svg?branch=master)](https://travis-ci.org/glyif/pelican)

Dev Build Status: [![Build Status](https://travis-ci.org/glyif/pelican.svg?branch=dev)](https://travis-ci.org/glyif/pelican)

## Requirements
- Python version >= 3.4 with standard libraries installed

## How to use
Instructions for how to use this program can be found via its help document by running this command (assuming that we are in the main folder of the program, '$' sign is stating a command line prompt):

```bash
$ ./pelican help
```

The above command will show:

```bash
USAGE:
    pelican [PARAMS]

HELP:
    pelican help

PARAMS:
    --xmlfile <value>   Specify path to XML file
    --outfile <value>   Specify path for writing output file
    --anyext            Whether to scan all files with all extensions
    --lang <value>      Specify the language using or let program detect automatically
    --dir <value>       Directory which is used as working directory
```

If the **PARAMS** is not using, program will use default settings from the config file.

Currently working on compiling into a standalone executable.

## Examples

Run command, write output file to an absolute path at `/home/user/OUTPUT.md`, working directory, input XML file are getting from default settings, programming language will be detected automatically:
```bash
$ ./pelican --outfile /home/user/OUTPUT.md
```

XML file named `readme.xml` and output file named `README.md` will be got from the default working directory setting in config file
```bash
$ ./pelican --outfile README.md --xmlfile readme.xml
```

Working directory is being specified at `/home/user/project`, XML file `readme.xml` and output file `README.md` will be got from the specified working directory also:
```bash
$ ./pelican --outfile README.md --xmlfile readme.xml --dir /home/user/project
```

Specify using Python as language parser by param `--lang python`, and instruct the parser to scan all files without caring their extensions by param `--anyext` *(these two can be used individually)*. Any other options will be loaded as default settings from config file: 
```bash
$ ./pelican --lang python --anyext
```

## Supported languages
- **Python**
- **C**
- **JavaScript**
