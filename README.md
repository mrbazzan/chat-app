
# CHAT APPLICATION
    
    A Real time chat application built with Python and jQuery AJAX.

Users in a group can view all the previous messages in a particular ``chat room``. Cool isn't it?

# HOW IT WORKS

![Example](/assets/chat-application.gif)

# HOW TO INSTALL LOCALLY

- Clone the repository
```shell script
git clone https://git@github.com:mrbazzan/chat-app
```

- Change directory
```shell script
cd chat-app
```

- Set up Virtual Environemnt and activate it
```shell script
python3 -m venv venv/
source venv/bin/activate
```

- Install the requirements
```shell script
pip install -r requirements.txt
```

- Then run;
```shell script
python3 manage.py makemigrations
python3 manage.py migrate
 
python3 manage.py runserver
```

[Tutorial Video](https://www.youtube.com/watch?v=IpAk1Eu52GU)
                ^
                |
                |
            Code with Tomi