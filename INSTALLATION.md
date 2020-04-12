# Installation

### Local Installation
This type of installation is better if you want to start customizing shortcuts right away. 
Within a few minutes you should be set up to start making your own shortcuts

* Install [Python](https://www.python.org/downloads/)
* Set up the dependencies using `pip install -r requirements.txt`
⋅⋅* If you run into issues, just install [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
* Start the local web service by running `bash local_run.sh`
* Open settings. Scroll down to the section where it says "Search engine"
* Click 'Manage search engines'. Next to 'Other search engines', click the ADD button 
* Name the 'Search engine' and 'Keyword' field whatever you want. Inside the URL field, paste this: `http://http://127.0.0.1:5000/q/?query=%s`
* Set this search engine to your default

### Web Server Installation
Coming Soon!
