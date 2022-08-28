-- CREATE DATABASE springboardopt;

USE springboardopt;

DROP TABLE IF EXISTS `springboardopt`.`sales`;

CREATE TABLE springboardopt.sales (
	ticket_id INT,
	trans_date DATETIME,
	event_id INT,
	event_name VARCHAR(50),
	event_date DATE,
	event_type VARCHAR(10),
	event_city VARCHAR(20),
	customer_id INT,
	price DECIMAL,
	num_tickets INT
)
