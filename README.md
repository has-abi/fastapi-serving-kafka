# Decoupled FastAPI serving and downstream processing stack with Apache Kafka - Example.

The project contains 2 microservices: **serving service** and **data service** besides a Kafka cluster, and mongodb database.

**serving service**: Serve a named entity pipline using spacy and produce a prediction event that gets stored in `ner.predictions` Kafka topic.
**data service**: Consume events from Kafka `ner.predictions` topic process them and store the processed predictions in a mongodb database.


## Requirements

- `docker` installed
- `make` installed

## Clone the project

```shell
git clone git@github.com:has-abi/fastapi-serving-kafka.git
```

## Run the stack

To launch the stack you can use the [Makefile](../Makefile) on the root of the repository which define the different
target based on the [docker-compose.yml](../docker-compose.yml):


### Start the stack

To start all services (serving-servince, data-service) with kafka cluster and mongodb:

```shell
make all
```

### Stop the stack

To stop and delete all running services :

```shell
make down
```

Once all services are running you can access serving service on : [http://localhost:8008/api/serving/docs](http://localhost:8008/api/serving/docs)

### Commands to interact with Kafka

First sh into kafka container:

```shell
docker exec -it kafka_container_id sh
```
To show all Kafka topics

```shell
kafka-topics --list --bootstrap-server localhost:29092
```

To show `ner.predictions` kafka topic content

```shell
kafka-console-consumer --bootstrap-server localhost:29092 --topic ner.predictions --from-beginning
```

### Commands to ineract with mongodb using `mongosh`

First access mongodb

```shell
sudo docker exec -it mongo_container_id mongosh admin -u mongo -p mongo
```

Show all databases

```shell
show dbs
```

Switch to `predictionsdb` database

```shell
use predictionsdb
```

Show all documents in `predictions` collection

```shell
db.predictions.find()
```
