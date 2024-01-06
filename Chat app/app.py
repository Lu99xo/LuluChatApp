
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import base64
import werkzeug
import time
from time import sleep
from flask import jsonify



app = Flask(__name__)

app.secret_key = 'password'

# Insert data into database
cnx = mysql.connector.connect(user='username', password='password',
                                host='0000',
                                database='databae')
cursor = cnx.cursor()

#___First page ever in the App________

@app.route('/')
def form():
    return render_template('login.html')


#___Regist new Account_____

@app.route('/submit', methods =['GET','POST'])
def submit():

    errormsg = ''
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    avatar = request.form['avatar']
        
    query = ("INSERT INTO form(username,password, email, avatar) VALUES (%s, %s, %s, %s)")
    data = (username, password, email,avatar )

    cursor.execute(query, data)
    cnx.commit()

    cursor.close()
    cnx.close()

    return redirect(url_for('form'))

#__linking signup link

@app.route('/signup')
def signup():
    return render_template('index.html')


#____ Login page 

# global user x ID 
usernameID = 0
# global users y info
datag = ''
ung = ''
pimg = ''
lastxt = ''

#__Login function 
    #__ check password and username
    #__ Get user x 
    #__ Get all users y data
@app.route('/login', methods =['GET','POST'])
def login() :
    msg = ''
   
    if request.method == 'POST' :

        # get username & password from the login page

        username = request.form['username']
        password = request.form['password']



        #!!!!!!!!!!!!!!!!!!!!!!!!
        #Active dot

        #if the user login
            #make the button green 
        #else
            #gray button



        #Profile image for the user x

        user_query = "SELECT avatar FROM form WHERE username = %s"
        cursor.execute(user_query, (username,))
        user_avatar = cursor.fetchall()
        for av in user_avatar :
            profile_img = av
        
        # Get user x ID
            
        global usernameID
        Id_query = "SELECT ID FROM form WHERE username = %s"
        cursor.execute(Id_query, (username,))
        usernameIDQ= cursor.fetchone()
        for ID in  usernameIDQ :
            userxID = ID
        usernameID = userxID

        # procedure for last messages 
        
        """ global lastxt

        def lastMsg (usery) :

            userx = usernameID 
            for y in usery :

                lastmsg_query = " SELECT msg FROM msg
                                    WHERE ( incoming_msg_id = %s AND outgoing_msg_id = %s )
                                    OR ( incoming_msg_id = %s AND outgoing_msg_id = %s )
                                    ORDER BY msgDate DESC
                                    LIMIT 1;

                "
                cursor.execute(lastmsg_query, (userx , y, y, userx ) )
                lastxt_q = cursor.fetchall()

                return lastxt_q 
        
        # user y IDs list 

        yIDs_query = "SELECT ID FROM form WHERE ID != %s"
        cursor.execute(yIDs_query, (usernameID, ))
        yIDs_q = cursor.fetchall()
        
        result_lastMsg = []
        for ID in yIDs_q :
            call = lastMsg(ID)
            result_lastMsg.append(call) 

        

        for ID in result_lastMsg :
            for msg in ID  :
                rez = msg[0]
       """
        #  Get user y ID, avatar, username
             #_function to get  users data ( ID , username , avatar )

        def users():

            usersList = """ SELECT username, avatar FROM form WHERE username != %s """
            cursor.execute(usersList, (username,) )
            usersx = cursor.fetchall()
            return usersx
            

        # Check if the password right? 

        query = "SELECT password FROM form WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        #check wrong password 
        if result is not None and result[0] == password:
            #for logout
            session['loggedin'] = True
            #for userData
            data = users()

            #save data for global 
            global datag 
            datag = data

            global ung 
            ung = username

            global pimg 
            pimg = profile_img

            return render_template('users.html', data = data, username = username ,  profile_img =  profile_img )
        
        else:

            msg = " Wrong password ! "
            return render_template('login.html', msg = msg )
        
        #Here I need to check wrong username and alert with that

    return msg

#__ back step to users page
    #_ use global vars here 
@app.route('/usersp')
def usersp() :

    global datag 
    data = datag

    global ung 
    username = ung

    global pimg 
    profile_img = pimg 
    

    return render_template('users.html',  data = data, username = username ,  profile_img =  profile_img)

#__search 
    #the target user

@app.route('/search')
def t_user() : 

    #IF POST
        # request username
        # get usersnames from global var
        # if username == usernames 
            #return the target user message

    return



#__Logout function
@app.route('/logout')
def logout() :
    msg = "ur logged out"
    session.pop('loggedin', None)
    return render_template('login.html', msg = msg )


# Global user y ID
uID = 0
username = ''
                                        #                                    
                                       ###
                                    #########
                                  #############
                                #################
                              #####################
                            #########################
                         ##############################
                     ######################################
                ################################################
           ################## the not working code ###################
############# thank you for wasting my time, see you in the new year ###############

# chat page function 
    #__ Return user y ID & avatar 
    #___ Return saved messages from Database 

@app.route('/chat/<user>', methods =['GET','POST'])
def chatu(user):

    # get usery info 
    global username
    username = user

    #__ ID 
    global uID
    usery_query = """ SELECT ID FROM form WHERE username = %s """
    cursor.execute( usery_query, (user,) )
    usery_query= cursor.fetchone()
    for ID in usery_query :
        uyID = ID
    uID = uyID

    #__avatar
    userav_query = """ SELECT avatar FROM form WHERE username = %s """
    cursor.execute( userav_query, (user,) )
    userav_query = cursor.fetchone()
    for av in userav_query  :
        avatar = av


    #user Y ID
    inMsgID = uID

    #user X ID
    global usernameID
    outMsgID = usernameID
    
    #__ Retrive all messages from DB

    def inmsg() :

        incoming_query = """ SELECT outgoing_msg_id,incoming_msg_id, msg  FROM msg
                            WHERE (outgoing_msg_id = %s AND incoming_msg_id = %s )
                            OR ( incoming_msg_id = %s AND outgoing_msg_id  = %s )
                            ORDER BY msgDate ASC ; 
                        """
        cursor.execute(incoming_query, ( outMsgID, inMsgID , outMsgID,  inMsgID ))
        inMsg_q = cursor.fetchall()


        return inMsg_q 
    
    
    inMsg = inmsg()

    return render_template('chatu.html', user=user, avatar = avatar,  inMsg = inMsg , outMsgID = outMsgID ,  inMsgID  =  inMsgID )


# save messages function 
    #__ insert the msgs to DB 
@app.route('/click', methods =['GET','POST'])
def click() : 
    txtmsg = ''
    if request.method == 'POST' :
        #user y ID
        global uID  
        inMsgID = uID

        #user x ID
        global usernameID
        outMsgID= usernameID
        
        # get msg
        user_msg = request.form['txtmsg']

        #if outMsgID != 0 and inMsgID != 0 :

        query = ("INSERT INTO msg(incoming_msg_id, outgoing_msg_id, msg) VALUES (%s, %s, %s)")
        data = (inMsgID, outMsgID , user_msg )

        cursor.execute(query, data)
        cnx.commit()

        #msg to send
        txtmsg = user_msg
   
    return txtmsg 

# make the outcoming msgs stay at the page 

@app.route('/load_msgs', methods =['GET','POST'])
def load_msgs() :
  
    #user Y ID
    global uID  
    inMsgID = uID

    #user X ID
    global usernameID
    outMsgID = usernameID

                                                                
    msg_query = """ SELECT * FROM msg WHERE outgoing_msg_id = %s AND incoming_msg_id = %s
                    ORDER BY msgDate ASC;
                """
    cursor.execute(msg_query, ( outMsgID,inMsgID, ))
    user_msg_query = cursor.fetchall()

    msgs = {
            'outgoing': [],
            
        }

    return jsonify(msgs)


# search user Function 

@app.route('/search_user' , methods =['GET','POST'])   
def search_user() : 

    #request input data
    if request.method == 'POST' :
                
        tar_user = request.form['search']

        #_function to get  users data ( ID , username , avatar )
            #select users from data where username = %s
                #execute input username
        def users():

            usersList = """ SELECT username, avatar FROM form WHERE username = %s """
            cursor.execute(usersList, (tar_user,) )
            usersx = cursor.fetchall()
            return usersx
        
        data = users()

        # get user x username & avatar 
        
        global ung 
        username = ung 

        global pimg 
        profile_img = pimg


        #return username from users list
    
        return render_template('users.html', data = data, username = username ,  profile_img =  profile_img )
        


if __name__ == '__main__':
    app.run(debug=True)

