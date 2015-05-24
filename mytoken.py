#!/usr/bin/env python
# -*- coding: utf-8  -*-
# TODO:
# Add button to copy to clipboard

import pygtk
pygtk.require('2.0')
import gtk
import time
import sys
import datetime
import pyotp
totp = pyotp.TOTP("$mysecret")

class Token:

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("MyToken")
        self.label = gtk.Label()
        window.add(self.label)
        window.set_border_width(25)
        window.show_all ()
    
    def update(self):
	currentotp =  str(totp.now()).zfill(6)
	seconds=30 - (int(datetime.datetime.now().strftime('%S')) % 30)
        self.label.set_text("Token : " + currentotp + " Remaining seconds " + str(seconds))
        return True  #needed to keep the update method in the schedule

def main():
    gtk.main()

if __name__ == "__main__":
    token = Token()
    gtk.timeout_add(200, token.update)  #add to the main loop scheduled tasks
    main()
