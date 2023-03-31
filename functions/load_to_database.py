from azure.cosmos import exceptions, CosmosClient, PartitionKey
from config import config


def uploadDict (pythondict, container_name):
    HOST = config.settings['host']
    MASTER_KEY = config.settings['master_key']
    client = CosmosClient(HOST, credential=MASTER_KEY)
    database = client.get_database_client('data-es-job')
    container = database.get_container_client(container_name)
    container.create_item(body=pythondict)
    return

######################################################
# a datastructure like we will need

#now = datetime.datetime.now()
#date_string = now.strftime("%Y-%m-%d")

#pythondict = {
#    "id": date_string,
#    "data_engineer": 40,
#    "data_science": 30,
#    "data_analyst": 50,
#    "business_analyst": 60,
#    "area": "Barcelona" 
#    }

#container.create_item(body=salary_sample)
#container.delete_item(item="2023-03-17", partition_key="2023-03-17") #delete #partion key is sam eof id?

#################################################################

