#!/bin/bash

# set the kafka folder directory path
KAFKAPATH="kafka_2.11-2.0.0/"


cd $KAFKAPATH
# Start ZooKeeper Server
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

# create topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sample

# list topics 
bin/kafka-topics.sh --list --zookeeper localhost:2181
