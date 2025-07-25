# py-ai-theatre
Employer testing task. Website for theatre tickets reservation using AI chat.


## General information 

The purpose of the project is to create back end of the website where authorised
users can reserve tickets to visit the theatre but through the communication
with the AI agent (Smart Assistant, of SA) from the theatre side. The examples of sentences 
that SA understand provided lower. Any user can register at the site and after the 
registration (s)he can open the chat page. User can create request to SA and
get responses. User can see only own chat and receive information on own
booking. User can cancel his own booking. While booking SA validates if the seat
number is correct and checks if it is not booked yet. User can browse history of his
own chat and can clear the history.
Only users with admin authorisation can create events. In the case you need to
create a superuser please use common Python approach.
SA uses the information from the database, not from tha chat history.
The seat numbers use format XX-Y where XX is a row (1 - 20), and Y the number
of seat in the row (A - Q), e.g. 17-F, 5-H.


## Installation

1. Python3 must be already installed. Python 3.13 used in development.
2. Docker must be installed in the case you need to work with dockerized version.


```shell
git clone https://github.com/AndyStarGitHub/py-ai-theatre/
cd py-stadium
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py runserver
```


```Docker shell
7777777777777777
```


## Additional software requirements
annotated-types==0.7.0
anyio==4.9.0
asgiref==3.9.1
certifi==2025.7.14
colorama==0.4.6
crispy-bootstrap5==2025.6
distro==1.9.0
Django==5.2.4
django-crispy-forms==2.4
dotenv==0.9.9
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
jiter==0.10.0
openai==1.97.1
pydantic==2.11.7
pydantic_core==2.33.2
python-dotenv==1.1.1
sniffio==1.3.1
sqlparse==0.5.3
tqdm==4.67.1
typing-inspection==0.4.1
typing_extensions==4.14.1
tzdata==2025.2


## Features

1. Any user can register at the site at 
    http://127.0.0.1:8000/accounts/signup/.
2. The registered user can sign in at
    http://127.0.0.1:8000/accounts/login/.
3. The admin user can oped admin panel at:
    http://127.0.0.1:8000/admin/.
4. The authorized user can open his chat with SA at 
    http://127.0.0.1:8000/chat/.
5. Request examples to SA:
    - Show me the list of events
    - Give me details for Hamlet
    - Book seat 11-N for Macbeth
    - Show all my bookings
    - Cancel seat 11-N for Macbeth


## Demo

The project can be cloned from https://github.com/AndyStarGitHub/py-stadium.

Training database has been populated with faked data. 

To login as a superuser with the credentials:
    Login: super@stadium.mate
    Password: ueur!!77eeen


## Run with Docker

Docker must be installed.
To run the commands:
    docker-compose build
    docker-compose up



