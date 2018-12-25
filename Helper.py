from flaskext.mysql import MySQL
import hmac
import hashlib
import base64
import json

def ExecuteLoginSP(mysql,conn,_userEmail,_userPassword):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_USER_LOGIN',(_userEmail,_userPassword))
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteLoginSP': str(e)}

        finally:
            cursor.close()

def ExecuteLogoutSP(mysql,conn,_userId):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_USER_LOGOUT',(_userId))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteLogoutSP': str(e)}

        finally:
            cursor.close()



def ExecuteRegisterSP(mysql,conn,user_Email,user_Password ,User_Name,user_First_Name,user_Last_Name,user_Mobile_Num,user_DOB,user_Gender):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_ADD_USER',(user_Email,user_Password ,User_Name,user_First_Name,user_Last_Name,user_Mobile_Num,user_DOB,user_Gender))
            conn.commit()
            data = cursor.fetchall()

            if data is not None:
                return data
            else:
                return [[0,0]]

            #return data

        except Exception as e:
            return {'error_ExecuteSP': str(e)}

        finally:
            cursor.close()


def ExecuteSendFRSP(mysql,conn,_FromUserId,_ToUserId):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_SEND_FRIEND_REQUEST',(_FromUserId,_ToUserId))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteSendFRSP': str(e)}

        finally:
            cursor.close()

def ExecuteRespondFRSP(mysql,conn,_RequestId,_Response):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_RESPOND_TO_FRIEND_REQUEST',(_RequestId,_Response))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteSendFRSP': str(e)}

        finally:
            cursor.close()


def ExecuteAddPostSP(mysql,conn,_UserId,_Caption,_Content):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_ADD_POST',(_UserId,_Caption,_Content))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteAddPostSP': str(e)}

        finally:
            cursor.close()

def ExecuteUserIdSP(mysql,conn,SP_NAME,_UserId):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc(SP_NAME,(_UserId))
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteUserIdSP': str(e)}

        finally:
            cursor.close()

def ExecuteUpdatePostSP(mysql,conn,_PostId,_Caption,_Content):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_UPDATE_POST',(_PostId,_Caption,_Content))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteUpdatePostSP': str(e)}

        finally:
            cursor.close()

def ExecuteUpdateUserSP(mysql,conn,User_Id,Country,State,City,Profile_picture_url):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_UPDATE_USER_DETAILS',(User_Id,Country ,State,City,Profile_picture_url))
            conn.commit()
            data = cursor.fetchall()

            if data is not None:
                return data
            else:
                return [[0,0,'Unable to Update']]

            #return data

        except Exception as e:
            return {'error_ExecuteUpdateUserSP': str(e)}

        finally:
            cursor.close()


def ExecuteFriendlistSP(mysql,conn,_userId):
        try:

            if conn.ping(True) :
                cursor = conn.cursor()
            else:
                conn = mysql.connect()
                cursor = conn.cursor()

            cursor.callproc('SP_FETCH_FRIENDLIST',(_userId))
            conn.commit()
            data = cursor.fetchall()

            return data

        except Exception as e:
            return {'error_ExecuteFriendlistSP': str(e)}

        finally:
            cursor.close()

def CreateHashPwd(inputstring):
        try:
            secret_key='go recko'
            digest = hmac.new(secret_key, msg=inputstring, digestmod=hashlib.sha256).digest()
            signature = base64.b64encode(digest).decode()
            return signature

        except Exception as e:
            return {'error_CreateHash': str(e)}







