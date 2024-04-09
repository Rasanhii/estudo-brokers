# estudo-brokers
Um estudo de uma criação utilizando o modelo produto-consumidor

Iniciar o server local KAFKA:
- bin/zookeeper-server-start.sh config/zookeeper.properties
- bin/kafka-server-start.sh config/server.properties

Consumer:
- cd Kafka && python consumer.py 

Producer:
- cd Kafka && python pronducer.py