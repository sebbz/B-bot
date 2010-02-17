# coding=utf-8
import sys
import socket
import string
import signal

import b

def signal_handler(signal, frame):
    global s
    print "lol"
    s.close()
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)
HOST="irc.se.quakenet.org"
PORT=6667
NICK="stolpen_kok"
IDENT="b-boten"
REALNAME="b botson"
OWNER="grul"
CHANNELINIT="#it05 apknull"
readbuffer=""

s=socket.socket()
s.connect((HOST, PORT))
s.send("NICK "+NICK+"\r\n")
s.send("USER "+IDENT+" "+HOST+" :"+REALNAME+"\r\n")

done = False
while not done:
    line = s.recv(500)
    print line


s.close()

