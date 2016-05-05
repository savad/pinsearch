# Pinsearch
### (Not used Haystack for searching)
A web API interface for Indian Post office pin directory. We can search post office details by following keyword, the output will be the json data.
* office_name
* pin_code
* office_type
* delivery_status
* division
* region
* circle
* taluk
* district
* state

### Installation guide:

In this project we use,

* Django
* django-rest-framework
* elasticsearch

Create a virtual environment and activate.

Clone the repository

`git clone git@github.com:savad/pinsearch.git`

switched to the branch `feature/elastic-search-without-using-haystack`

`cd pinsearch`

`pip install -r requirements.txt`

setup the database settings at `pin/settings.py`

Dump `pin.sql` file to database

Install Elastic search on your machine

For ubuntu ref here https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04

Activate elastic search servie on your machine

`python manage.py migrate  --noinput // For migrating the DB`

`python manage.py collectstatic  --noinput`


`python manage.py index_pin_details // For building search index`

`python manage.py runserver // Run server`



***GET*** : http://localhost:8000/search/?pin_code=670592&&taluk=kannur

```javascipt

{
    "hits": {
        "hits": [
            {
                "_score": 1.0,
                "_type": "pin",
                "_id": "62258",
                "_source": {
                    "office_name": "Kanhirode B.O",
                    "taluk": " Kannur",
                    "district": " Kannur",
                    "division": " Cannanore",
                    "region": " Calicut",
                    "office_type": " B.O",
                    "state": " KERALA",
                    "circle": " Kerala",
                    "delivery_status": " Non-Delivery",
                    "pin_code": " 670592"
                },
                "_index": "my_index"
            }
        ],
        "total": 1,
        "max_score": 1.0
    },
    "_shards": {
        "successful": 4,
        "failed": 0,
        "total": 4
    },
    "took": 75,
    "timed_out": false
}
```


***GET:*** http://localhost:8000/search/?q=chekkikulam
```javascript
{
    "hits": {
        "hits": [
            {
                "_score": 7.9234834,
                "_type": "pin",
                "_id": "62253",
                "_source": {
                    "office_name": "Chekkikulam B.O",
                    "taluk": " Taliparamba",
                    "district": " Kannur",
                    "division": " Cannanore",
                    "region": " Calicut",
                    "office_type": " B.O",
                    "state": " KERALA",
                    "circle": " Kerala",
                    "delivery_status": " Delivery",
                    "pin_code": " 670592"
                },
                "_index": "my_index"
            }
        ],
        "total": 1,
        "max_score": 7.9234834
    },
    "_shards": {
        "successful": 4,
        "failed": 0,
        "total": 4
    },
    "took": 20,
    "timed_out": false
}
```

