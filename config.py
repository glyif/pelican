#!/usr/bin/python3

# Define dir which would be used to write output
# or do the file scanning as default
DEFAULT_WORKING_DIR = '.'

# Define path or name of output file, if this is
# relative path, then DEFAULT_WORKING_DIR would
# be used as root
DEFAULT_OUTPUT_FILE = 'README.md'

# Path or name of XML file, applied same treatment
# as DEFAULT_OUTPUT_FILE above
DEFAULT_XML_FILE = 'readme.xml'

# Extensions for C
C_EXTENSIONS = {'.c'}

# Extensions for Python
PYTHON_EXTENSIONS = {'.py'}

# Extensions for JavaScript
JAVASCRIPT_EXTENSIONS = {'.js'}

# Logo Alt text
DEFAULT_LOGO_ALT = ''

# Logo URL
DEFAULT_LOGO_URL = ''

# Header size for title, values: h1, h2, ..., h6
DEFAULT_TITLE_HSIZE = 'h1'

# Header size for author
DEFAULT_AUTHOR_HSIZE = 'h2'

# Text added before author name
DEFAULT_AUTHOR_PREFIX = 'Author:'

# Text added after author name
DEFAULT_AUTHOR_SUFFIX = ''

# Header size for paragraph
DEFAULT_PARAGRAPH_HSIZE = 'h2'

# Header size for license
DEFAULT_LICENSE_HSIZE = 'h2'

# Header text for license block
DEFAULT_LICENSE_HEADER = 'License'

# Default for license type
DEFAULT_LICENSE_TYPE = 'MIT'

# Default header for general "Files" block
DEFAULT_FILES_HEADER = 'File Breakdown'

# Default header size for general "Files" block
DEFAULT_FILES_HSIZE = 'h2'

# Header size for displaying path of source code file
DEFAULT_FILEPATH_HSIZE = 'h3'

# Prepend order number before source code file path
USE_NUM_BEFORE_FILEPATH = True

# Whether to skip ".folder" or ".file" while scanning
SKIP_LEADING_DOT_ITEMS_IN_FOLDER = True

# Header for "Params" block inside function prototype
PROTOTYPE_PARAMS_HEADER = 'Params'

# Header for "Returns" block inside function prototype
PROTOTYPE_RETURNS_HEADER = 'Returns'

# Header for "Raises" block inside function prototype
PROTOTYPE_RAISES_HEADER = 'Raises'

# Header size for blocks inside function prototype
PROTOTYPE_PARTS_HSIZE = 'h6'

# Markup parameter name by prepending '@' or not
AT_SIGN_BEFORE_PARAM = True
