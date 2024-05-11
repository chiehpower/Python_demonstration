from kafka import KafkaProducer
import time
a = time.time()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
print(f"producer take {time.time()-a}")
for i in range(100):
    b = time.time()
    message = f'my_value {i}: {b}'
    future = producer.send('baeldung_linux', key=b'my_key', value=bytes(message, 'utf-8'), partition=0)
    result = future.get(timeout=10)
    print(result)
    print(f"No.{i} take {time.time()-b}\n")
    time.sleep(0.5)
