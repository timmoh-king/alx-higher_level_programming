-- a script that lists all records of the table second_table
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
-- INSERT INTO `second_table`(id, name, score) VALUES(5, 'Aria', 18);
-- INSERT INTO `second_table`(id, name, score) VALUES(6, 'Aria', 12);

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
