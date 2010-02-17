# -*- coding: utf-8 -*-

'''
@author: han som inte får commita
'''

import sqlite3

class Stats(object):
    """
    Lögn, förbannad lögn och statistik. 100.000 fler sysselsatta idag, sade statsminister Fredrik Reinfeldt i partiledardebatten i Agenda igår.
    """
    def __init__(self):
        self.database = Database("stats.db")
        #self.database.createTables()

    def addWin(self,nick):
        #Ökar vinstsaldot för ett nick med 1
        self.database.addWin(nick)
    
    def getTopTen(self):
        #Returnerar topp tio-lista
        topTen = self.database.getTopTen()
        topList = "Nick\t\t\tWins"

        for player in topTen:
            topList += "\n" + player[0] + "\t\t\t" + str(player[1])

        return topList

class Database():
    """
    Interface mot (t.ex.) SQLite-database
    """

    def __init__(self, dbfile):
        #Initerar databasanslutning
        self.dbfile = dbfile
        self.conn = sqlite3.connect(dbfile)

    def createTables(self):
        #Skapar statistiktabell(er)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE stats (nick text, wins int)''')
        self.conn.commit()
        c.close()

    def addWin(self,nick):
        #Ökar en användares vinstsaldo i databasen med 1
        c = self.conn.cursor()
        t = (nick,)
        c.execute('SELECT * FROM stats WHERE nick=?',t)

        numrows = 0

        for row in c:
            numrows += 1

        if numrows == 1:
            c.execute('UPDATE stats SET wins = wins + 1 WHERE nick = ?',t)
        elif numrows == 0:
            c.execute('INSERT INTO stats VALUES (?,1)',t)

        self.conn.commit()

    def getTopTen(self):
        #Hämtar tio i topp-lista från databasen
        topTen = []
        c = self.conn.cursor()
        c.execute('SELECT * FROM stats ORDER BY wins DESC LIMIT 10')

        for row in c:
            topTen.append(row)

        return topTen


#Test code
"""
stats = Stats()
stats.addWin('sebbz')
stats.addWin('grul')
stats.addWin('igno')
print stats.getTopTen()
"""
