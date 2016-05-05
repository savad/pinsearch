__author__ = 'savad'
import json
import requests

from django.core.management.base import NoArgsCommand

from pin_search.models import PostOfficeDetails


class Command(NoArgsCommand):
    help = "Getting social feeds in timly basis."

    def handle(self, *args, **options):
        data = {"settings": {
                    "number_of_shards": 4,
                    "number_of_replicas": 1
                },
                "mappings": {
                    "pin": {
                        "properties": {
                            "office_name": {"type": "string", "boost": 4 },
                            "pin_code": {"type": "string", "boost": 2 },
                            "office_type": {"type": "string"},
                            "delivery_status": {"type": "string"},
                            "division": {"type": "string"},
                            "region": {"type": "string"},
                            "circle": {"type": "string"},
                            "taluk": {"type": "string"},
                            "district": {"type": "string"},
                            "state": {"type": "string"},
                        }
                    }
                }
            }
        requests.put('http://127.0.0.1:9200/my_index/', data=json.dumps(data))
        data = ''
        for p in PostOfficeDetails.objects.all():
            data += '{"index": {"_id": "%s"}}\n' % p.pk
            data += json.dumps({ "office_name": p.office_name,
                                 "pin_code": p.pin_code, "office_type": p.office_type,
                                 "delivery_status": p.delivery_status, "division": p.division,
                                 "region": p.region, "circle": p.circle, "taluk": p.taluk,
                                 "district": p.district, "state": p.state
            })+'\n'
        response = requests.put('http://127.0.0.1:9200/my_index/pin/_bulk', data=data)
        print response.text
        print "Success! Search index build completed"
