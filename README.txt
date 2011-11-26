
This is an unorganized pile of code dealing with hooking the keyboard, sending
keystrokes and stuff like that.  It's a collection of a few experiments from
over the years.  Some of the code might work, most of it probably doesn't.
I'm only posting this cuz somebody e-mailed me about [this question](http://stackoverflow.com/questions/5851942/getting-pyhook-and-sendkeys-to-work-together?answertab=active#tab-top) and I thought I might as well dump my
collection on GitHub.

I think I concluded the easiest approach was to invoke an external exe from a
Python script with subprocess.  I used the SendKeys program, which I think is
Windows only.