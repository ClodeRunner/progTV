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
dateCompJour = ''
nomLocal = 'complet.xml'
dossierLocal = '/users/progTV/'
dossierNomLocal = dossierLocal + nomLocal
titreFilmXML = ''
titreFilm = ''
descProgrTVXML = ''
descProgrTV = ''
position = 0
filmCanal = 0
dateDebut = ''
heureDebut = ''
tempChaineTV1 = 'a'
tempChaineTV2 = 'a'
tempDateHeure = ''
IDchaineTV = ''
chainesTV1 = ["TF1","France2","France3","France5","M6","Arte","D8","W9","TMC","NT1","NRJ12","France4","D17","Gulli","AB1","LocIDF","DisneyChannel","FranceO","GameOne","RTL9","SyFy","HD1","6ter","Num23","RMC","Cherie25","Paramount"]
chainesTV2 = ["C1","C2","C3","C5","C6","C7","C8","C9","C10","C11","C12","C13","C17","C18","C23","C40","C73","C119","C121","C199","C201","C4131","C4133","C4134","C4135","C4136","C4141"]
IDlibTV = 0
prgTVrecherche = "film de science-fiction"

#  - url et infos pour SMS free
urlSMS ='https://smsapi.free-mobile.fr/sendmsg?'
userSMS = '12345678'
passSMS = 'abcDEFGHIJklmn'
msgSMS = prgTVrecherche

# -------------
# les actions
# -------------
# 1 - definir la chaine de caracteres date demain pour comparer aux donnees xml
today = datetime.date.today( )
tomorrow = today + datetime.timedelta(days=1)
dateCompJour = tomorrow.strftime('%Y%m%d')

# 2 - recherche dans le xml local
doc = minidom.parse(dossierNomLocal)
items = doc.getElementsByTagName("programme")
for item in items:
	tempDateHeure = item.getAttribute('start')
	tempChaineTV1 = str(item.getAttribute('channel'))
	tempChaineTV2 = tempChaineTV1.strip('.telerama.fr')
	IDchaineTV = tempChaineTV2
	titreFilmXML = item.getElementsByTagName("title")[0]
	titreFilm = titreFilmXML.firstChild.data
	descProgrTVXML = item.getElementsByTagName("category")[1]
	descProgrTV = descProgrTVXML.firstChild.data
	
	position = descProgrTV.find(prgTVrecherche)
	if position >= 0:
		dateDebut = tempDateHeure[0:8]
		if dateCompJour == dateDebut:
			heureDebut = tempDateHeure[8:10] + ':' + tempDateHeure[10:12]
			if IDchaineTV in chainesTV2:
				IDlibTV = chainesTV2.index(IDchaineTV)				
				msgSMS = msgSMS + ' | ' + heureDebut + ' ' + chainesTV1[IDlibTV] + ' ' + titreFilm

msgSMS = sansaccent(msgSMS)

# 3 - envoyer par SMS
urlallSMS = urlSMS + 'user=' + userSMS + '&pass=' + passSMS + '&msg=' + msgSMS
request = urllib2.urlopen(urlallSMS)
request.close
