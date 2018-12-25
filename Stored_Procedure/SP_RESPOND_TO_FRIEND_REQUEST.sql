DELIMITER $$
CREATE PROCEDURE SP_RESPOND_TO_FRIEND_REQUEST(
IN request_id INT,
IN Response INT
)
BEGIN 
   
   SET @REQUEST_ID = (SELECT FM.REQUEST_ID FROM FRIENDSHIP_MAPPING AS FM WHERE FM.REQUEST_ID= request_id AND FM.ACTIVE_FLAG=0);

	IF(@REQUEST_ID IS NOT NULL AND (Response = 0 || Response =1) ) THEN
             UPDATE FRIENDSHIP_MAPPING AS FM SET FM.ACCEPTED_FLAG = Response ,FM.ACCEPTED_DATE=NOW() , FM.ACTIVE_FLAG=1 WHERE FM.REQUEST_ID=request_id;
             
             IF(Response = 1) THEN
                              SET @FROM_ID = (SELECT FM.FRIEND_ID_FROM FROM FRIENDSHIP_MAPPING AS FM WHERE FM.REQUEST_ID=request_id);
                              SET @TO_ID = (SELECT FM.FRIEND_ID_TO FROM FRIENDSHIP_MAPPING AS FM WHERE FM.REQUEST_ID=request_id);             
                              UPDATE USER_DETAILS AS UD SET UD.ACTIVE_FRIEND_COUNT = UD.ACTIVE_FRIEND_COUNT + 1 WHERE UD.USER_ID IN (@FROM_ID,@TO_ID);
             END IF;
             
             SELECT 'true' AS SUCCESS,@REQUEST_ID as REQUEST_ID,'Sucessfully Responded' AS ERROR_DESC;
	ELSE 
             IF(@REQUEST_ID IS NULL) THEN
                SELECT 'false' AS SUCCESS,0 as REQUEST_ID,'Invalid Request_Id' AS ERROR_DESC;
			 ELSE
                SELECT 'false' AS SUCCESS,@REQUEST_ID as REQUEST_ID,'Invalid Response. Please enter 0 or 1.' AS ERROR_DESC;
             END IF;
	END IF;
END$$
DELIMITER ;
