function register() {
    name = document.querySelector('#name').value;
    if (!Boolean(name) || name === "undefined") {
        alert("retry");
        return true;
    }
    localStorage.name = name;
    location.replace("/chatroom");
}

function welcome() {

    if (!localStorage.name) {
        reg_form = '<form><input id="name" name="name" type="text" class="form-control" placeholder="User Name"><br><button onclick="register()">Register</button></form>';
        document.querySelector('#reg_form').innerHTML = reg_form;
    } else {
        window.location.href = '/chatroom';
    }
}

function get_msgs(channel) {
    const request = new XMLHttpRequest();
    request.open('GET', `/channel/${channel}`);
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.channel_exist) {

            localStorage.current_channel = channel;
            var i;
            var content="";
            msgs=data.msgs
            for (i = 0; i < msgs.length;i++) {
                if (msgs[i].name == localStorage.name) {
                    content = content + '<li class="chat__bubble chat__bubble--sent ">'  + msgs[i].msg + '<br>' + msgs[i].date_time + '</li>';
                } else {
                    content = content + '<li class="chat__bubble chat__bubble--rcvd "><b>' + msgs[i].name + '</b><br>' + msgs[i].msg + '<br>' + msgs[i].date_time + '</li>';
                }
            }
            document.querySelector('.chat').innerHTML=content;
            alert(channel+" Entered");
            console.log(content);

        }
        else {
            document.querySelector('.chat').innerHTML = "No such chatroom";
        }
    };
    request.send();
    return false;
}

function notify(message) {
    document.querySelector('.notify').innerHTML = '<div class="alert alert-warning alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>' + message + '</div>';
}

document.addEventListener('DOMContentLoaded', () => {
  get_msgs(localStorage.current_channel);
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        document.querySelector('#create_channel').onsubmit = () => {
            const new_channel = document.querySelector('#new_channel').value;
            if (!new_channel || new_channel === '') {
                alert("Enter channel name");
                return false;
            }
            socket.emit('create new channel', {
                'new_channel': new_channel
            });
            return false;
        };
        document.querySelector('.post_box').onsubmit = () => {
            const new_msg = document.querySelector('#new_msg').value;
            const channel = localStorage.current_channel;
            if (!new_msg || new_msg === '') {
                alert("Enter message");
                return false;
            }
            socket.emit('send new msg', {
                'name': localStorage.name,
                'new_msg': new_msg,
                'channel': channel
            });

            return false;
        };
    });

    socket.on('new msg', data => {
        if (localStorage.current_channel == data.channel) {
            if (data.name == localStorage.name) {
                document.querySelector('.chat').innerHTML = document.querySelector('.chat').innerHTML + '<li class="chat__bubble chat__bubble--sent ">' + data.new_msg + '<br>' + data.date_time + '</li>';
            } else {
                document.querySelector('.chat').innerHTML = document.querySelector('.chat').innerHTML + '<li class="chat__bubble chat__bubble--rcvd "><b>' + data.name + '</b><br>' + data.new_msg + '<br>' + data.date_time + '</li>';
            }
        }
        else{
          notify("New message in "+data.channel);

        }
    });
    socket.on('channel exists', data => {
        if (!data.channel_created) {
            alert("Channel exists");
        }
    });
    socket.on('Channel created', data => {
        nav = '<li class="nav-text"><a class="nav-text" onclick="get_msgs(\'' + data.new_channel + '\')" href="#" >' + data.new_channel + '</a></li>';
        document.querySelector('#channel_nav').innerHTML = document.querySelector('#channel_nav').innerHTML + nav;
        alert_msg = "New channel " + data.new_channel + "created";
        notify(data.new_channel);

    });
});
