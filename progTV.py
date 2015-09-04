#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import datetime
import time
import unicodedata
from xml.dom import minidom

# script qui liste les films de science-fiction qui seront diffuses demain sur les chaines que je recois
# 1- recuperer la date de demain
# 2- lire le xml 
# 2-1  comparer a la date du programme
# 2-3 le programme est il de la science-fiction ?
# 2-4 le programme est il diffuse sur les chaines listees ?  Faire la conversion entre IDchaine du programme et IDchaine TV
# 3- envoyer par sms

# debut SMS : FILMS SF 24/08 |
# puis chaine, horaire, titre ex : RTL9 - 23:10 - Star Trek |
def sansaccent(ch, encod='utf-8'):
    """Supprime les accents sans changer la casse (majuscules et minuscules)"""
    conv = False
    if not isinstance(ch, unicode):
        ch = unicode(ch, encod, 'replace')
        conv = True
    alpha1 = u"àÀâÂäÄåÅçÇéÉèÈêÊëËîÎïÏôÔöÖùÙûÛüÜÿŸ"
    alpha2 = u"aAaAaAaAcCeEeEeEeEiIiIoOoOuUuUuUyY"
    x = ""
    for c in ch:
        k = alpha1.find(c)
        if k >= 0:
            x += alpha2[k]
        else:
            x += c
    if conv:
        x = x.encode(encod)
    return x

# -------------
# les variables
# -------------
# pour la recherche dans le xml local
dateCalJour = '15-01'
nomLocal = 'complet.xml'
#dossierLocal = '/media/raid/'
dossierLocal = '/users/nous/'
dossierNomLocal = dossierLocal + nomLocal
titreFilmXML = ''
titreFilm = ''
descProgrTVXML = ''
descProgrTV = ''
position = 0
filmCanal = 0
dateHeureDebut = ''
tempChaineTV1 = 'a'
tempChaineTV2 = 'a'
chaineTV = ''
#  - url et infos pour SMS free
urlSMS ='https://smsapi.free-mobile.fr/sendmsg?'
userSMS = '12345678'
passSMS = 'abcDEFGHIJklmn'
msgSMS = ''

# -------------
# les actions
# -------------
# 1 - definir la chaine de caracteres datedemain pour comparer aux donnees xml
today = datetime.date.today( )
tomorrow = today + datetime.timedelta(days=1)
print (tomorrow)
#emits: 2004-11-17 2004-11-18 2004-11-19
dateCompJour = '20' + time.strftime('%y%m%d', tomorrow)
print (dateCompJour)
# 15-08-17
# 20150902204000

# 2 - recherche dans le xml local
doc = minidom.parse(dossierNomLocal)
items = doc.getElementsByTagName("programme")
for item in items:
	tempDateHeure = item.getAttribute('start')
	tempChaineTV1 = str(item.getAttribute('channel'))
	tempChaineTV2 = tempChaineTV1.strip('.telerama.fr')
	chaineTV = tempChaineTV2.strip('C')
	#IDChaineTV = ChaineTV
	titreFilmXML = item.getElementsByTagName("title")[0]
	titreFilm = titreFilmXML.firstChild.data
	descProgrTVXML = item.getElementsByTagName("category")[1]
	descProgrTV = descProgrTVXML.firstChild.data
	
	position = descProgrTV.find("film de science-fiction")
	if position >= 0:
		dateHeureDebut = tempDateHeure[6:8] + '/' + tempDateHeure[4:6] + ' ' + tempDateHeure[8:10] + ':' + tempDateHeure[10:12]
		print (dateHeureDebut)
		print str(chaineTV)
		print (titreFilm)
#		filmCanal = titreFilm.find('Canal')
#		if filmCanal < 0:
			#print(titreFilm)
#			msgSMS = msgSMS + ' -- ' + titreFilm

#msgSMS = sansaccent(msgSMS)
#msgSMS = msgSMS.replace(' | ', '-')
#msgSMS = msgSMS.replace('--', '|')

# 3 - envoyer par SMS
urlallSMS = urlSMS + 'user=' + userSMS + '&pass=' + passSMS + '&msg=' + msgSMS
# print (msgSMS)
#print (urlallSMS)
#request = urllib2.urlopen(urlallSMS)
#request.close
