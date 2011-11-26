
import sys, traceback

import pyHook, pythoncom

from jca.misc.timestamp import timestamp

' Note:  This does not work well with a gui app.  Use as an external binary. '

# Write events to passed file.  Mouse move and F5 are special case.
if len(sys.argv) > 1:  log_path = sys.argv[1]
else:  log_path = 'key_log_%s.txt' % timestamp()
out = open(log_path, 'w')
std_attrs = ['MessageName', 'Message', 'Time', 'Window', 'WindowName']
key_seq = u''
def info_handler(attrs):
  def event_info(e):
    try:
      if e.MessageName == 'mouse move':  return True
      if len(key_seq) > 100: key_seq = key_seq[10:]
      key_seq += unicode(chr(e.Ascii))
      for s in std_attrs + attrs:
        out.write('%s: %s\n' % (s, getattr(e, s)))
      out.write('\n')
      return True
    except:
      traceback.print_exc()
      sys.exit()
  return event_info
  
# Hook mouse and keyboard.  Start listening.
hm = pyHook.HookManager()
hm.MouseAll = info_handler(['Position', 'Wheel', 'Injected'])
hm.KeyDown = info_handler(['Ascii', 'Key', 'KeyID', 'ScanCode', 'Extended',
               'Injected', 'Alt', 'Transition'])
hm.HookKeyboard()
pythoncom.PumpMessages()