#!/bin/bash

export KAFKA_VERSION="3.2.0"
export KAFKA_UUID="AR6hyiffQQQ5FPrAvR2kUu" && echo "export KAFKA_UUID=AR6hyiffQQQ5FPrAvR2kUu" >> ~/.bashrc       
export CONFIG_FILE=$KAFKA_HOME/config/kraft/server.properties
export BOOTSTRAP_SERVER=localhost:9092
export PATH="$KAFKA_BIN:$PATH"

# Start Kafka
kafka-storage.sh format --config $KAFKA_HOME/config/kraft/server.properties --cluster-id $KAFKA_UUID --ignore-formatted
kafka-server-start.sh $CONFIG_FILE

# Creating topic
/tmp/kafka/kafka_2.12-3.2.0/bin# ./kafka-topics.sh --bootstrap-server=localhost:9092 \
--create --topic book_purchases --partitions 1 --replication-factor 1