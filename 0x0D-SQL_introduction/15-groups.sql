-- lists the number of records with the same score in the table second_table
-- number of records for this score with the label number
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
