from fileinput import filename
from unittest import result
import webbrowser

from Ozeroute.sevDetails import getsSeveralDetails
from Ozeroute.usePrivee import getOzerouteOffors
#from Ozeroute.Results import Results
from voiceSetup import Speaker
from datetime import datetime  # For time manipulation
from queue import Queue
import json
#import requests  # For executing requests

def trs_bus(speaker , qu):
    if speaker.lang == 'en':
        speaker.talk(qu, "Welcome to shuttel reservation!")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "Bienvenue sur réservation des bus !")
    nbad, nben, nbby , depDet ,dateTime, arrDet= getsSeveralDetails(speaker, qu)

    if speaker.lang == 'en':
        speaker.talk(qu, "Searching for offers, please wait...")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "En cours de la recherche d'offres, veuillez attendre...")

        
    fileName=getOzerouteOffors(nbad, nben, nbby , depDet ,dateTime, arrDet, speaker , qu)
    if fileName == False:
        if speaker.lang == 'en':
            speaker.talk(qu, "Can't find offers for the desired inputs!")
        elif speaker.lang == 'fr':
            speaker.talk(qu, "Impossible de trouver des offres pour les intrants souhaités!")
    else:
        f=open(fileName,"r")
        resultat=json.load(f) 
        if speaker.lang == 'en':
            speaker.talk(qu, "Showing results...")
            speaker.talk(qu, f"for shuttel there are :")              
            speaker.talk(qu, f"Type: {resultat['shuttel'][0]['vehicle']['type']}.")      
            speaker.talk(qu, f"Total duration: {round(resultat['shuttel'][0]['duration'])} minutes.")
            speaker.talk(qu, f"Departure: {resultat['shuttel'][0]['path']['from']['name']} .")
            speaker.talk(qu, f"Arrival: {resultat['shuttel'][0]['path']['to']['name']} with Code postal: {resultat['shuttel'][0]['path']['to']['address']['cp']}  .")
            speaker.talk(qu, f"With a total price of: {resultat['shuttel'][0]['price']['total']['value']} EUR.")
            speaker.talk(qu, "Change private transfer or proceed this way?")
            way = speaker.take_command(qu)
            if way.lower() in ["change bus","bus","change"]:  
                trs_prv(speaker , qu)
            elif way.lower() in ["proceed","proceed this way","proceed way","way"]:
                url= resultat['shuttel'][0]['vehicle']['image']
                #print(url)
                webbrowser.open(url)
            else :
                speaker.talk(qu,"Unable to Recognize your voice, try Again please...")
        else :
            speaker.talk(qu, "Affichage des résultats...")
            speaker.talk(qu, f"pour les navettes et bus il y a :")
            speaker.talk(qu, f"Type: {resultat['shuttel'][0]['vehicle']['type']}.")                     
            speaker.talk(qu, f"Durée totale: {round(resultat['shuttel'][0]['duration'])} minutes.")
            speaker.talk(qu, f"Départ: {resultat['shuttel'][0]['path']['from']['name']} .")
            speaker.talk(qu, f"Arrivée: {resultat['shuttel'][0]['path']['to']['name']} with Code postal: {resultat['shuttel'][0]['path']['to']['address']['cp']}.")
            speaker.talk(qu, f"Avec un prix total de: {resultat['shuttel'][0]['price']['total']['value']} EUR.")
            speaker.talk(qu, "Changer transfert privé ou poursuivre ce moyen?")
            way = speaker.take_command(qu)
            if way.lower() in ["changer transfert privé","changer transfert prive","changer transfert","changer","change"]:
                trs_prv(speaker , qu)
            elif way.lower() in ["poursuivre","poursuivre ce moyen","ce moyen","moyen"]:
                url= resultat['shuttel'][0]['vehicle']['image']
                print(url)
                webbrowser.open(url)
            else :
                speaker.talk(qu,"Impossible de reconnaître votre voix, réessayez s'il vous plaît...")


def trs_prv(speaker , qu):
    if speaker.lang == 'en':
        speaker.talk(qu, "Welcome to private transfer reservation!")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "Bienvenue sur réservation de transfert privé!")
    nbad, nben, nbby , depDet ,dateTime, arrDet= getsSeveralDetails(speaker, qu)

    if speaker.lang == 'en':
        speaker.talk(qu, "Searching for offers, please wait...")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "En cours de la recherche d'offres, veuillez attendre...")

        
    fileName=getOzerouteOffors(nbad, nben, nbby, depDet ,dateTime, arrDet, speaker , qu)
    if fileName == False:
        if speaker.lang == 'en':
            speaker.talk(qu, "Can't find offers for the desired inputs!")
        elif speaker.lang == 'fr':
            speaker.talk(qu, "Impossible de trouver des offres pour les intrants souhaités!")
    else:
        f=open(fileName,"r")
        resultat=json.load(f) 

        if speaker.lang == 'en':
            speaker.talk(qu, "Showing results...")
            speaker.talk(qu, f"for private transfer there are :")    
            speaker.talk(qu, f"Type: {resultat['vtc'][0]['vehicle']['type']}.")                 
            speaker.talk(qu, f"Total duration: {round(resultat['vtc'][0]['duration'])} minutes.")
            speaker.talk(qu, f"Departure: {resultat['vtc'][0]['path']['from']['name']} .")
            speaker.talk(qu, f"Arrival: {resultat['vtc'][0]['path']['to']['name']} with Code postal: {resultat['vtc'][0]['path']['to']['address']['cp']}  .")
            speaker.talk(qu, f"With a total price of: {resultat['vtc'][0]['price']['total']['value']} EUR.")
            speaker.talk(qu, "Change bus or proceed this way?")
            way = speaker.take_command(qu)
            if way.lower() in ["change bus","bus","change"]:
                trs_bus(speaker , qu)
            elif way.lower() in ["proceed","proceed this way","proceed way","way"]:
                url= resultat['vtc'][0]['vehicle']['image']
                print(url)
                webbrowser.open(url)
            else :
                speaker.talk(qu,"Unable to Recognize your voice, try Again please...")
            
               
        elif  speaker.lang == 'fr':

            speaker.talk(qu, "Affichage des résultats...")
            speaker.talk(qu, f"pour les transferts privés il y a :")    
            speaker.talk(qu, f"Type: {resultat['vtc'][0]['vehicle']['type']}.")                  
            speaker.talk(qu, f"Durée totale: {round(resultat['vtc'][0]['duration'])} minutes.")
            speaker.talk(qu, f"Départ: {resultat['vtc'][0]['path']['from']['name']} .")
            speaker.talk(qu, f"Arrivée: {resultat['vtc'][0]['path']['to']['name']} with Code postal: {resultat['vtc'][0]['path']['to']['address']['cp']}.")
            speaker.talk(qu, f"Avec un prix total de: {resultat['vtc'][0]['price']['total']['value']} EUR.")
            speaker.talk(qu, "Changer bus ou poursuivre ce moyen!")
            
            way = speaker.take_command(qu)
            if way.lower() in ["changer bus","bus","change bus","changer"]:
                trs_bus(speaker , qu)
            elif way.lower() in ["poursuivre","poursuivre ce moyen","ce moyen","moyen"]:
                url= resultat['vtc'][0]['vehicle']['image']
                print(url)
                webbrowser.open(url)
            else :
                speaker.talk(qu,"Impossible de reconnaître votre voix, réessayez s'il vous plaît...")

def getOzeroute(speaker , qu):
    privee = ["transfert privé", "transfert prive", "transfert","privé","prive","private transfer","private","transfer"]
    bus = ["bus", "navette", "bus et navette"]
    

    if speaker.lang == 'en':
        speaker.talk(qu, "Welcome to the ozeroute service, where you can find the best mean of transport to go from point A to point B using different way.")
        speaker.talk(qu, "We offer you these means of transport, please choose one of them: private transfer or bus")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "Bienvenue sur le service ozeroute, où vous pouvez trouver le meilleur moyen de transport pour aller d'un point A à un point B selon différents moyens.")
        speaker.talk(qu, "Nous vous proposons ces moyens de transport, merci d'en choisir un : transfert privé ou bus")
        
    transport = speaker.take_command(qu)

     

    if transport.lower() in privee:
        trs_prv(speaker , qu)
        
    elif transport.lower() in bus:
        trs_bus(speaker , qu)
        
    else :
        if speaker.lang == 'en':
            speaker.talk(qu, "Can't find offers for the desired inputs!")
        elif speaker.lang == 'fr':
            speaker.talk(qu, "Impossible de trouver des offres pour les intrants souhaités!")
           
            

       
       
       
        