# coding=utf-8
import sys
import socket
import string
import signal

def signal_handler(signal, frame)

HOST="irc.se.quakenet.org"
PORT=6667
NICK="stolpen_kok"
IDENT="b-boten"
REALNAME="b botson"
OWNER="grul"
CHANNELINIT="#it05 apknull"
readbuffer=""

u = raw_input("lol")
s=socket.socket()
print "fätta"
s.connect((HOST, PORT))
print "SÄLAS"
s.send("NICK "+NICK+"\r\n")
print "säldahf"
s.send("USER "+IDENT+" "+HOST+" :"+REALNAME+"\r\n")

done = False
while not done:
    line = s.recv(500)
    print line
    a = raw_input("FITTA\n")
    if a == "quit":
        done = True

s.close()

