import sys
import os
import imp

colorModule = imp.load_source('', sys.argv[1])

f = open("/tmp/colornotify.fifo")

while True:
    data = f.read().rstrip()
    if not data or not data.isdigit():
        continue
    m = colorModule.MailNotifier()
    m.setColor(int(data))
