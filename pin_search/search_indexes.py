import datetime
from haystack import indexes

from models import PostOfficeDetails


class PinIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    office_name = indexes.CharField(model_attr='office_name')
    pin_code = indexes.CharField(model_attr='pin_code')
    office_type = indexes.CharField(model_attr='office_type')
    delivery_status = indexes.CharField(model_attr='office_type')
    division = indexes.CharField(model_attr='division')
    region = indexes.CharField(model_attr='region')
    circle = indexes.CharField(model_attr='circle')
    taluk = indexes.CharField(model_attr='taluk')
    district = indexes.CharField(model_attr='district')
    state = indexes.CharField(model_attr='state')

    def get_model(self):
        return PostOfficeDetails

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
