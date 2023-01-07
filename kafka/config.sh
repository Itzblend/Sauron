#!/bin/bash

export KAFKA_VERSION="3.2.0"
export KAFKA_UUID="AR6hyiffQQQ5FPrAvR2kUu" && echo "export KAFKA_UUID=AR6hyiffQQQ5FPrAvR2kUu" >> ~/.bashrc       
export CONFIG_FILE=$KAFKA_HOME/config/kraft/server.properties
export BOOTSTRAP_SERVER=localhost:9092
export PATH="$KAFKA_BIN:$PATH"

# Start Kafka
kafka-storage.sh format --config $KAFKA_HOME/config/kraft/server.properties --cluster-id $KAFKA_UUID --ignore-formatted
kafka-server-start.sh $CONFIG_FILE
