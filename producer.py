from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

while True:
	print("\n\nType\"quit\" to exit")
	print("Enter message to be sent:")
	msg = input()
	producer.send('test', msg)