from kafka import KafkaConsumer
from json import loads
import csv
from regression_model import model as regression
 

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

regression = regression()

for message in consumer:
    message = message.value
    row = [ message['year'],message['salary'] ]
    print(row)
    if message['train']:
        regression.update()
    regression.predict(float(message['year']))
    with open('model_data/data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)    
        writer.writerow(row)
    csvFile.close()

    