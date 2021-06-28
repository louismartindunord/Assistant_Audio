from bs4 import BeautifulSoup
import requests
import pandas as pd 
import os

url = 'https://www.topito.com/top-meilleures-blagues-16h16-la-fin-dune-epoque'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify)

tableau = soup.find_all(class_="items")
print(tableau)

reponses = []
questions = []
for i in range(len(tableau)):
	question = []
	
	
	for j in tableau[i].find_all('h2'):
		question.append(j.text)
	questions.append(question)
	
	


for i in range(len(tableau)):
	reponse = []
	for f in tableau[i].find_all('p'):
		reponse.append(f.text)
	reponses.append(reponse)
print(reponses)


df_questions = pd.DataFrame(questions)
df_questions = df_questions[::-1]
os.makedirs('blagues', exist_ok=True)
df_questions.to_csv('blagues/questions.csv',index=False)

"""

df_reponses = pd.DataFrame(reponses)
df_reponses.to_csv('blagues/reponses.csv',index=False)

"""
