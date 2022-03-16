-- Script that create a second table in database hbtn_oc_0.
CREATE TABLE IF NOT EXISTS second_table(
    id INT NOT NULL, name VARCHAR(256) NOT NULL,
    score INT NOT NULL);

INSERT INTO second_table(id, name, score)
VALUES 
    ('1', 'Aria', '10'),
    ('2', 'Alex', '3'),
    ('3', 'Bob', '14'),
    ('4', 'George', '8');
