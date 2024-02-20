## Usage

Start the services.
```
docker-compose up -d
```

1. Start the consumer.
    ```
    docker-compose exec kafka kafka-console-consumer.sh --topic baeldung_linux --from-beginning --bootstrap-server kafka:9092
    ```
2. Start the producer.
    ```
    docker-compose exec kafka kafka-console-producer.sh --topic baeldung_linux --broker-list kafka:9092
    ```
    You can start type the message, and then you can check the message in the consumer side.
