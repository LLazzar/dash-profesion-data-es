# dash-profesi-n-data-es
Un repo que construía un panel de control para visualizar la oferta laboral en el ámbito de datos en España.

# notes for explaining

In Azure Cosmos DB, data is stored in containers, which are logical units of storage that correspond to a table-like structure. You can create multiple containers within a Cosmos DB database to store different types of data or to partition your data for scalability. a

Containers in Cosmos DB are schema-agnostic, which means that they don't enforce a fixed schema on the data stored within them. You can store documents with different structures within the same container, and you can change the schema of a container at any time.

However, it's important to note that containers are not equivalent to traditional SQL tables, as they do not enforce a fixed schema or primary key constraints. Instead, Cosmos DB provides a flexible data model that allows you to store and query data in a variety of ways.

So, to answer your question, you can create multiple containers in a Cosmos DB database to organize your data in different ways, but these containers are not equivalent to traditional SQL tables.

Cosmos DB is a distributed NoSQL database system designed for building highly scalable and available cloud applications. The database is organized into containers, which are similar to tables in traditional databases. Within a container, data is stored as JSON documents.

One of the key features of Cosmos DB is its ability to automatically partition data across multiple physical partitions for high scalability and availability. Partitioning is based on a partition key, which is a value that is specified by the application developer and used to determine which physical partition a document will be stored in. Each partition contains a subset of the documents in the container and is managed independently by Cosmos DB.

When you create a container in Cosmos DB, you must specify a partition key. This key should be chosen carefully based on the access patterns of your application. If your application frequently queries for data based on a certain property, that property would make a good candidate for a partition key.

Once you have chosen a partition key, it cannot be modified. This is because changing the partition key would require reorganizing the data in Cosmos DB, which could be a very time-consuming process. Therefore, it's important to carefully choose your partition key upfront.

However, if you need to change the partition key, you can create a new container with the new partition key and migrate the data from the old container to the new container. This can be done using Cosmos DB's migration tool or by writing your own migration code.

I hope this helps! Let me know if you have any more questions.