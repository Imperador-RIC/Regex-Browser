# -*- coding: utf-8 -*-

"""This module is the core of the Regex Browser, responsible for making queries and ensuring the proper functioning of the program"""

import re
from typing import Union
from os import system, name

from selenium import webdriver
from selenium.webdriver.edge.options import Options

# The numerical value below defines the time the program should wait while executing JavaScript code before the next step
# Higher values tend to ensure better functioning

time = 5

def clear ():
    """Runs a command in the system shell to clear the screen"""

    if name == 'nt':
        system ('cls')

    else:
        system ('clear')

def query (target: str, regex: str, cli_mode: bool = True) -> Union [list, str]:

    """This function receives the target URL and the REGEX CODE that will be used in the query

        Receive:
            target: string containing the URL to be queried
            regex: string with the REGEX CODE that will be used in the query
            cli_mode: Boolean value indicating whether or not the program is running directly from the command line, if so, a small filtering will be done on the target URL and on the REGEX CODE

        Returns:
            list: if the query is successful, a list with the result is returned
            str: if an error occurs, a string saying the error is returned
    """

    if cli_mode:
        target = target.strip ('"')
        regex = regex.strip ('"')

    if re.match (r'^(https?://)?([\w.-]+)\.([\w.-]+)(/[^\s]*)?$', target):

        if not target.startswith ('http://') and not target.startswith ('https://'):
            target = 'http://' + target

        try:

            options = Options ()
            options.add_argument ('--headless')
            driver = webdriver.Edge (options = options) 

            driver.get (target)
            driver.implicitly_wait (time)

            result = re.findall (regex, driver.page_source)

            if result != [] and result != None:
                clear ()
                return result

            else:
                clear ()
                return 'No results were found'

        except:
            clear ()
            return 'An error occurs while executing the query'

    else:
        clear ()
        return 'Please enter a valid URL'

def interactive () -> Union [list, str]:
    """Prompts the user to enter the target URL and the REGEX CODE of the query, then calls the query function passing as arguments the data that was written by the user"""

    target = str (input ('Enter your target URL: '))
    regex = str (input ('Enter the REGEX CODE you want to use in your query: '))

    print (query (target, regex, False))
