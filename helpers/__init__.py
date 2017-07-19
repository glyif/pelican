#!/usr/bin/env python3


import os, sys, getopt


def readfile(fpath):
    if not os.path.isfile(fpath):
        raise FileNotFoundError('File {:s} could not be found'.format(fpath))
    with open(fpath, 'r') as f:
        content = f.read()
    return content


def writefile(fpath, content, overwrite=False):
    if os.path.isfile(fpath) and not overwrite:
        raise FileExistsError('File is already existed: {:s}'.format(fpath))
    with open(fpath, 'w') as f:
        f.write(content)


def find_matches(text, patterns):
    patterns = [patterns] if isinstance(patterns, str) else list(patterns)
    for pattern in patterns:
        found = pattern.findall(text)
        if found:
            return found
    return []


def allfiles(folder, skipdot=False):
    """Return all files in input folder"""

    def isdot(item):
        """Check if folder of file is leading dot"""
        check = lambda s: s.startswith('.') and not s.endswith('.')
        try:
            next(filter(check, item.split('/')))
            return True
        except StopIteration:
            return False

    # Check input folder
    if not os.path.isdir(folder):
        raise NotADirectoryError('Folder not found: {:s}'.format(folder))

    # Traverse folder
    for root, _, files in os.walk(folder):
        if skipdot and isdot(root):
            continue
        for file in files:
            if skipdot and isdot(file):
                continue
            yield os.path.join(root, file)


def isfile(path):
    return os.path.isfile(path)


def isdir(path):
    return os.path.isdir(path)


def pathprep(root, path):
    """Prepare absolute and relative path for input path
    based on root path"""

    # Path is absolute
    if os.path.isabs(path):
        pref = os.path.abspath(root)

        # Path is related with root
        if path.startswith(pref):
            pos = 1 if pref == '/' else len(pref) + 1
            return path, path[pos:]

        # Path is not related with root
        else:
            return None, None

    # Path is relative
    else:
        return os.path.join(root, path), path


def getext(fpath):
    """Get file extension"""
    _, ext = os.path.splitext(fpath)
    return ext


def readargs(**kwargs):
    """Read command line arguments"""

    def usage():
        """Display usage info"""
        kv = ''
        for k, v in params.items():
            k = '--{} <value>'.format(k[:-1]) if k.endswith('=') else '--{}'.format(k)
            kv += '{i}{k:20}{v}\n'.format(i=indent, k=k, v=v)
        return fmt.format(i=indent, cmd=cmd, kv=kv)

    # Base definitions
    indent = ' ' * 4
    fmt = '\nUSAGE:\n{i}{cmd} [PARAMS]\n\nHELP:\n{i}{cmd} help\n\nPARAMS:\n{kv}'
    cmd = kwargs['command'] if 'command' in kwargs else ''
    params = kwargs['params'] if 'params' in kwargs else {}

    # Read arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', list(params.keys()))
    except getopt.GetoptError as msg:
        msg = '{:s}\nTry "{:s} help" for more information'.format(msg, cmd)
        raise SyntaxError(msg)

    # Display help if required
    if 'help' in args:
        print(usage())
        raise SystemExit

    # Return arguments
    return {k[2:]: v for k, v in opts}


def minpy(ver):
    """Check required version for current Python"""
    if not str(ver).replace('.', '').isdigit():
        raise ValueError('Input version is incorrect')
    curver = sys.version_info
    pairs = zip([curver.major, curver.minor, curver.micro], map(int, ver.split('.')))
    for cur, req in pairs:
        if cur > req:
            return True
        elif cur < req:
            return False
    return True


def basedir(path, path_is_file=False):
    """Get last folder name of folder or file path"""
    path = os.path.abspath(path)
    return os.path.dirname(path) if path_is_file else os.path.basename(path)


def joinroot(root, path):
    """Join path to root if path is relative"""
    return path if os.path.isabs(path) else os.path.join(root, path)


def dirfound(path, path_is_file=False):
    """Check existence of folder if path is folder, parent folder if path is file"""
    return os.path.isdir(os.path.dirname(path) if path_is_file else path)
