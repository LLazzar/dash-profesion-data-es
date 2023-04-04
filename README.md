# Aim and Result

This repository has been created with the aim of building a publicly accessible Power BI dashboard to display real-time data (updated daily) about job offers and salaries in the data field. The dashboard will also maintain and display a historical record of this data. The four main job categories analyzed are Data Engineer, Data Scientist, Data Analyst, and Business Analyst.

The live dashboard can be accessed at: https://app.powerbi.com/view?r=eyJrIjoiZDM1Y2MyY2UtOTdkNi00YTZlLWFmMTYtMzY4ZGViN2IxOGVlIiwidCI6Ijc4NDg0MWU1LTAxYjEtNGQ5My04NzczLTUwYzcxYWI4NWMzYiIsImMiOjl9

# Logic

The repo is essentially the deployment package for an Azure Function called `scrape_and_upload_to_db`, which is a serverless service provided by Azure. The function is written in Python and triggered daily by a timer. It scrapes data from glassdoor.es using Beautiful Soup, including the number of job offerings and median salaries for the four main job categories. This data is then uploaded in JSON format to an Azure Cosmos DB NoSQL database with two separate containers. The database is directly accessed by Power BI to create visualizations, and the resulting dashboard is published to the web. The dashboard is set up to refresh daily to sync with the new data that is loaded into the database every day.

# CosmosDb No sql database structure

The daily scraped data is stored in a Cosmos DB NoSQL free tier database offered by Azure. Two containers are defined:

- glassdoor_count: This container stores objects that contain the number of job offerings for various fields in a certain area and on a certain date. The partition key is "area". An example of the structure of the items (JSON) stored is:

```
{
    "id": "2023-03-30",
    "data_engineer": "2573",
    "data_scientist": "738",
    "data_analyst": "1171",
    "business_analyst": "278",
    "area": "España"
}
```

- glassdoor_salary: This container stores objects that contain salary figures, including median, lower quartile, and upper quartile, for a certain job and on a certain date. The partition key is "job". An example of the structure of the items stored is:

```
{
    "id": "2023-04-01",
    "median": 38100, 
    "q1": "32000",
    "q3": "49000",
    "job": "Data Engineer"
}
```

# Folder Structure

- `__pycache__`: Contains cached files for Python.
- `.vscode` : Contains files related to Visual Studio Code settings and configurations about the specific azure function (auto-generated).
- `config` : Contains .py file defining the URI and MASTER_KEY needed to connect to CosmosDB.
- `figure`. Contains a visual cover for the project.
- `functions`: Contains the code for auxillary functions used for scraping, storing, and uploading data to the database, which are called from within the "proper" azure function.
- `scrape_and_upload_to_db` : It is the azure function folder that cointains `__init__.py` with the code that runs daily and its settings .
- `urls` : Contains excel files with the URLs that need to be scraped.
- `.funcignore` : Contains files that should be ignored when deploying the function app.
- `.gitignore` : Contains files that should be ignored by Git.
- `dash-profesion-data-es.code-workspace` : Contains files related to Visual Studio Code workspace settings.
- `host.json`: A global configuration file that specifies settings for the Azure Functions host.
- `local.settings.json` A file that contains local configuration settings for the Azure Functions project (ignored during deployment).
- `powerbi_dashboard.pbix`: Contains the Power BI dashboard created for the project.
- `requirements.txt`: A file that lists the required Python packages and their versions for the Azure Functions project to run. This file is used by Azure Functions to install the required packages when deploying the function app.

# About CosmosDB

Azure Cosmos DB is a distributed NoSQL database system designed for building highly scalable and available cloud applications. In Cosmos DB, data is stored in containers, which are logical units of storage that correspond to a table-like structure. You can create multiple containers within a Cosmos DB database to store different types of data or to partition your data for scalability. Containers in Cosmos DB are schema-agnostic, which means that they don't enforce a fixed schema on the data stored within them. You can store documents with different structures within the same container, and you can change the schema of a container at any time.

However, it's important to note that containers are not equivalent to traditional SQL tables, as they do not enforce a fixed schema or primary key constraints. Instead, Cosmos DB provides a flexible data model that allows you to store and query data in a variety of ways. One of the key features of Cosmos DB is its ability to automatically partition data across multiple physical partitions for high scalability and availability. Partitioning is based on a partition key, which is a value that is specified by the application developer and used to determine which physical partition a document will be stored in. Each partition contains a subset of the documents in the container and is managed independently by Cosmos DB.

When you create a container in Cosmos DB, you must specify a partition key. This key should be chosen carefully based on the access patterns of your application. If your application frequently queries for data based on a certain property, that property would make a good candidate for a partition key. Once you have chosen a partition key, it cannot be modified. This is because changing the partition key would require reorganizing the data in Cosmos DB, which could be a very time-consuming process. Therefore, it's important to carefully choose your partition key upfront.

If you need to change the partition key, you can create a new container with the new partition key and migrate the data from the old container to the new container. This can be done using Cosmos DB's migration tool or by writing your own migration code. Overall, Cosmos DB provides a flexible and scalable solution for storing and querying data in the cloud.

# About Azure Functions

Azure Functions is a serverless compute service that allows you to build event-driven applications in the cloud without having to manage the underlying infrastructure. One of the key features of Azure Functions is the ability to define functions that are triggered by events, such as HTTP requests, messages in a queue, or changes to a database.

The timer trigger function is a type of trigger that allows you to run a function on a schedule. You can specify the schedule using a cron expression, which is a string that defines the frequency of the schedule. When the timer trigger function runs, it passes a context object to the function, which contains information about the trigger and the execution environment.

The timer trigger function is a versatile tool that can be used for a variety of purposes. For example, you could use it to clean up temporary files, send scheduled notifications, or perform periodic data processing tasks. It's a powerful tool for building event-driven applications that need to perform tasks on a regular basis.

Overall, Azure Functions and the timer trigger function provide a flexible and scalable solution for building event-driven applications in the cloud. By leveraging the power of Azure Functions, you can focus on building your application logic without having to worry about managing infrastructure.