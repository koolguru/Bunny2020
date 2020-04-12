# Installation

### Local Installation
This type of installation is better if you want to start customizing shortcuts right away. 
Within a few minutes you should be set up to start making your own shortcuts.

Note: I'll make this easier one day, I promise! 

* Install [Python](https://www.python.org/downloads/)
* Set up the dependencies using `pip install -r requirements.txt
  * If you run into issues, just install [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Gunicorn](https://gunicorn.org/)
* Start the app by running `bash run.sh` 
  * This runs Bunny2020 in the background with gunicorn running on a specific port number and display the url used for search queries
  * If you have any issues, or want to test your extensions, run `bash local_run.sh` (This starts flask directly)
* In Chrome, Open settings. Scroll down to the section where it says "Search engine"
* Click 'Manage search engines'. Next to 'Other search engines', click the ADD button 
* Name the 'Search engine' and 'Keyword' field whatever you want. Inside the URL field, paste the url returned from the bash script (e.g `http://127.0.0.1:5000/q/?query=%s`)
* Set this search engine to your default

### Web Server Installation
Coming Soon!
