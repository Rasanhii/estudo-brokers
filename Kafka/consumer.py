from confluent_kafka import Consumer, KafkaError

# Configurações do Kafka
kafka_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'meu-grupo'}

# Cria um consumidor
consumer = Consumer(kafka_config)

# Tópico para consumir mensagens
topic = 'meu-topico'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro no consumo: {msg.error()}')
                break
        print(f'Mensagem recebida: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()