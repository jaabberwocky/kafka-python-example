# Simple tutorial in Python for Kafka

Using Java/Scala to work with Kafka is hard (especially for someone like me). *Ta-da!*

## What is Kafka?

Kafka is a distributed messaging system. The architecture is a publish-subscribe model, where **consumers** read messages from **topics** that they have subscribed, where the messages are sent by **producers**. 

Common use-cases: 

- messaging between applications, where you can have applications "talk" to each using messages
- data ETL from source systems to target destinations, thereby processing information on a *streaming* basis, rather than in batches as with your traditional ETL jobs

There is a lot more complexity under the hood, and I suggest you read the [official docs](https://kafka.apache.org/documentation/) for more information.

## Step 1: Download the distribution
Download the 2.0.0 release and un-tar it.
	
> tar -xzf kafka_2.11-2.0.0.tgz
> cd kafka_2.11-2.0.0

Also, install pip requirements by running `pip install -r requirements.txt`

## Step 2: Start the server

Kafka uses ZooKeeper so you need to first start a ZooKeeper server.
	
> bin/zookeeper-server-start.sh config/zookeeper.properties


Now start the Kafka server:
	
> bin/kafka-server-start.sh config/server.properties

## Step 3: Create a topic

Create a topic named "test":
	
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

See list of topics using the following command:

> bin/kafka-topics.sh --list --zookeeper localhost:2181 test

## Step 4: 

In separate command shells, run the following:

1. `python consumer.py`

This is a consumer of the messages sent through Kafka. Simple processing of message length is shown to indicate what you can do with each message. Press CTRL + C to send KeyboardInterrupt to exit the process. Alternatively, close the 

2. `python producer.py`

Producer of messages. Key in any valid string to send. Type "quit" to exit.


You should now see the shell running `consumer.py` displaying the messages from Kafka!

