DELIMITER $$
CREATE  PROCEDURE SP_FETCH_FRIENDLIST(
IN User_id INT
)
BEGIN 
   
    SET @USER_ID = (SELECT U.USER_ID FROM USERS AS U WHERE U.USER_ID=User_id);    

	IF(@USER_ID IS NOT NULL) THEN
                SELECT FM.FRIEND_ID_TO AS FRIEND_ID,UD.USER_NAME FROM FRIENDSHIP_MAPPING AS FM
                LEFT JOIN USER_DETAILS AS UD ON UD.USER_ID=FM.FRIEND_ID_TO
				WHERE FM.FRIEND_ID_FROM=User_id AND FM.ACCEPTED_FLAG=1 AND FM.ACTIVE_FLAG=1
				UNION
				SELECT FM.FRIEND_ID_FROM AS FRIEND_ID,UD.USER_NAME FROM FRIENDSHIP_MAPPING AS FM 
                LEFT JOIN USER_DETAILS AS UD ON UD.USER_ID=FM.FRIEND_ID_FROM
				WHERE FM.FRIEND_ID_TO=User_id AND FM.ACCEPTED_FLAG=1 AND FM.ACTIVE_FLAG=1;
	END IF;

END$$
DELIMITER ;