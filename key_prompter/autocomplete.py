
import traceback, sys, threading

import pyHook, pythoncom

def on_key(e):
  unicode(chr(e.Ascii))
  if len(v.key_seq) > 100: v.key_seq = v.key_seq[10:]
    v.key_seq += unicode(chr(e.Ascii))
  if v.key_seq.endswith('for'):
    display_autocomplete_options()
hm = pyHook.HookManager()
hm.KeyDown = on_key
hm.HookKeyboard()
pythoncom.PumpMessages()
