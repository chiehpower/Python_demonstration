# from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# future = producer.send('test',
#                        key=b'my_key',
#                        value=b'my_value')
# result = future.get(timeout=10)
# print(result)

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
future = producer.send('baeldung_linux', key=b'my_key', value=b'my_value', partition=0)
result = future.get(timeout=10)
print(result)
