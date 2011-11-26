
from os.path import exists, join
import os, threading

from jca.qter.qter_test import *
from jca.qter.core.link_browser import LinkBrowser
from jca.files.all_files.all_files import all_files
from jca.files import my_paths

import pyHook
import pythoncom

class v:
  keys_pressed = []
  searching = False

def save(word1, word2):
  Write word1, word2
  We want to know likelihood of word2 coming after word1
  
def info_handler(attrs):
  def event_info(e):
    if e.MessageName == 'key down':
      v.keys_pressed.append(e.Key)
      limit = 100
      if len(v.keys_pressed) > limit:  
        v.keys_pressed = v.keys_pressed[-limit:]
      curr_word = ''
      for ch in v.keys_pressed[::-1]:
        if ch == 'Space':
          if word_before:
            store_word(word_before, curr_word)
          word_before = curr_word
        curr_word = ch + word
    return True
  return event_info

def search(text):
  v.searching = True
  link_browser.setPlainText('')
  for path in all_files(my_paths.jca, pattern='*.py', ignore_dirs=True, 
              recursive=True):
    with open(path) as file:
      if text.lower() in unicode(file.read().lower(), 
                     'ascii', 'replace'):
        link_browser.add_line('"%s"' % path)
  link_browser.repaint()
  v.searching = False
 
start_if_havent()
hm = pyHook.HookManager()
hm.KeyDown = info_handler(['Ascii', 'Key', 'KeyID', 'ScanCode', 'Extended',
               'Injected', 'Alt', 'Transition'])
hm.HookKeyboard()

t = threading.Thread(target=pythoncom.PumpMessages, args=[], kwargs={})
t.start()

link_browser = LinkBrowser()
link_browser.show()
launch_if_havent()