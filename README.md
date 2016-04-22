# Pinsearch
A web app for Indian Post office pin directory. We can search post office details by following keyword
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



***GET*** : http://localhost:8000/search/?region=Hyderabad

```javascipt

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "office_name": " Kodad B.O\"",
            "pin_code": 508206,
            "office_type": "B.O",
            "delivery_status": "B.O",
            "division": "Suryapet",
            "region": "Hyderabad",
            "circle": "Andhra Pradesh",
            "taluk": "Huzurnagar",
            "district": "Nalgonda",
            "state": "ANDHRA PRADESH"
        }
    ]
}
```


***GET:*** http://localhost:8000/search/?circle=Rajasthan&&state=RAJASTHAN
```javascript
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "office_name": "12 S.O\"",
            "pin_code": 302017,
            "office_type": "S.O",
            "delivery_status": "S.O",
            "division": "Jaipur City",
            "region": "Jaipur HQ",
            "circle": "Rajasthan",
            "taluk": "Jaipur",
            "district": "Jaipur",
            "state": "RAJASTHAN"
        },
        {
            "office_name": "rajgarh S.O\"",
            "pin_code": 301408,
            "office_type": "S.O",
            "delivery_status": "S.O",
            "division": "Alwar",
            "region": "Jaipur HQ",
            "circle": "Rajasthan",
            "taluk": "Rajgarh",
            "district": "Alwar",
            "state": "RAJASTHAN"
        },
        {
            "office_name": "Bandar Sindari S.O\"",
            "pin_code": 305817,
            "office_type": "S.O",
            "delivery_status": "S.O",
            "division": "Ajmer",
            "region": "Ajmer",
            "circle": "Rajasthan",
            "taluk": "Kishangarh",
            "district": "Ajmer",
            "state": "RAJASTHAN"
        }
    ]
}
```

