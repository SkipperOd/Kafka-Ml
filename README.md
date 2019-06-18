# Kafka-Ml
 Creating pipeline by integrating Kafka with Machine learning techniques.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Clone repo
```
git clone https://github.com/SkipperOd/Kafka-Ml.git
```

### Setting up the environment

### Installing

First of all you want to have installed Kafka and Zookeeper on your machine

```
https://kafka.apache.org/downloads
```

### Configuring kafka

Configuring Apache Kafka on Windows.
```
https://medium.com/@shaaslam/installing-apache-kafka-on-windows-495f6f2fd3c8
```
Next install Kafka-Python.

You can do this using pip or conda, if you’re using an Anaconda distribution.
```
pip install kafka-python

conda install -c conda-forge kafka-python
```
## Running Kafka

Run Zookeeper 
```
zookeeper-server-start config/zookeeper.properties
```
Run Kafka-Server
```
kafka-server-start config/server.properties
```
#### Don’t forget to start your Zookeeper server and Kafka broker before executing the example code below.

Create a new topic

```
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic numtest
```