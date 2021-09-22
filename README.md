made so that I can get NYTimes recipes past the paywall

everything is super scuffed

front end is raw html with bootstrap

backend is flask

had to finangle some stuff to make it work on elastic beanstalk

run locally by calling 
```
export FLASK_APP = application
flask run
```
I'm not tryna host this on AWS for perpetuity cuz it's expensive

# YEP

Learnings
- needed to add requirements.txt
- easiest to just add application.py as a dummy that calls existing flask module
- something something virtual environments
