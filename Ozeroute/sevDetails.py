import json
from logging import exception  # For manipulating JSON files
import os  # For manipulating os files and folders
from deep_translator import GoogleTranslator  # For translating
from word2number import w2n  # For converting number words to actual numbers
from dateutil.parser import parse  # For datetime parsing
from Ozeroute.placeDetails import getDetails  # For place details
from datetime import datetime
from voiceSetup import Speaker

def validPassengers(passengerInput):
    
    if passengerInput.isnumeric()  :
        return True
    else:
        return False


def getDate(speaker, qu):
    # Taking the voice input for the date
    depDate = speaker.take_command(qu)

    # Translating the input to english for the date parser
    if speaker.lang == "fr":
        depDate = GoogleTranslator(source='auto', target='en').translate(depDate)

    # Using the date parser to get the formatted date and time
    depDate = parse(depDate, fuzzy=True)
    print(depDate)

    dateTime = depDate.strftime("%Y-%m-%d %H:%m")
    print(dateTime)
    return True, dateTime


def getsSeveralDetails(speaker, qu):
    
    # Departure place input to get details
    if speaker.lang == 'en':
        speaker.talk(qu, "insert departure place please!")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérez le lieu de départ s'il vous plait!")

    depPlace = "" 
    
    validPlace = False

    while not validPlace:
        depPlace = speaker.take_command(qu)
        validPlace = getDetails(depPlace)

        if validPlace:
            pass
        else:
            if speaker.lang == 'en':
                speaker.talk(qu, "Please provide a valid departure place!")
            elif speaker.lang == 'fr':
                speaker.talk(qu, "Veuillez indiquer un lieu de départ valide!")

    f = open("placeDetails.json", "r")
    pDet = json.load(f)

   

    # Filling the departure details
    depDet = {
        "address":pDet["idFetch"]["description"],
        "lat":pDet["coordsFetch"]["result"]["geometry"]["location"]["lat"],
        "lng":pDet["coordsFetch"]["result"]["geometry"]["location"]["lng"]
          
        }
    print(depDet)
    f.close()
    os.remove("placeDetails.json")


    # Destination place input to get details
    if speaker.lang == 'en':
        speaker.talk(qu, "insert destination place please!")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérer le lieu de destination s'il vous plait!")

    destPlace = ""
    validPlace = False
        
    while not validPlace:
        destPlace = speaker.take_command(qu)

        validPlace = getDetails(destPlace)
        
        if validPlace:
            pass
        else:
            if speaker.lang == 'en':
                speaker.talk(qu, "Please provide a valid destination place!")
            elif speaker.lang == 'fr':
                speaker.talk(qu, "Veuillez fournir un lieu de destination valide!")

    f = open("placeDetails.json", "r")
    pDet = json.load(f)

    # Getting the code of the destination place
    if pDet["coordsFetch"]["result"]["place_codes"]["code"]:
        dest_code = pDet["coordsFetch"]["result"]["place_codes"]["code"]
    else:
        dest_code = ""

    # Filling the departure details
    arrDet = {
            "address":pDet["idFetch"]["description"],
            "lat":pDet["coordsFetch"]["result"]["geometry"]["location"]["lat"],
            "lng":pDet["coordsFetch"]["result"]["geometry"]["location"]["lng"],
            "cp":pDet["coordsFetch"]["postal_code"]
        }
    print(arrDet)
    f.close()
    os.remove("placeDetails.json")


    # Filling the departure date
    if speaker.lang == 'en':
        speaker.talk(qu, "insert date and time of departure please!")
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérez la date et l'heure de départ s'il vous plait!")


    while True:
        try:

            validDate, dateTime = getDate(speaker, qu)
            if validDate == False:
                raise Exception
            break
        except Exception as e:
            
            if speaker.lang == 'en':
                speaker.talk(qu, "Insert a valid date please!")
            elif speaker.lang == 'fr':
                speaker.talk(qu, "Insérez une date valide s'il vous plait!")

    

    # input the passengers


    if speaker.lang == 'en':
        speaker.talk(qu, "insert number of passengers adult please! ")
        nbadult = speaker.take_command(qu)
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérez le nombre des adultes s'il vous plait! " )
        nbadult = speaker.take_command(qu)

    while not validPassengers(nbadult):
        if speaker.lang == 'en':
            speaker.talk(qu, "insert number of passengers adult please! ")
            nbadult = speaker.take_command(qu)
            
        elif speaker.lang == 'fr':
            speaker.talk(qu, "insérez le nombre des adultes s'il vous plait! " )
            nbadult = speaker.take_command(qu)
    nbad=int(nbadult)       
    
    if speaker.lang == 'en':
        speaker.talk(qu, "insert number of passengers child please! ")
        nbenfant = speaker.take_command(qu)
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérez le nombre des enfants s'il vous plait! " )
        nbenfant = speaker.take_command(qu)


    while not validPassengers(nbenfant):
        if speaker.lang == 'en':
            speaker.talk(qu, "insert number of passengers child please! ")
            nbenfant = speaker.take_command(qu)
            
        elif speaker.lang == 'fr':
            speaker.talk(qu, "insérez le nombre des enfants s'il vous plait! " )
            nbenfant = speaker.take_command(qu)

    nben=int(nbenfant)       

    if speaker.lang == 'en':
        speaker.talk(qu, "insert number of passengers baby please! ")
        nbbyby = speaker.take_command(qu)
    elif speaker.lang == 'fr':
        speaker.talk(qu, "insérez le nombre des bébés s'il vous plait! " )
        nbbyby = speaker.take_command(qu)
    while not validPassengers(nbbyby):
        if speaker.lang == 'en':
            speaker.talk(qu, "insert number of passengers baby please! ")
            nbbyby = speaker.take_command(qu)
            
        elif speaker.lang == 'fr':
            speaker.talk(qu, "insérez le nombre des bébés s'il vous plait! " )
            nbbyby = speaker.take_command(qu)

    nbby=int(nbbyby) 

    return nbad, nben, nbby , depDet ,dateTime, arrDet
    