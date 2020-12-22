import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twthandle=["LewisHamilton","ValtteriBottas","Max33Verstappen","SChecoPerez","danielricciardo","carlossainz55","alex_albon","Charles_Leclerc","LandoNorris","PierreGASLY","lance_stroll","OconEsteban","kvyatofficial","HulkHulkenberg","Anto_Giovinazzi","GeorgeRussell63","RGrosjean","KevinMagnussen","NicholasLatifi","PiFitti","nikita_mazepin","SchumacherMick","callum_ilott", "MercedesAMGF1","redbullracing","McLarenF1","RacingPointF1","RenaultF1Team","ScuderiaFerrari","AlphaTauriF1","HaasF1Team","WilliamsRacing","alfaromeoracing"]
bio=[]
for i in range(len(twthandle)):
	user = api.get_user(twthandle[i])
	bio.append(user.description)

while(True):
	for i in range(len(twthandle)):
		user = api.get_user(twthandle[i])
		b=user.description
		if(bio[i]!=b):
			msg=f"@{twthandle[i]} changed their Twitter Bio from '{bio[i]}' to '{b}'."
			api.update_status(msg)
			bio[i]=b	
	time.sleep(300000)