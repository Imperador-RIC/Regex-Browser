# -*- coding: utf-8 -*-

"""This module is a graphical interface for the program, using the engine for its internal operation"""

import modules.engine

from pyperclip import copy

from tkinter import *
from tkinter import scrolledtext

class Application (Tk):

    def __init__ (self):

        Tk.__init__ (self)

        # Variables for styling the graphical interface, they define the color of the frames, background, text font, among other things

        self.background = '#2c2c2c'

        self.bg = '#565656'
        self.bd = 4

        self.highlightbackground = '#000000'
        self.highlightthickness = 2

        self.fg = '#ffffff'
        self.font = ('Arial', 16, 'bold')

        self.default_result = 'Welcome to Regex Browser, perform your searches on web pages using regex code'
        self.result = self.default_result

        # Calling the methods to form the graphical interface, then starting it

        self.Screen ()
        self.Frame ()

        self.Widget ()
        self.Label ()
        self.Entry ()
        self.Button ()

        self.mainloop ()

    def Screen (self) -> None:
        """Method for creating and configuring the program window"""

        self.title ('Regex Browser')
        self.iconbitmap ('image/icon.ico')

        self.configure (background = self.background)

        # Modify the parameters below if you need to run the program on different screens, with different resolutions and sizes
        self.geometry ('600x600+100+100') # Sets the initial program size and opening position
        #self.maxsize (width = 600, height = 600)
        #self.minsize (width = 600, height = 600)

        self.attributes ('-fullscreen', False)
        self.resizable (False, False)
        self.state ('normal')

    def Create_Frame (self) -> Frame:
        """Method for creating frames"""

        return Frame (bd = self.bd, bg = self.bg, highlightbackground = self.highlightbackground, highlightthickness = self.highlightthickness)

    def Frame (self) -> None:
        """Method for configuring the frames"""

        self.frame_main = self.Create_Frame ()
        self.frame_main.place (relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.38)

        self.frame_result = self.Create_Frame ()
        self.frame_result.place (relx = 0.01, rely = 0.41, relwidth = 0.98, relheight = 0.58)

    def Widget (self) -> None:
        """Method for creating and configuring the widget which displays query results"""

        self.widget = scrolledtext.ScrolledText (self.frame_result, wrap = WORD, yscrollcommand = set, font = ('Courier New', 14, 'bold'))
        self.widget.pack (fill = BOTH, expand = True)

        self.widget.config (state = 'normal')
        self.widget.insert (END, self.result)
        self.widget.config (state = 'disabled')

    def Creater_Label (self, frame, text) -> Label:
        """Method for creating labels"""

        return Label (frame, bg = self.bg, fg = self.fg, font = self.font, text = text)

    def Label (self) -> None:
        """Method for configuring labels"""

        self.label_target = self.Creater_Label (self.frame_main, text = 'Enter the URL of your target:')
        self.label_target.place (relx = 0.01, rely = 0.01)

        self.label_regex = self.Creater_Label (self.frame_main, text = 'Enter the REGEX CODE you want to query:')
        self.label_regex.place (relx = 0.01, rely = 0.3)

    def Entry (self) -> None:
        """Method for creating and assembling text entries"""

        self.entry_target = Entry (self.frame_main, font = self.font)
        self.entry_target.place (relx = 0.01, rely = 0.15, relheight = 0.12, relwidth = 0.98)

        self.entry_regex = Entry (self.frame_main, font = self.font)
        self.entry_regex.place (relx = 0.01, rely = 0.44, relheight = 0.12, relwidth = 0.98)

    def Result (self) -> None:
        """Method to refresh display of query result"""

        self.widget.config (state = 'normal')
        self.widget.delete (1.0, END)
        self.widget.insert (END, self.result)
        self.widget.config (state = 'disabled')

    def Clear (self) -> None:
        """Method for cleaning the query result and user inputs"""

        self.entry_target.delete (0, END)
        self.entry_regex.delete (0, END)
        self.result = self.default_result
        self.Result ()

    def Query (self) -> None:
        """Method for carrying out the query"""

        self.result = str (modules.engine.query (self.entry_target.get (), self.entry_regex.get (), False))
        self.Result ()

    def Copy (self) -> None:
        """Method to copy query result to clipboard"""

        copy (self.result)

    def Button (self) -> None:
        """Method for creating and positioning buttons"""

        self.button_clear = Button (self.frame_main, font = self.font, text = 'CLEAR', command = lambda: self.Clear ())
        self.button_clear.place (relx = 0.1, rely = 0.70, relwidth = 0.2, relheight = 0.2)

        self.button_query = Button (self.frame_main, font = self.font, text = 'QUERY', command = lambda: self.Query ())
        self.button_query.place (relx = 0.4, rely = 0.70, relwidth = 0.2, relheight = 0.2)

        self.button_copy = Button (self.frame_main, font = self.font, text = 'COPY', command = lambda: self.Copy ())
        self.button_copy.place (relx = 0.7, rely = 0.70, relwidth = 0.2, relheight = 0.2)
