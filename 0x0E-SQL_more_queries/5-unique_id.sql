-- Script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT NOT NULL UNIQUE,
    name VARCHAR(256));
ALTER TABLE unique_id ALTER id SET DEFAULT 1;
