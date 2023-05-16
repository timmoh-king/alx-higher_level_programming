-- a script that lists all records with a score >= 10
-- in the table second_table of the database hbtn_0c_0
-- Results should display both the score and the name
SELECT score, name
	FROM `second_table`i
	WHERE score >= 10
	ORDER BY score DESC;
