-- script that creates a function SafeDiv
DELIMITER |
CREATE FUNCTION SafeDiv ( a int, b int)
RETURNS FLOAT
BEGIN
DECLARE answer FLOAT;
IF b = 0 THEN
SET answer = 0;
ELSE
SET answer = a/b;
END IF;
RETURN answer;
END;
|