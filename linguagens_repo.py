import requests
import pandas as pd


# especificando a versão da API

base_url = 'https://api.github.com/'
owner = 'amzn'
url = f'{base_url}users/{owner}/repos'
#at = 'g
# hp_H
# qAmbZI
# ZTlR0
# dVDY4hcPN
# YI0hBO
# 1=wmf0
# fMxKc'

headers = {'Authorization':'Bearer ' + access_token,
            'X-GitHub-Api-Version': '2022-11-28'}


responses = []

for i in range(1,6):
    #url_page = f'{url}?page={i}'
    responses.append(requests.get(f'{url}?page={i}',headers=headers).json())
repo_name = []
repo_language = []
for i in responses:    
    for ii in i:
        repo_name.append(ii['name'])
        repo_language.append(ii['language'])


repo_df = pd.DataFrame()

repo_df['Name'] = repo_name
repo_df['Linguagem'] = repo_language

repo_df.to_csv('amazon_api.csv')

