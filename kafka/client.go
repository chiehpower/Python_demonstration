package main

import (
	"context"
	"fmt"
	"github.com/segmentio/kafka-go"
	"log"
	"strings"

	"io/ioutil"
	"os"
)

func getKafkaReader(kafkaURL, topic string) *kafka.Reader {
	brokers := strings.Split(kafkaURL, ",")
	return kafka.NewReader(kafka.ReaderConfig{
		Brokers:  brokers,
		Topic:    topic,
		// MinBytes: 10e3, // 10KB
		// MaxBytes: 10e6, // 10MB
	})
}

func main() {

	kafkaURL := "kafka:9092"
	// topic := "baeldung_linux"
	topic := "image_topic"

	reader := getKafkaReader(kafkaURL, topic)

	defer reader.Close()

	// 如果有設定這個 則會從最新的開始讀取，而不是從頭。
	reader.SetOffset(kafka.LastOffset) 

	fmt.Println("start consuming ... !!")
	for {
		m, err := reader.ReadMessage(context.Background())
		if err != nil {
			log.Fatalln(err)
		}

		fmt.Printf("message at topic: %v partition: %v offset: %v value: %s\n", m.Topic, m.Partition, m.Offset, string(m.Value))

		// Save the image.
		err = ioutil.WriteFile("received_image_client.jpg", m.Value, os.ModePerm)
		if err != nil {
			log.Println("Error saving image:", err)
			continue
		}

		fmt.Println("Image received and saved successfully.")
	}
}