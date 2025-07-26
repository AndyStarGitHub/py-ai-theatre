# py-ai-theatre
Employer testing task: AI-powered ticket reservation system for a theatre 
via chat interface.


## General information 

The purpose of the project is to create back end of the website where authorised
users can reserve tickets to visit the theatre but through communication
with the AI agent (Smart Assistant, of SA) from the theatre side. The examples 
of sentences that the Smart Assistant (SA) understands are shown below. Any 
user can register at the site and after the registration (s)he can open the 
chat page. 
Users can:
- create request to SA and get responses. 
- see only own chat
- get information on own bookings
- can cancel his own booking
- browse the history of his own chat
- clear the history. 
While booking SA validates if the seat number is correct and 
checks if it is not booked yet.
SA uses the information from the database, not from the chat history.
Seat numbers follow the format XX-Y, where XX is the row number (1–20), 
and Y is the seat letter (A–Q), e.g., 17-F, 5-H.
Only users with admin authorisation can create events (via admin panel). 
In the case you need to create a superuser please use a common Django approach.


## Installation

1. Python3 must be already installed. Python 3.13 used in development.
2. Docker must be installed in case you need to work with dockerized version.


```shell
git clone https://github.com/AndyStarGitHub/py-ai-theatre/
cd py-ai-theatre
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py runserver
```


```Docker shell
docker-compose up --build

The site will be avaliable at http://localhost:8000.

Optional (for setup, only if necessary):
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata events.json

```


## Additional software requirements

The dependencies are listed in requirements.txt. 
Here's a snapshot:

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
3. The admin user can open admin panel at:
    http://127.0.0.1:8000/admin/.
4. The authorized user can open his chat with SA at 
    http://127.0.0.1:8000/chat/.
5. Request examples to SA:
    - Show me the list of events
    - Give me details for Hamlet
    - Book seat 11-N for Macbeth
    - Show all my bookings
    - Cancel seat 11-N for Macbeth
6. Sample screenshot of the active chat: [img.png]. 


## Demo (non-Docker)

1. The project can be cloned from https://github.com/AndyStarGitHub/py-ai-theatre.

2. All migrations shall be completed:
```shell
python manage.py makemigrations
python manage.py migrate
```

3. For your convenience you can load some fake events (optional):

```shell
python manage.py loaddata events.json
```
4. If you have no AI agent exists yet (manual setup), then  
you will have to run the following:

```shell
python scripts/create_assistant.py
  
* You will get Assistant ID, please copy it to .env.

python scripts/update_assistant.py
```
