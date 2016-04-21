from rest_framework import viewsets
from haystack.query import SearchQuerySet, EmptySearchQuerySet

from serializers import PinSearchSerializer
from models import PostOfficeDetails


class PinSearchViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get']
    queryset = PostOfficeDetails.objects.all()
    serializer_class = PinSearchSerializer

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = EmptySearchQuerySet()
        query = request.GET.dict()
        flag = True
        for k, v in query.iteritems():
            if not k in ['q', 'state', 'district', 'taluk', 'circle', 'region', 'division',
                         'delivery_status', 'pin_code', 'office_name']:
                flag = False
        if flag:
            query['content'] = query.pop('q')
            queryset = SearchQuerySet().filter(**query)
        return queryset
