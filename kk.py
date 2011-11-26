import subprocess
import threading, re

import pyHook
import pythoncom

# Keyboard shortcuts and corresponding full strings
shortcuts = [
['je', 'jessealdridge@gmail.com'],
['div', "<div class='container'>foo</div>"],
['style', '<style> .container{ background-color:#eee; } </style>'],
['script', '<script> </script>'],
['children', "$('.container').children('.node')"],
['console', "console.log('index: ', index)"],
['index', "$(children).index($('.current'))"],
['addclass', "$('.current').addClass('highlight')"],
['for', "for(var i = 0; i < list.length; i++) {"],
['link', "<link rel='stylesheet' type='text/css' href='static/etc/main.css'/>"],
]

# Escape special chars in full strings.
for shcut in shortcuts:
  shcut[1] = re.sub(pattern='({|})', repl=r'{\1}', string=shcut[1])
  escape = '+^%~[]'
  for ch in escape:  
    find = '\\' + ch if ch in '+^[]' else ch
    shcut[1] = re.sub(find, '{%s}' % ch, shcut[1])
  shcut[1] = shcut[1].replace(' ', '{SPACE}')
  shcut[1] = shcut[1].replace('(', '+9').replace(')', '+0')

# Store typed keys.  Set correct timer.
def on_key_down(e):
  if e.Key == 'Back':  v.keys = v.keys[:-1]
  else: v.keys += chr(e.Ascii)
  for shcut in shortcuts:
    if v.keys.endswith('kk' + shcut[0]):
      v.keys = ''
      threading.Thread(target=lambda: send_keys(shcut)).start()
      break
  return True

# Send the shortcut.  Hook the keyboard.
def send_keys(shcut):
  subprocess.Popen('pythonw -m SendKeys -p0 "{BS %i}%s"' % (
    len('kk' + shcut[0]), shcut[1])).communicate()
class v:
  keys = ''
  t = None
hm = pyHook.HookManager()
hm.KeyDown = on_key_down
hm.HookKeyboard()
pythoncom.PumpMessages()