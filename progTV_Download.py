#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import zipfile

# script qui telecharge le fichier XML contenant les programmes TV
# variables - les urls et noms pour download
url = 'http://xmltv.dtdns.net/download/'
nomDistant = 'complet.zip'
urlnomDistant = url + nomDistant
nomLocal = 'complet.zip'
#dossierLocal = '/media/raid/'
dossierLocal = '/users/nous/'
dossierNomLocal = dossierLocal + nomLocal

# actions - download puis unzip du fichier
urllib.urlretrieve(urlnomDistant, dossierNomLocal)
with zipfile.ZipFile(dossierNomLocal, "r") as z:
    z.extractall(dossierLocal)
