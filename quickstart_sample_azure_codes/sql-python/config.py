import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://data-es-jobs.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'ka24eMJnoFy7YV9jhaugR1MfjqhubUAU9EXv8IzQjyQ9nY4HJ7vAe5Cwht3LvGwSB6UcClPRMxmbACDbGeojkg=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}