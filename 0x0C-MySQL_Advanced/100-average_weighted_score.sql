-- script that creates a stored procedure ComputeAverageWeightedScoreForUser

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT SUM(score * weight) / (SELECT SUM(weight))
	FROM projects
	INNER JOIN corrections
	WHERE projects.id = corrections.project_id
	AND corrections.user_id = user_id)
	WHERE users.id = user_id;
END

$$

DELIMITER ;