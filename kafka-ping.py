from kafka import KafkaConsumer

consumer = KafkaConsumer('purchases', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', security_protocol='SSL')
for message in consumer:
    print (message)
