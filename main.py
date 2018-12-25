from flask import Flask , json , render_template
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from Helper import CreateHashPwd,ExecuteLoginSP,Return_Object,ExecuteRegisterSP,ExecuteLogoutSP,ExecuteSendFRSP,ExecuteRespondFRSP,ExecuteAddPostSP,ExecuteUserIdSP,ExecuteUpdatePostSP,ExecuteUpdateUserSP,ExecuteFriendlistSP


app = Flask(__name__)
api = Api(app)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'abhinavprakash16'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Pass@123'
app.config['MYSQL_DATABASE_DB'] = 'abhinavprakash16$SocialNetwork'
app.config['MYSQL_DATABASE_HOST'] = 'abhinavprakash160896.mysql.pythonanywhere-services.com'

mysql.init_app(app)

conn = mysql.connect()


#@app.route('/Login',methods=['POST'])
class Login(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('Email', type=str, help='Email address to create user')
            parser.add_argument('Password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userEmail = args['Email']
            _userPassword = CreateHashPwd(args['Password'])

            data = ExecuteLoginSP(mysql,conn,_userEmail,_userPassword)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'USER_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_main': str(e)}

#@app.route('/RegisterUser',methods=['POST'])
class RegisterUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('Email', type=str, help='Email address to create user')
            parser.add_argument('Password', type=str, help='Password to create user')
            parser.add_argument('User_Name', type=str, help='User_Name to create user')
            parser.add_argument('First_Name', type=str, help='First_Name of user')
            parser.add_argument('Last_Name', type=str, help='Last_Name of user')
            parser.add_argument('Mobile_Num', type=str, help='Mobile number of user (maximum 10 digits)')
            parser.add_argument('DOB', type=str, help='DOB in format YYYY-MM-DD')
            parser.add_argument('Gender', type=str, help='Gender in form of M,F,T')

            args = parser.parse_args()

            user_Email= args['Email']
            #user_Password= args['Password']
            user_Password= CreateHashPwd(args['Password'])
            User_Name= args['User_Name']
            user_First_Name= args['First_Name']
            user_Last_Name= args['Last_Name']
            user_Mobile_Num= args['Mobile_Num']
            user_DOB= args['DOB']
            user_Gender= args['Gender']

            data = ExecuteRegisterSP(mysql,conn,user_Email,user_Password ,User_Name,user_First_Name,user_Last_Name,user_Mobile_Num,user_DOB,user_Gender)

            if data[0][0] == 1:
                success=True
                error_code="E001"
                error_desc="Successfully Added"
            else:
                success=False
                error_code="E002"
                error_desc="Unable To Add"

            #return {'data':data}
            return {'SUCCESS':success,'USER_ID':data[0][1],'ERROR_DESC':error_desc}

        except Exception as e:
            return {'error_RegisterUser': str(e)}

#@app.route('/Logout',methods=['POST'])
class Logout(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('User_Id', type=str, help='User_Id of user to be logged out')
            args = parser.parse_args()

            _userId = args['User_Id']

            data = ExecuteLogoutSP(mysql,conn,_userId)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'USER_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_Logout': str(e)}

#@app.route('/SendFriendRequest',methods=['POST'])
class SendFriendRequest(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('From_User_Id', type=str, help='User_id of friend request sending user')
            parser.add_argument('To_User_Id', type=str, help='User_id of friend request sending to user')
            args = parser.parse_args()

            _From_User_Id = args['From_User_Id']
            _To_User_Id = args['To_User_Id']

            data = ExecuteSendFRSP(mysql,conn,_From_User_Id,_To_User_Id)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'REQUEST_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_SendFriendRequest': str(e)}

#@app.route('/RespondToFriendRequest',methods=['POST'])
class RespondToFriendRequest(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('Request_Id', type=int, help='Id of friend_request')
            parser.add_argument('Response', type=int, help='Response of friend request')
            args = parser.parse_args()

            _Request_Id = args['Request_Id']
            _Response = args['Response']

            data = ExecuteRespondFRSP(mysql,conn,_Request_Id,_Response)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'REQUEST_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_RespondToFriendRequest': str(e)}

#@app.route('/AddPost',methods=['POST'])
class AddPost(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('User_Id', type=int, help='Id of friend_request')
            parser.add_argument('Caption', type=str, help='Caption of the post')
            parser.add_argument('Content', type=str, help='Content of the post')
            args = parser.parse_args()

            _User_Id = args['User_Id']
            _Caption = args['Caption']
            _Content = args['Content']

            data = ExecuteAddPostSP(mysql,conn,_User_Id,_Caption,_Content)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'POST_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_AddPost': str(e)}

#@app.route('/FetchUserFeed',methods=['POST'])
class FetchUserFeed(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('User_Id', type=str, help='Id of user')
            args = parser.parse_args()

            _User_Id = args['User_Id']

            data = ExecuteUserIdSP(mysql,conn,'SP_FETCH_FEED',_User_Id)

            FinalObject=[]

            for i in range(len(data)):
                thisrow={
                    "POST_ID": data[i][0],
                    "USER_ID": data[i][1],
                   "CAPTION": data[i][2],
                    "CONTENT": data[i][3]
                }
                FinalObject.append(thisrow)

            return {'data':FinalObject}

        except Exception as e:
            return {'error_FetchUserFeed': str(e)}

#@app.route('/UpdatePost',methods=['POST'])
class UpdatePost(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('Post_Id', type=int, help='Id of friend_request')
            parser.add_argument('Caption', type=str, help='Caption of the post')
            parser.add_argument('Content', type=str, help='Content of the post')
            args = parser.parse_args()

            _Post_Id = args['Post_Id']
            _Caption = args['Caption']
            _Content = args['Content']

            data = ExecuteUpdatePostSP(mysql,conn,_Post_Id,_Caption,_Content)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'POST_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_UpdatePost': str(e)}

#@app.route('/UpdateUserDetails',methods=['POST'])
class UpdateUserDetails(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('User_Id', type=int, help='Id of user')
            parser.add_argument('Country', type=str, help='Country name of the user')
            parser.add_argument('State', type=str, help='State of the user')
            parser.add_argument('City', type=str, help='City name of the user')
            parser.add_argument('Profile_Picture_Url', type=str, help='Profile_Picture_Url of the user')

            args = parser.parse_args()

            _User_Id = args['User_Id']
            _Country = args['Country']
            _State = args['State']
            _City = args['City']
            _Profile_Picture_Url = args['Profile_Picture_Url']

            data = ExecuteUpdateUserSP(mysql,conn,_User_Id,_Country,_State,_City,_Profile_Picture_Url)

            if data[0][0] is 1 :
                error_code="E001"
                success=True
            else:
                error_code="E002"
                success=False

            return {'SUCCESS':success,'USER_ID':data[0][1],'ERROR_DESC':data[0][2]}

        except Exception as e:
            return {'error_UpdateUserDetails': str(e)}


#@app.route('/FetchFriendList',methods=['POST'])
class FetchFriendList(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('User_Id', type=str, help='Id of user')
            args = parser.parse_args()

            _User_Id = args['User_Id']

            data = ExecuteFriendlistSP(mysql,conn,_User_Id)

            FinalObject=[]

            for i in range(len(data)):
                thisrow={
                    "FRIEND_ID": data[i][0],
                    "USER_NAME": data[i][1]
                }
                FinalObject.append(thisrow)

            return {'data':FinalObject}

        except Exception as e:
            return {'error_FetchFriendList': str(e)}



api.add_resource(Login, '/Login')
api.add_resource(RegisterUser, '/RegisterUser')
api.add_resource(Logout, '/Logout')
api.add_resource(SendFriendRequest, '/SendFriendRequest')
api.add_resource(RespondToFriendRequest, '/RespondToFriendRequest')
api.add_resource(AddPost, '/AddPost')
api.add_resource(FetchUserFeed, '/FetchUserFeed')
api.add_resource(UpdatePost, '/UpdatePost')
api.add_resource(UpdateUserDetails, '/UpdateUserDetails')
api.add_resource(FetchFriendList, '/FetchFriendList')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def hello_world():
    return render_template('index.html')

