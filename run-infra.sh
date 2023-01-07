docker-compose up -d kafka1
sleep 10
docker-compose up -d api
sleep 5
docker-compose up -d bot


# $KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic purchases