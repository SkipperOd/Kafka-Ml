from time import sleep
from json import dumps
from kafka import KafkaProducer


data_source = open('input.txt')
producer = KafkaProducer(bootstrap_servers=['localhost:y'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

while True:
    line = data_source.readline()
    if not line :
        continue
    else:
        print(line)
        producer.send('numtest', value=line)
    sleep(2)