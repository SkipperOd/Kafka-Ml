from kafka import KafkaConsumer
from json import loads
import csv
from ml import test_function
 


test_function()

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    message = message.value
    row = [ message['year'],message['salary'] ]
    with open('data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)    
        writer.writerow(row)
    csvFile.close()

    