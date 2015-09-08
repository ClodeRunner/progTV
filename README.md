progTV
======

Ce script est mon premier essai en python. Je voulais etre averti des films de science-fiction qui passent sur les chaines tv que je recois:

0. Le script [progTV_Download.py](progTV_Download.py) telecharge sur http://xmltv.dtdns.net/download/ les programmes de 190 chaines sur 12 jours.
0. Le script [progTV.py](progTV.py) analyse le fichier telecharge 
0. La recherche est envoyee par SMS avec l'API de Free mobile 


Installation
-----------

modifier les variables
Pour l'envoi du SMS par Free :
```
userSMS = '12345678'
passSMS = 'abcDEFGHIJklmn'
```

Pour l'emplacement ou stocker les fichiers
```
dossierLocal = '/users/progTV/'
```

La recherche
```
prgTVrecherche = "film de science-fiction"
```


Usage
-----

```
python ./progTV.py

```
J'utilise ensuite les taches CRON pour lancer tous les jours

Licence
-------
Servez-vous ware. Il faut que je me penche sur les licenses pour proposer la bonne.
