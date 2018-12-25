DELIMITER $$
CREATE PROCEDURE SP_USER_LOGIN(
IN user_Email VARCHAR(100),
IN user_Password VARCHAR(96)
)
BEGIN 

   SET @USER_PWD = (SELECT USR.USER_PWD FROM USERS AS USR WHERE USR.USER_EMAIL=user_Email);
   SET @USER_ID = (SELECT USR.USER_ID FROM USERS AS USR WHERE USR.USER_EMAIL=user_Email);
   
   IF(@USER_PWD = user_Password) THEN
   
         IF(@USER_ID IS NOT NULL) THEN
       
             UPDATE USERS AS U SET U.LOGIN_COUNT = U.LOGIN_COUNT+1 WHERE U.USER_EMAIL = user_Email;#'abhinavp@gmail.com';
             COMMIT;
             SELECT 'true' AS SUCCESS,@USER_ID AS USER_ID,'Sucessfull Login' AS ERROR_DESC;
	     ELSE
             SELECT 'false' AS SUCCESS , 0 AS USER_ID,'Invalid User_Id' AS ERROR_DESC;
         END IF;
	ELSE
          SELECT 'false' AS SUCCESS,0 AS USER_ID,'Invalid Password' AS ERROR_DESC;
	END IF ;
END$$
DELIMITER ;
