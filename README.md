# Brokers
Um estudo de uma criação utilizando o modelo produto-consumidor

Iniciar o server local *KAFKA*:
- cd kafka_2.13-3.7.0 && bin/zookeeper-server-start.sh config/zookeeper.properties
- cd kafka_2.13-3.7.0 && bin/kafka-server-start.sh config/server.properties

Consumer:
- cd Kafka && python consumer.py 

Producer:
- cd Kafka && python pronducer.py