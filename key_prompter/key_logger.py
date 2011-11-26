
import traceback, sys, threading

import pyHook, pythoncom, win32gui

# Write recent keys to file.  Use timer to avoid writing to frequently.
def event_info(e):
  try:
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    if not title.endswith('- Google Chrome'):
      return 1
    if len(v.key_seq) > 100: v.key_seq = v.key_seq[10:]
    v.key_seq += unicode(chr(e.Ascii))
    if not v.timer:
      v.timer = threading.Timer(1, write_keys)
      v.timer.start()
  except:
    " Because otherwise we won't see errors. "
    print 'Error, quitting'
    traceback.print_exc()
    sys.exit()
def write_keys():
  print 'writing keys'
  with open('keys.txt', 'w') as f:  f.write(v.key_seq)
  v.timer = None

# Hook keyboard.
class v:
  key_seq = u''
  timer = None
hm = pyHook.HookManager()
hm.KeyDown = event_info
hm.HookKeyboard()
pythoncom.PumpMessages()
' Note:  This does not work well with a gui app.  Use as an external binary. '