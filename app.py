import os
from collections import deque
from flask import Flask,render_template,jsonify, send_from_directory
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels={"main":deque(maxlen=100),"new":deque(maxlen=100)}

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


@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/chatroom",methods=["GET","POST"])
def chat():
    return render_template("chatroom.html",channels=channels)

@app.route("/channel/<string:channel>")
def get_msgs(channel):
    if channel not in channels:
        return jsonify({"channel_exist":False})
    result=make_json(channel)
    result["channel_exist"]=True
    return jsonify(result)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@socketio.on("create new channel")
def create_channel(data):
    channel=data["new_channel"]
    if channel in channels:
        emit("channel exists",{"channel_created":False},broadcast=False)
    else:
        channels[channel]=deque(maxlen=100)
        emit("Channel created",{"new_channel":channel},broadcast=True)

@socketio.on("send new msg")
def send_msg(data):
    date_time=datetime.now().strftime("%d/%m/%y  %M:%S")
    msg=message(data["name"],date_time,data["new_msg"])
    post_msg(msg,data["channel"])
    emit("new msg",{"channel":data["channel"],"name":data["name"],"new_msg":data["new_msg"],"date_time":date_time},broadcast=True)

@socketio.on("get msgs")
def send_msgs(data):
    channel=data["channel"]
    msgs=make_json(channel)
    emit("channel msgs",msgs)


def make_json(channel):
    json_form=dict()
    json_form["msgs"]=list()
    for all in channels[channel]:
        new=dict()
        new["name"]=all.name
        new["date_time"]=all.date_time
        new["msg"]=all.msg
        json_form["msgs"].append(new)
    json_form["channel"]=channel
    return json_form


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
