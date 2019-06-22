from time import sleep
from json import dumps
from kafka import KafkaProducer
import json

data_source = open('raw_data/salary_data.csv')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
line_count = 0 
while True:
    line = data_source.readline()

    if not line :
        continue
    else:
        if line_count==0:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            features = line.split(",")
            payload = {"year":features[0], "salary" : features[1], "train": True if line_count%10 == 0 else False,"line_count": line_count}
            print(payload)
            producer.send('numtest', value=payload)
    sleep(2)