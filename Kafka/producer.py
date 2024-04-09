from confluent_kafka import Producer

# Configurações do Kafka
kafka_config = {'bootstrap.servers': 'localhost:9092'}

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao enviar mensagem: {err}')
    else:
        print(f'Mensagem enviada: {msg.value().decode("utf-8")}')

# Cria um produtor
producer = Producer(kafka_config)

# Tópico para enviar mensagens
topic = 'meu-topico'

# Envia mensagens
for i in range(5):
    producer.produce(topic, f'Mensagem {i}', callback=delivery_report)

# Aguarda as mensagens serem entregues
producer.flush()