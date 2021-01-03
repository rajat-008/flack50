# flack50

Flack50 is a chat application served over the web, that was undertaken as a part of the popular online course from Harvard, [CS50W](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/). It is a simple to use app which allows creations of chatrooms to help organize chat.

## Dev Stack

The backend of the app is built in Flask. SocketIO is made use of to perform real-time communication betwee client and server. 

## Instructions to run the app

Building the docker image
```docker
docker build -t flack50 .
docker run -p 80:80 --name my_flack flack50
```

