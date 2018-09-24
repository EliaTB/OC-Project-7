import random

""" Set messages GrandPy randomly uses to answer the user query """



ADRESS_MGS = [
    ">GrandPy : Bien sûr voici l'adresse:",
 	">GrandPy : Si je me souviens bien l'adresse est:",
 	">GrandPy : Il me semble que ça se trouve ici: "
    ]



STORY_MGS = [
    ">GrandPy : Et t'ai je déjà raconté cette histoire ? :\n",
    ">GrandPy : Je me souviens que ....\n",
    ">GrandPy : Si tu as deux minutes , je peux te raconter une petite histoire.. :\n",
    ">GrandPy : Est-ce que tu savais que....\n",
	]


FAILURE_MESSAGES = [
   ">GrandPy : Ça ne me dit rien du tout, fais attention à l'orthographe da la recherche",
   ">GrandPy : je n'ai pas de connaissance à ce sujet-là, fais attention à l'orthographe recherche"
    ]



def return_failure():
	message = random.choice(FAILURE_MESSAGES)
	return message

def return_address(address):
	random_msg = random.choice(ADRESS_MGS)
	message = random_msg + "  -" + address
	return message

def return_story(summary):
	random_msg = random.choice(STORY_MGS)
	message = random_msg + summary
	return message



