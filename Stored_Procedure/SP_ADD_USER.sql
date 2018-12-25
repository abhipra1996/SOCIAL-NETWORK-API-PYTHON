DELIMITER $$
CREATE  PROCEDURE SP_ADD_USER(
IN user_Email      VARCHAR(50),
IN user_Password   VARCHAR(96),
IN User_Name  VARCHAR(50) ,
IN user_First_Name VARCHAR(20),
IN user_Last_Name  VARCHAR(20),
IN user_Mobile_Num VARCHAR(20),
IN user_DOB        DATE,
IN user_Gender     ENUM('M','F','T')
)
BEGIN 
   
   SET @USER_ID = (SELECT U.USER_ID FROM USERS AS U WHERE U.USER_EMAIL=user_Email);
   
   IF (@USER_ID IS NULL AND (LENGTH(user_Email) > 0) AND (LENGTH(user_Password) > 0) AND (LENGTH(User_Name)>0) AND (LENGTH(user_First_Name)>0)) THEN 
            INSERT INTO USERS (USER_EMAIL,USER_PWD,USER_MOBILE,LOGIN_ATTEMPT,REGISTERED_DATE,ACTIVE_FLAG)VALUES (user_Email,user_Password,user_Mobile_Num,0,NOW(),1);
            SET @USERID:=LAST_INSERT_ID();
            INSERT INTO USER_DETAILS (USER_ID,USER_NAME,FIRST_NAME,LAST_NAME,GENDER,USER_DOB,ACTIVE_FRIEND_COUNT,UPDATED_TIME) VALUES (@USERID,User_Name,user_First_Name,user_Last_Name,user_Gender,user_DOB,0,NOW());
            SELECT 'true' AS SUCCESS,@USERID AS USER_ID,'Successfully Created' as Error_Desc; 
   ELSE
            IF(@USER_ID IS NOT NULL) THEN
			    SELECT 'false' AS SUCCESS,@USER_ID AS USER_ID,'Email_Address already exists' as Error_Desc;
            ELSEIF(LENGTH(user_Email) = 0) THEN
                SELECT 'false' AS SUCCESS,0 AS USER_ID,'Invalid Email_Address' as Error_Desc; 	
            ELSEIF(LENGTH(user_Password) = 0) THEN
                SELECT 'false' AS SUCCESS,0 AS USER_ID,'Invalid Password' as Error_Desc;
            ELSEIF(LENGTH(User_Name) = 0) THEN
                SELECT 'false' AS SUCCESS,0 AS USER_ID,'Invalid User_Name' as Error_Desc;
            ELSE
                SELECT 'false' AS SUCCESS,0 AS USER_ID,'Invalid First_Name' as Error_Desc;			
			END IF;
   END IF;
   
END$$
DELIMITER ;
