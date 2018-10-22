from kafka import KafkaConsumer
import csv
from datetime import datetime
import os


consumer = KafkaConsumer('test')
if os.path.isfile('messages.csv'):
	print("messages.csv already exists...\ndeleting...")
	os.remove('messages.csv')

with open('messages.csv', 'a') as f:
	fWriter = csv.writer(f)
	fWriter.writerow(['timestamp','message'])
	print("CSV initialised")
	for message in consumer:
		msg = str(message.value.decode())
		# divide by 1000 as it's in ms
		ts = datetime.fromtimestamp(message.timestamp/1000).strftime("%A, %B %d, %Y %I:%M:%S")
		print("Writing message %s..." % msg)
		fWriter.writerow([ts, msg])