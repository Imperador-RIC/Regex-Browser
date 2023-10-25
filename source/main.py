# -*- coding: utf-8 -*-

import modules.engine, modules.interface

from sys import argv

try:

    if argv [1].upper () == '--INT':
        modules.engine.interactive ()

    elif argv [1].upper () == '--GUI':
        modules.interface.Application ()

    else:
        target = str (argv [1])
        regex = str (argv [2])

        print (modules.engine.query (target, regex))

except (IndexError):

    print ("""
Regex Browser

Syntax example:
python main.py ["TARGET"] ["REGEX"]

Example of use:
python main.py "https://www.website.com" "\d{3}-\d{3}-\d{4}"

Use interactive mode:
python main.py --int

Use graphics mode:
pythonw main.py --gui
""")

    exit ()
