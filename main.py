#!/usr/bin/env python3


import sys
from modules.md import MDGen
from helpers import readargs, minpy, joinroot, isfile, isdir, dirfound
from config import DEFAULT_WORKING_DIR, DEFAULT_OUTPUT_FILE, DEFAULT_XML_FILE

# Define program run command
PROGRAM_RUN_COMMAND = 'pelican'

# Minimum version of Python required
MINIMUM_PYTHON_REQUIRED = '3.4'

# Settings for command line running
COMMAND_LINE_SETTINGS = {
    'command': PROGRAM_RUN_COMMAND,
    'params': {
        'xmlfile=': 'Specify path to XML file',
        'outfile=': 'Specify path for writing output file',
        'dir=': 'Directory which is used as working directory',
        'lang=': 'Specify the language using or let program detect automatically',
        'anyext': 'Whether to scan all files with all extensions'
    }
}


def main():
    """Main program"""

    # Check Python
    if not minpy(MINIMUM_PYTHON_REQUIRED):
        print('Failed! Minimum Python required is %s' % MINIMUM_PYTHON_REQUIRED)
        sys.exit(1)

    # Read arguments
    try:
        args = readargs(**COMMAND_LINE_SETTINGS)
    except SyntaxError as msg:
        print(msg)
        sys.exit(2)
    except SystemExit:
        sys.exit()

    # Load settings
    wdir = args.get('dir', DEFAULT_WORKING_DIR)
    xml = joinroot(wdir, args.get('xmlfile', DEFAULT_XML_FILE))
    out = joinroot(wdir, args.get('outfile', DEFAULT_OUTPUT_FILE))
    lang = args.get('lang', None)
    anyext = True if 'anyext' in args else False

    # Check XML file existence
    if not isfile(xml):
        print('Failed! XML file is not existed:', xml)
        sys.exit(1)

    # Check output file existence
    if isfile(out):
        print('Output file is existed:', out)
        confirm = input('Do you want to overwrite? (type Y to confirm, any key to exit): ')
        if confirm != 'Y':
            sys.exit()

    # Make sure output file is not a dir
    if isdir(out):
        print('Failed! Ouput file path is a directory:', out)
        sys.exit(1)

    # Check output file parent dir
    if not dirfound(out, path_is_file=True):
        print('Failed! Output file\'s parent dir is not found:', out)
        sys.exit(1)

    # Do generating
    try:
        MDGen(infile=xml, outfile=out, workdir=wdir, language=lang, any_ext=anyext)
    except Exception as msg:
        print('Failed! Error found: %s' % msg)
        sys.exit(2)

    # Done
    print('MD file successfully generated:', out)


if __name__ == '__main__':
    main()
