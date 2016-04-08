 Implementing Interview process using Django
============================================
Django application that provides Interview process with Single Sign On/OAuth feature for your project. 

There are 3 interviewers interviewing multiple candidates. They would rate each candidate between 1 to 5. They don't want others opinion bias their own. They are allowed to enter the rating for each candidate and can see the rating they have given. At the end of the interview process, all must enter their credentials to see the rank of each candidate. Try using Single Sign On/OAuth, Google Docs or any open source technologies to demo your expertise.

Installation
=======================
The dependent packages:

PyJWT==0.3.0
oauthlib==0.7.1
python-openid==2.2.5
python-social-auth==0.2.1
requests==2.4.3
requests-oauthlib==0.4.2
six==1.8.0
wsgiref==0.1.2

Install with pip



DEMO
=====
Interviewers
------------

Interviewer1

username: demo_001
password: 12345

Interviewer2

username: demo_002
password: 12345

Interviewer3

username: demo_003
password: 12345


Candidates
-----------

candidate1

username: test1
password: 12345

candidate2

username: test2
password: 12345

candidate3

username: test3
password: 12345

candidate4

username: test4
password: 12345

candidate5

username: test5
password: 12345


 

Usage
=====
In this project there are 3 interviewers, each interviewer can enter  candidate id and enter mark. Candidate register our profile to my site id can be automatically generated.(candidate id like CA10001,CA10002 .....). Candidate pages show Candidate id and rank. Interviewers page has entry of each candidate and generate report.

Candidate and interviewer can be registered using normal registration or Single sign on/oauth2









Deploy and Run the Webserver:

$ python manage.py runserver

Open the project:

To access the url "http://localhost:8000/"

Add the user using to access the url "http://localhost:8000/admin" (Username: amp, Password: diamond)





