#!/bin/bash

# New
export KAFKA_DIR="/usr/kafka"
export KAFKA_VERSION="3.2.0"

#add-apt-repository ppa:webupd8team/java && \
apt install default-jdk -y && \
apt install default-jre -y

mkdir -p ${KAFKA_DIR} && \
curl "https://archive.apache.org/dist/kafka/$KAFKA_VERSION/kafka_2.12-3.2.0.tgz" -o ${KAFKA_DIR}/kafka.tgz && \
tar -xzf ${KAFKA_DIR}/kafka.tgz -C ${KAFKA_DIR} --strip-components 1 && \
rm ${KAFKA_DIR}/kafka.tgz

export HOME=/root
export KAFKA_BIN=${KAFKA_DIR}/bin
export KAFKA_HOME=${KAFKA_DIR}
export PATH="$KAFKA_BIN:$PATH"

# Old
export KAFKA_UUID="AR6hyiffQQQ5FPrAvR2kUu" && echo "export KAFKA_UUID=AR6hyiffQQQ5FPrAvR2kUu" >> ~/.bashrc       
export CONFIG_FILE=$KAFKA_HOME/config/kraft/server.properties
export PATH="$KAFKA_BIN:$PATH"

# Start Kafka
/usr/kafka/bin/kafka-storage.sh format --config $KAFKA_HOME/config/kraft/server.properties --cluster-id $KAFKA_UUID --ignore-formatted
/usr/kafka/bin/kafka-server-start.sh $CONFIG_FILE
