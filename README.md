# Simple tutorial in Python for Kafka

Using Java/Scala to work with Kafka is hard (especially someone like me). *Ta-da!*

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
Step 2: Start the server

Also, install pip requirements by running `pip install -r requirements.txt`

## Step 2: 

Kafka uses ZooKeeper so you need to first start a ZooKeeper server if you don't already have one. You can use the convenience script packaged with kafka to get a quick-and-dirty single-node ZooKeeper instance.
	
> bin/zookeeper-server-start.sh config/zookeeper.properties
[2013-04-22 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
...

Now start the Kafka server:
	
> bin/kafka-server-start.sh config/server.properties
[2013-04-22 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
[2013-04-22 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
...

## Step 3: Create a topic

Let's create a topic named "test" with a single partition and only one replica:
1
	
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

We can now see that topic if we run the list topic command:

> bin/kafka-topics.sh --list --zookeeper localhost:2181 test

## Step 4: 

In separate command shells, run the following:

1. `python consumer.py`

This is a consumer of the messages sent through Kafka. Simple processing of message length is shown to indicate what you can do with each message. Press CTRL + C to send KeyboardInterrupt to exit the process. Alternatively, close the 

2. `python producer.py`

Producer of messages. Key in any valid string to send. Type "quit" to exit.


You should now see the shell running `consumer.py` displaying the messages from Kafka!

