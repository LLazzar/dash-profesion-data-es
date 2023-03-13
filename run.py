from azure.cosmos import exceptions, CosmosClient, PartitionKey
import config
import datetime

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

client = CosmosClient(HOST, credential=MASTER_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

# one data structure example
item = {"id": "1", "name": "John", "age": 30}

container.create_item(body=item) #add
container.delete_item(item="1",partition_key="1") #delete

# a datastructure like we will need

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")

job_count_sample_entry = {
    "id": date_string,
    "data_engineer": 40,
    "data_science": 30,
    "data_analyst": 50,
    "business_analyst": 60,
    "area": "Barcelona" 
    }

container.create_item(body=job_count_sample_entry)
container.delete_item(item="2023-03-13",partition_key="2023-03-13") #delete