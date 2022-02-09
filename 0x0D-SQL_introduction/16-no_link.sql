-- lists all records of the table second_table
-- dosen't  list rows without a name value
-- score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
