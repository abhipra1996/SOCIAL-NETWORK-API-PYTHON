DELIMITER $$
CREATE PROCEDURE SP_FETCH_FEED(
IN User_id INT
)
BEGIN 
    
    SET @USER_ID = (SELECT U.USER_ID FROM USERS AS U WHERE U.USER_ID=User_id);

	IF(@USER_ID IS NOT NULL) THEN
            SELECT P.POST_ID,P.USER_ID,P.CAPTION,P.CONTENT FROM
			(
				SELECT FM.FRIEND_ID_TO AS FRIEND_ID FROM FRIENDSHIP_MAPPING AS FM
				WHERE FM.FRIEND_ID_FROM=User_id AND FM.ACCEPTED_FLAG=1 AND FM.ACTIVE_FLAG=1
				UNION
				SELECT FM.FRIEND_ID_FROM AS FRIEND_ID FROM FRIENDSHIP_MAPPING AS FM 
				WHERE FM.FRIEND_ID_TO=User_id AND FM.ACCEPTED_FLAG=1 AND FM.ACTIVE_FLAG=1
				UNION
				SELECT @USER_ID AS FRIEND_ID
			) AS FM
			INNER JOIN POSTS AS P ON FM.FRIEND_ID=P.USER_ID
			ORDER BY COALESCE(P.DATE_UPDATED,P.DATE_CREATED) DESC;
	END IF;
END$$
DELIMITER ;
