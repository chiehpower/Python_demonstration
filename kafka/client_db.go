package main

import (
	"context"
	"fmt"
	"github.com/segmentio/kafka-go"
	"log"
	"os"
	"database/sql"
	"strings"
	"encoding/json"
	"github.com/lib/pq"
	"github.com/joho/godotenv"
)

type Message struct {
	Created      string       `json:"created"`
	UserName     string    `json:"user_name"`
	ProjectName  string    `json:"project_name"`
	ClassIDs     []int     `json:"class_ids"`
	KeyPoints    [][][]int `json:"keypoints"`
	Rois         [][]int   `json:"rois"`
	Scores       []float64 `json:"scores"`
	RawImgPath   string    `json:"raw_img_path"`
	ImgResultPath string    `json:"img_result_path"`
	Word         []string  `json:"word"`
}

func getKafkaReader(kafkaURL, topic string) *kafka.Reader {
	brokers := strings.Split(kafkaURL, ",")
	return kafka.NewReader(kafka.ReaderConfig{
		Brokers:  brokers,
		Topic:    topic,
		// MinBytes: 10e3, // 10KB
		// MaxBytes: 10e6, // 10MB
	})
}

/*
The target is to store these info in the DB after receive the info.
1. created
2. user_name
3. project_name
4. class_ids
5. keypoints
6. rois
7. scores
8. raw_img_path
9. img_result_path
10. word
*/

func main() {

	kafkaURL := "kafka:9092"
	topic := "baeldung_linux"

	reader := getKafkaReader(kafkaURL, topic)

	defer reader.Close()

	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	// Get environment variables
	user := os.Getenv("DB_USER")
	password := os.Getenv("DB_PASSWORD")
	dbname := os.Getenv("DB_NAME")
	host := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	// Connect to PostgreSQL DB
	connStr := fmt.Sprintf("user=%s password=%s dbname=%s host=%s port=%s sslmode=disable", user, password, dbname, host, port)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// 如果有設定這個 則會從最新的開始讀取，而不是從頭。
	reader.SetOffset(kafka.LastOffset) 

	fmt.Println("start consuming ... !!")
	for {
		m, err := reader.ReadMessage(context.Background())
		if err != nil {
			log.Fatalln(err)
		}
		fmt.Printf("message at topic: %v partition: %v offset: %v value: %s\n", m.Topic, m.Partition, m.Offset, string(m.Value))
		
		// Parse the info
		var message Message
		err = json.Unmarshal([]byte(m.Value), &message)
		if err != nil {
			log.Println("Error decoding message:", err)
			continue
		}

		// Write the info into PostgreSQL table.
		query := `INSERT INTO results (created, user_name, project_name, class_ids, keypoints, rois, scores, raw_img_path, img_result_path, word)
				   VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)`
		_, err = db.Exec(query, message.Created, message.UserName, message.ProjectName, pq.Array(message.ClassIDs), pq.Array(message.KeyPoints), pq.Array(message.Rois), pq.Array(message.Scores), message.RawImgPath, message.ImgResultPath, pq.Array(message.Word))
		if err != nil {
			log.Println("Error inserting message into PostgreSQL:", err)
		}

	}
	
}