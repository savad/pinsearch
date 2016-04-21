from rest_framework import serializers


class PinSearchSerializer(serializers.Serializer):
    office_name = serializers.CharField()
    pin_code = serializers.IntegerField()
    office_type = serializers.CharField()
    delivery_status = serializers.CharField()
    division = serializers.CharField()
    region = serializers.CharField()
    circle = serializers.CharField()
    taluk = serializers.CharField()
    district = serializers.CharField()
    state = serializers.CharField()
