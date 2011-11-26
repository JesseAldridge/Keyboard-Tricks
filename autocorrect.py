import subprocess
import threading, re

import pyHook
import pythoncom
import enchant
d = enchant.Dict("en_US")

# Store typed keys.  Set correct timer.
def on_key_down(e):
  if e.Key == 'Back':  v.keys = v.keys[:-1]
  elif e.Key == 'Space':  v.keys += ' '
  elif 'shift' in e.Key or 'control' in e.Key:  return True
  elif e.Key in ['Home', 'Left', 'Up', 'Right', 'Down', 'End', 'Return']:
    v.keys = ''
  elif e.Ascii >= 32 and e.Ascii <= 126:  v.keys += chr(e.Ascii)
  else:  print 'key: ', e.Key
  if v.t:  v.t.cancel()
  v.t = threading.Timer(1, correct_words)
  v.t.start()
  v.prev_key = e.Key
  return True
  
# Unhook.  Spell check the word.  Erase and retype.  Rehook.
def correct_words():
  if not v.keys.strip():  return
  v.should_pump = False
  new_str = ''
  non_letters = '(\W+)'
  for word in re.split(non_letters, v.keys):
    if not word:  continue
    if not re.match(non_letters, word):
      if not spell_check.check(word):  word = spell_check.suggest(word)[0]
    new_str += word
  subprocess.Popen('pythonw -m SendKeys -p0 "{BS %i}%s"' % (
    len(v.keys), new_str.replace(' ', '{SPACE}'))).communicate()
  v.keys = ''
  v.should_pump = True

# Listen to keys.
class v:
  keys = ''
  t = None
  should_pump = True
  prev_key = None
spell_check = enchant.Dict("en_US")
hm = pyHook.HookManager()
hm.KeyDown = on_key_down
hm.HookKeyboard()

pythoncom.PumpMessages()