import requests
import pandas as pd
from dotenv import load_dotenv
import os



# Carregar variáveis do arquivo .env
load_dotenv()

base_url = 'https://api.github.com/'
owner = 'amzn'
url = f'{base_url}users/{owner}/repos'
access_token = os.getenv('TOKEN')

headers = {'Authorization':'Bearer ' + access_token,
            'X-GitHub-Api-Version': '2022-11-28'}


#Percorrendo as páginas do repositorio e salvando 
responses = []
for pages in range(1,20):
    #url_page = f'{url}?page={i}'
    responses.append(requests.get(f'{url}?page={pages}',headers=headers).json())
repo_name = []
repo_language = []
for response in responses:    
    for repos in response:
        repo_name.append(repos['name'])
        repo_language.append(repos['language'])

# Criando dataframe e salvando em CSV
repo_df = pd.DataFrame()
repo_df['Name'] = repo_name
repo_df['Linguagem'] = repo_language
repo_df.to_csv('./dados/amazon_api.csv')
