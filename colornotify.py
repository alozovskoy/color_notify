import sys
import os
import imp
import subprocess


colorModule = imp.load_source('', sys.argv[1])
fifoFileName = '/tmp/colornotify.fifo'

if not os.path.exists(fifoFileName):
    os.umask(000)
    os.mkfifo(fifoFileName, 0666)

fifo = open(fifoFileName)

while True:
    data = fifo.read().rstrip()
    if not data or not data.isdigit():
        continue
    notifier = colorModule.MailNotifier()
    notifier.setColor(int(data))
