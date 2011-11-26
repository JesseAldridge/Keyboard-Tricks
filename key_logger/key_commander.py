
import sys, traceback

import pyHook, pythoncom

from jca.misc.timestamp import timestamp

# Read commands
class Command:
  def __init__(self, seq, filename):  self.seq, self.filename = seq, filename
with open('commands.txt') as f:  lines = f.read().strip().splitlines()
commands = []
for line in lines:  commands.append(Command(*line.split(' = ')))

# Handle key events, build string of recent keys.
def info_handler():
  def event_info(e):
    try:
      if len(v.key_seq) > 100: v.key_seq = v.key_seq[10:]
      v.key_seq += unicode(chr(e.Ascii))
      if '@' in v.key_seq:  after = v.key_seq.rsplit('@', 1)[-1]
      if '.' in after
      for command in commands:
        if v.key_seq.endswith(command.seq):
          subprocess.Popen('python -uB "%s"' % command.)

      return True
    except:
      traceback.print_exc()
      sys.exit()
  return event_info

# Hook keyboard.  Start listening.
class v:  key_seq = u''
hm = pyHook.HookManager()
hm.KeyDown = info_handler()
hm.HookKeyboard()
pythoncom.PumpMessages()
' Note:  This does not work well with a gui app.  Use as an external binary. '