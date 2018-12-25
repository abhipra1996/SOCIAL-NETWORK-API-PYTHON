DELIMITER $$
CREATE  PROCEDURE SP_ADD_POST(
IN user_id INT,
IN caption VARCHAR(300),
IN content VARCHAR(11000)
)
BEGIN 
   
    SET @USER_ID = (SELECT U.USER_ID FROM USERS AS U WHERE U.USER_ID=user_id);

	IF(@USER_ID IS NOT NULL AND LENGTH(caption) > 0 AND LENGTH(content) > 0) THEN
             INSERT INTO POSTS (USER_ID,CAPTION,CONTENT,DATE_CREATED) VALUES (user_id,caption,content,NOW());
			 SET @POST_ID:=LAST_INSERT_ID();
             SELECT 'true' AS SUCCESS,@POST_ID as POST_ID,'Sucessfully POSTED' AS ERROR_DESC;
	ELSE 
             IF(@USER_ID IS NULL) THEN
                SELECT 'false' AS SUCCESS,0 as POST_ID,'Invalid User_Id' AS ERROR_DESC;
			 ELSEIF(LENGTH(caption) = 0) THEN
                SELECT 'false' AS SUCCESS,0 as POST_ID,'Invalid Caption' AS ERROR_DESC;
			 ELSE
                SELECT 'false' AS SUCCESS,0 as POST_ID,'Invalid Content' AS ERROR_DESC;
             END IF;
	END IF;
END$$
DELIMITER ;