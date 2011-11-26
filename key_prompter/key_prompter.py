import subprocess
import traceback, sys
from os.path import join

from jca.files import my_paths
from jca.qter.qter_test import *

def check_keys():
  # Check the logged keys.  Display info on interesting keystrokes.
  try:
    try:
      with open('keys.txt') as f:  keys = f.read().strip()
    except IOError: return
    print 'keys: ', keys
    if 'undefined' in keys:  edit.setPlainText('What is undefined?')
    else: edit.setPlainText('')
  except:
    traceback.print_exc()
    sys.exit()

# Check file on a timer. Create edit. Launch.
proc = subprocess.Popen('python -uB "%s"' % 'key_logger.py')
start_if_havent()
t = QTimer()
t.connect(t, SIGNAL("timeout()"), check_keys)
t.start(1000)
edit = QPlainTextEdit()
edit.setWindowTitle('Key Prompter')
edit.show()
launch_if_havent()