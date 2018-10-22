from kafka import KafkaConsumer

consumer = KafkaConsumer('test')

for message in consumer:
	if len(message) >= 10:
		print("Message is long.\n\nMessage:\n", message)
	else:
		print("Message is short.\n\nMessage:\n", message)