import os
from collections import deque
from flask import Flask,render_template,jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels={"main":deque(maxlen=100)}

class message:
    def __init__(self,name,date_time,msg):
        self.name=name
        self.date_time=date_time
        self.msg=msg

def create_channel(name):

    
    if name in channels:
        return False
    else:
        #using deque for message list, as suggested at https://stackoverflow.com/a/5944754
        channels[name]=deque(maxlen=100)
        return True

def post_msg(msg,channel):
    channels[channel].append(msg)

first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")
first= message("rajat",datetime.now(),"hi there!! test works")
post_msg(first,"main")


@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/chatroom",methods=["GET","POST"])
def chat():
    return render_template("chatroom.html",channels=channels)

@app.route("/")
def retjson():
    return make_json(channels["main"])

def make_json(channel_msgs):
    json_form=str()
    json_form='{"msgs":'
    for all in channel_msgs:
        json_form+='{"name":'+str(all.name)+',"msg":'+str(all.msg)+',"date":'+str(all.date_time)+'},'
    json_form=json_form+'}'
    return jsonify(json_form)
