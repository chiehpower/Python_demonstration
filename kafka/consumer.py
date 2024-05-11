from kafka import KafkaConsumer

# Kafka broker地址和主題名稱
bootstrap_servers = ['kafka:9092']
topic_name = 'baeldung_linux'

# 設置Kafka消費者
consumer = KafkaConsumer(topic_name,
                         bootstrap_servers=bootstrap_servers)
                        #  group_id= 'group2')
                        #  consumer_timeout_ms=1000)
# 從主題中讀取消息
for message in consumer:
    # print(message)
    # 解析消息的主題、分區、偏移量、鍵和值
    print("hello")
    topic = message.topic
    partition = message.partition
    offset = message.offset
    key = message.key
    value = message.value

    # 輸出消息資訊
    print(f"Topic: {topic}, Partition: {partition}, Offset: {offset}, Key: {key}, Value: {value.decode('utf-8')}")
print("test")
# 關閉消費者連接
consumer.close()

# from kafka import KafkaConsumer
# from kafka import TopicPartition

# consumer = KafkaConsumer(group_id= 'group2', bootstrap_servers= ['kafka:9092'])
# consumer.assign([TopicPartition(topic= 'my_topic', partition= 0)])
# for msg in consumer:
#     print(msg)