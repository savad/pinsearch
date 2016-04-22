# pinsearch

### Installation guide:

Create a virtual environment and activate.

Clone the repository
`git clone git@github.com:savad/pinsearch.git`

`cd pinsearch`

`pip install -r requirements.txt`

setup the database settings at `pin/settings.py`

Dump `pin.sql` file to database

Install Elastic search on your machine

For ubuntu ref here https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04

Activate elastic search servie on your machine

`python manage.py migrate  --noinput`

`python manage.py collectstatic  --noinput`

`python manage.py rebuild_index`

`python manage.py runserver`


http://localhost:8000/search/?state=andhra



