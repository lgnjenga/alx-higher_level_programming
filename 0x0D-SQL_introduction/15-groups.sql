-- List the number of records with the same score
-- Records ordered in descending manner
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
