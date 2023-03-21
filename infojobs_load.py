from azure.cosmos import exceptions, CosmosClient, PartitionKey
import config
import datetime

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']

client = CosmosClient(HOST, credential=MASTER_KEY)

database = client.get_database_client('data-es-jobs')
container = database.get_container_client('infojobs_count')

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

container.create_item(body=salary_sample)
container.delete_item(item="2023-03-17", partition_key="2023-03-17") #delete #partion key is sam eof id?


item_id = '<your_item_id>'

# Construct the DELETE query
query = "DELETE FROM c WHERE c.id = @item_id"

# Set the query parameters
query_params = [{'name': '@item_id', 'value': item_id}]

# Execute the query
result = container.query_items(query, parameters=query_params)