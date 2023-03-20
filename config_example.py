import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://data-es-jobs.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'your_account_key'),
}

#put here url host and primary key, then rename it simply to config.py

#config.py is already added to the gitignore to avoid sharing key on github