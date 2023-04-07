import json
from voiceSetup import Speaker
from queue import Queue
from questions import q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,serv_q1,serv_q2,serv_q3,serv_q4,avant_ques0,avant_ques1,t_ques0,t_ques1,t_ques2,t_ques3,t_ques4,t_ques5,com_ques0,com_ques1,com_ques2,com_ques3,com_ques4, cond_ques0,cond_ques1,cond_ques2, ret_ques0,ret_ques1,ret_ques2,ret_ques3, lieu_ques0,lieu_ques1,lieu_ques2,lieu_ques3,lieu_ques4,lieu_ques5, att_ques0,att_ques1 , bag_ques0,bag_ques1,bag_ques2,bag_ques3,bag_ques4 , ft_ques0,ft_ques1,ft_ques2,ft_ques3
r1=["à propos des services","à propos de service","questions à propos des services","question à propos des services"]

def tnsf(speaker , qu):
    def cdg(speaker , qu):
        reponse=[]
        for i in my_data["transfert"]["cdg"]:
            speaker.talk(qu, i)
        for i in my_data["transfert"]["cdg"].values():
            reponse.append(i)
        
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)

            if ques.lower() in q1: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in q2: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in q3: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in q4: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")           
    def orly(speaker , qu):
        reponse=[]
        for i in my_data["transfert"]["orly"]:
            speaker.talk(qu, i)
    
        for i in my_data["transfert"]["orly"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
    
            if ques.lower() in q5: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in q6: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in q7: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in q8: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")
    def beauvais(speaker , qu):
        reponse=[]
        for i in my_data["transfert"]["beauvais"]:
                    speaker.talk(qu, i)
            
        for i in my_data["transfert"]["beauvais"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
    
            if ques.lower() in q9: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in q10: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in q11: 
                valid_res=True
                speaker.talk(qu, reponse[2])

            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")
    def disneyland(speaker , qu):
        reponse=[]
        for i in my_data["transfert"]["disneyland"]:
                    speaker.talk(qu, i)

            
        for i in my_data["transfert"]["disneyland"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
    
            if ques.lower() in q12: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in q13: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in q14: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in q15: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")


    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Des questions concernant l’aéroport de Charles de Gaulle (CDG) , Orly , Beauvais ou Disneyland")
        speaker.talk(qu, "Que voulez-vous?")

        
        valid_ques =False
        while not valid_ques :
            trf = speaker.take_command(qu)
            if trf.lower() in ["cdg","charles de gaulle","l'aéroport de charles de gaulle","aéroport de charles de gaulle","aéroport charles de gaulle","aéroport cdg","aéroport de cdg"]:  
                valid_ques =True
                cdg(speaker , qu)
            elif trf.lower() in ["orly","aéroport paris Orly","aéroport Orly","l'aéroport Orly","paris orly","aéroport de paris Orly","aéroport d'Orly","l'aéroport de paris Orly"]:  
                valid_ques =True
                orly(speaker , qu)
            elif trf.lower() in ["beauvais","l'aéroport Beauvais","l'aéroport de beauvais","aéroport beauvais","paris beauvais"]:  
                valid_ques =True
                beauvais(speaker , qu)
            elif trf.lower() in "disneyland":  
                valid_ques =True
                disneyland(speaker , qu)
            else:
                valid_ques=False
                speaker.talk(qu,"Insérez un choix valide s'il vous plait!")

            

def reserv(speaker , qu):

    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Des questions à propos de la réservation des services")
        reponse=[]
        for i in my_data["reservation"]:
            speaker.talk(qu, i)
        
        for i in my_data["reservation"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if ques.lower() in q16: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in q17: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in q18: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in q19: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            elif ques.lower() in q20: 
                valid_res=True
                speaker.talk(qu, reponse[4])
            elif ques.lower() in q21: 
                valid_res=True
                speaker.talk(qu, reponse[5])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def sercices(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions générales à propos des services: ")
        reponse=[]
        for i in my_data["services"]:
            speaker.talk(qu, i)
        
        for i in my_data["services"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if ques.lower() in serv_q1: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in serv_q2: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in serv_q3: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in serv_q4: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")
    
def avantage(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des avantages des services: ")
        reponse=[]
        for i in my_data["avantage"]:
            speaker.talk(qu, i)
        
        for i in my_data["avantage"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if ques.lower() in avant_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            if ques.lower() in avant_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")
    
def tarif(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des tarifs: ")
        reponse=[]
        for i in my_data["tarifs"]:
            speaker.talk(qu, i)
        
        for i in my_data["tarifs"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if ques.lower() in t_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in t_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in t_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in t_ques3: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            elif ques.lower() in t_ques4: 
                valid_res=True
                speaker.talk(qu, reponse[4])
            elif ques.lower() in t_ques5: 
                valid_res=True
                speaker.talk(qu, reponse[5])

            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def commande(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Modification et annulation d’une commande: ")
        reponse=[]
        for i in my_data["commande"]:
            speaker.talk(qu, i)
        
        for i in my_data["commande"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if ques.lower() in com_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in com_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in com_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in com_ques3: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            elif ques.lower() in com_ques4: 
                valid_res=True
                speaker.talk(qu, reponse[4])

            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def retard(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des retards des vols : ")
        reponse=[]
        for i in my_data["retard"]:
            speaker.talk(qu, i)
        
        for i in my_data["retard"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if  ques.lower() in ret_ques0 : 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in ret_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower() in ret_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in ret_ques3: 
                valid_res=True
                speaker.talk(qu, reponse[3])

            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def conducteur(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des informations sur le conducteur : ")
        reponse=[]
        for i in my_data["conducteur"]:
            speaker.talk(qu, i)
        
        for i in my_data["conducteur"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if  ques.lower() in cond_ques0 : 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in cond_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif  ques.lower() in cond_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])

            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def lieux(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des lieux des rendez-vous : ")
        reponse=[]
        for i in my_data["lieux"]:
            speaker.talk(qu, i)
        
        for i in my_data["lieux"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if  ques.lower() in lieu_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in lieu_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif  ques.lower() in lieu_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in lieu_ques3 : 
                valid_res=True
                speaker.talk(qu, reponse[3])
            elif ques.lower() in lieu_ques4: 
                valid_res=True
                speaker.talk(qu, reponse[4])
            elif  ques.lower() in lieu_ques5: 
                valid_res=True
                speaker.talk(qu, reponse[5])
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def attente(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des conditions d’attente du conducteur : ")
        reponse=[]
        for i in my_data["attente"]:
            speaker.talk(qu, i)
        
        for i in my_data["attente"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if  ques.lower() in att_ques0 : 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in att_ques1 : 
                valid_res=True
                speaker.talk(qu, reponse[1])
            
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def bagage(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions à propos des conditions du transport des bagages : ")
        reponse=[]
        for i in my_data["bagages"]:
            speaker.talk(qu, i)
        
        for i in my_data["bagages"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if  ques.lower() in bag_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif ques.lower() in bag_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif ques.lower()in bag_ques2 : 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif ques.lower() in bag_ques3: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            elif ques.lower() in bag_ques4: 
                valid_res=True
                speaker.talk(qu, reponse[4])
            
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def facturation(speaker , qu):
    with open("FAQ.json", 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        speaker.talk(qu, "Questions liées à la Facturation : ")
        reponse=[]
        for i in my_data["facturation"]:
            speaker.talk(qu, i)
        
        for i in my_data["facturation"].values():
            reponse.append(i)
        speaker.talk(qu, "choisissez une question s'il vous plaît !...")
        valid_res=False
        while not valid_res :
            ques = speaker.take_command(qu)
                
            if   ques.lower() in ft_ques0: 
                valid_res=True
                speaker.talk(qu, reponse[0])
            elif  ques.lower() in ft_ques1: 
                valid_res=True
                speaker.talk(qu, reponse[1])
            elif  ques.lower() in ft_ques2: 
                valid_res=True
                speaker.talk(qu, reponse[2])
            elif  ques.lower() in ft_ques3: 
                valid_res=True
                speaker.talk(qu, reponse[3])
            
            else :
                valid_res=False
                speaker.talk(qu,"Insérez une question valide s'il vous plait!")

def faq(speaker , qu):
    speaker.talk(qu, "Questions à propos de: ")
    speaker.talk(qu, " \n - Solutions de transfert aux aéroports \n - Réservation des services \n - à propos des services \n - Avantage des services \n - Questions à propos des tarifs \n - Modification et annulation d’une commande \n - Questions à propos des retards des vols \n - Les informations sur le conducteur \n - Les lieux des rendez-vous \n - Les conditions d’attente du conducteur \n - Condition du transport des bagages \n - Questions liées à la Facturation")

    speaker.talk(qu, "Que voulez-vous?")
    valid_res=False
    while not valid_res :
        type_ques = speaker.take_command(qu)
        if 'solution' in type_ques.lower() :
            valid_res=True
            tnsf(speaker , qu)
        elif 'réservation' in type_ques.lower():
            valid_res=True
            reserv(speaker, qu) 
        elif type_ques.lower() in r1 :
            valid_res=True
            sercices(speaker , qu)
        elif "avantage" in type_ques.lower():
            valid_res=True
            avantage(speaker , qu)
        elif "tarifs" in type_ques.lower() :
            valid_res=True
            tarif(speaker , qu)
        elif "modification" in type_ques.lower() :
            valid_res=True
            commande(speaker , qu)
        elif "retard"  in type_ques.lower() :
            valid_res=True
            retard(speaker , qu)
        elif "conducteur"  in type_ques.lower() :
            valid_res=True
            conducteur(speaker , qu)
        elif "lieux" in type_ques.lower() :
            valid_res=True
            conducteur(speaker , qu)
        elif "attente" in type_ques.lower() :
            valid_res=True
            attente(speaker , qu)        
        elif "bagages"  in type_ques.lower() :
            valid_res=True
            bagage(speaker , qu)
        elif "facturation"  in type_ques.lower() :
            valid_res=True
            facturation(speaker , qu)        
    
        else :
            speaker.talk(qu, "Impossible de reconnaître votre voix, veuillez réessayer...")






