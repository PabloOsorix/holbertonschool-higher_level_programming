/*script that list the number
of recrods with the same score*/
SELECT score, COUNT(*) AS number
FROM second_table GROUP BY score;
