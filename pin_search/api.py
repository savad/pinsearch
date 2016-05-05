import requests
import json

from rest_framework.response import Response
from rest_framework.views import APIView


class PinSearchAPIView(APIView):
    """
    View for searching Pin Directory
    """

    def get(self, request, *args, **kwargs):
        query = request.GET.dict()
        data = self.get_search_query(query)
        response = requests.post('http://127.0.0.1:9200/my_index/pin/_search', data=json.dumps(data))
        return Response(response.json())

    def get_search_query(self, user_query):
        """
        Creating search query
        :param user_query:
        :return: elastic search query dict
        """
        query, base_query = {}, {}
        base_query = {"query_string": {"query": user_query.get('q')}} if user_query.get("q")\
            else {"match_all": {}}
        filter_query = []
        for k, v in user_query.iteritems():
            flag = True
            if not k in ['state', 'district', 'taluk', 'circle', 'region', 'division',
                         'delivery_status', 'pin_code', 'office_name']:
                flag = False
            if flag:
                filter_by_field = {"query": {"match": {k: {"query": v}}}}
                filter_query.append(filter_by_field)
        query["query"] = {"filtered": {"query": base_query, "filter": {"bool": {"must": filter_query}}}}
        return query
