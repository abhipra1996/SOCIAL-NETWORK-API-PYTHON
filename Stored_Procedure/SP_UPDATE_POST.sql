DELIMITER $$
CREATE PROCEDURE SP_UPDATE_POST(
IN post_id INT,
IN caption VARCHAR(300),
IN content VARCHAR(11000)
)
BEGIN 
   
    SET @POST_ID = (SELECT P.POST_ID FROM POSTS AS P WHERE P.POST_ID=post_id);    

	IF(@POST_ID IS NOT NULL AND (LENGTH(caption) > 0 OR LENGTH(content) > 0)) THEN
             
             IF(LENGTH(caption) > 0 AND LENGTH(content) > 0) THEN
                UPDATE POSTS AS P SET P.CAPTION=caption , P.CONTENT=content , P.DATE_UPDATED=NOW() WHERE P.POST_ID=@POST_ID;
			 ELSEIF(LENGTH(caption) > 0) THEN
				UPDATE POSTS AS P SET P.CAPTION=caption, P.DATE_UPDATED=NOW() WHERE P.POST_ID=@POST_ID;
			 ELSE
                UPDATE POSTS AS P SET P.CONTENT=content, P.DATE_UPDATED=NOW() WHERE P.POST_ID=@POST_ID;
			 END IF;
             
             SELECT 'true' AS SUCCESS,@POST_ID AS POST_ID,'Successfully Updated' AS ERROR_DESC;
	 ELSE 
             IF(@POST_ID IS NULL) THEN
                SELECT 'false' AS SUCCESS,0 as POST_ID,'Invalid Post_Id' AS ERROR_DESC;
			 ELSE
                SELECT 'false' AS SUCCESS,@POST_ID as POST_ID,'Invalid Post Values' AS ERROR_DESC;
             END IF;
	END IF;
END$$
DELIMITER ;
