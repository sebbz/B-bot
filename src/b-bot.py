# coding=utf-8
import sys
import socket
import string
import signal
import time

import b

def signal_handler(signal, frame):
    global s
    print """
############
TERMINATING
############"""
    s.close()
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

buffer = ""

HOST="irc.se.quakenet.org"
PORT=6667
<<<<<<< HEAD:src/b-bot.py
NICK="klevert_brule"
=======
NICK="TALKSHOWHOST"
>>>>>>> 2565ebb3bf068552764ea7798d7a08c330703d4c:src/b-bot.py
IDENT="b-boten"
REALNAME="b botson"
OWNER="grul"
CHANNEL="#b-game"

s=socket.socket()
print "Connecting..."
s.connect((HOST, PORT))
print "Sending NICK..."
s.send("NICK %s\r\n" % NICK)
print "Sending USER..."
s.send("USER %s %s %s :%s\r\n" % (IDENT, IDENT, IDENT, REALNAME))

joined = False
pings = 0

game = b.B()

print "Main loop..."
while True:
    buffer += s.recv(2048)
    lines = buffer.split("\n")
    buffer = lines.pop()
    for line in lines:
        print line
	
	if str.find(line, "Register first") > 0:
		joined = False

        if line.find("PING") != -1:
            pings += 1
            s.send("PONG %s\r\n" % line.split()[1])
            if pings == 2:
                s.send("JOIN %s\r\n" % CHANNEL)
        if line.find("PRIVMSG") != -1:
            print line

s.close()

