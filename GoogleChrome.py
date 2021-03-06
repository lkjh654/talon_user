from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer

# It is recommended to use this script in tandem with Vimium, a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/


websites = {
    'test': 'test',
    'facebook': 'facebook.com',
    'twitter': 'twitter.com',
    'trello': 'trello.com',
    'gmail': 'gmail.com',
    'get hub': 'github.com',
}

context = Context('GoogleChrome', bundle='com.google.Chrome')

context.set_list('websites', websites.keys())

def open_website(m):
    name = str(m._words[1])
    print(name)
    w = websites.get(name)
    print(w)
    press('cmd-t')
    Str(w)(None)
    press('enter')

keymaps = {
  'back': Key('cmd-['),
  'forward': Key('cmd-]'),
  'website {GoogleChrome.websites}': open_website,
}

context.keymap(keymaps)
