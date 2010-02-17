# coding=utf-8
import sys
import socket
import string
import signal

#import b

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
NICK="stolpen_kok"
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

#game = b.B()
print "Main loop..."
while True:
    buffer += s.recv(2048)
    lines = buffer.split("\n")
    buffer = lines.pop()
    for line in lines:
        print line
        if line.find("PING") != -1:
            s.send("PONG %s\r\n" % line.split()[1])
            if not joined:
                s.send("JOIN %s\r\n" % CHANNEL)
                joined = True

s.close()

