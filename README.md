# Flask-Python-Ajax
## Source code for enabling Ajax in Flask UI Application
### If you are looking for setting up Ajax calls with simple javascript on Flask Application here is a sample code.

Whole idea behind this is 1) create a seperate URI in Python/Flask application for tracking the progress of workload 2) call the URI in your html page using Ajax at specificed intervals of time (say 200ms) to provide status to User


### What is different ?

If you dont want to go for jQuery or equivalent just to provide a simple ajax response you can go with this approach 


### Usage

Suitable for time consuming UIs which do multiple tasks at once(e.g an Upload UI with multiple steps or running batch mode workload) 


### Requirements:

Python

Javascript

HTML

Pace.js(optional)

Set your Flask application to operate in Multi-thread mode 


### Pace.js:
It provides nice visualization when the page gets loaded or redirected . Refer http://github.hubspot.com/pace/docs/welcome/ for more info on Pace.js
