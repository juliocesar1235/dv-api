from rest_framework import serializers

from .models import Zipcode

class ZipcodeSerializer(serializers.ModelSerializer):
    zipcode = serializers.CharField(max_length=200, required=True)
    settlement = serializers.CharField(max_length=500, required=True)
    settlement_type = serializers.CharField(max_length=200, required=True)
    municipality = serializers.CharField(max_length=200, required=True)
    state = serializers.CharField(max_length=200, required=True)
    settlement_zipcode = serializers.CharField(max_length=200, required=True)
    state_code = serializers.IntegerField(required=True)
    office_zipcode = serializers.CharField(max_length=200, required=True)
    settlement_type_code = serializers.CharField(max_length=50, required=True)
    municipality_code = serializers.IntegerField(required=True)
    settlement_id = serializers.IntegerField(required=True)
    zone = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        return Zipcode.objects.create(
            zipcode = validated_data.get('zipcode'),
            settlement = validated_data.get('settlement'),
            settlement_type = validated_data.get('settlement_type'),
            municipality = validated_data.get('municipality'),
            state = validated_data.get('state'),
            city = validated_data.get('city'),
            settlement_zipcode = validated_data.get('settlement_zipcode'),
            state_code = validated_data.get('state_code'),
            office_zipcode = validated_data.get('office_zipcode'),
            settlement_type_code = validated_data.get('settlement_type_code'),
            municipality_code = validated_data.get('municipality_code'),
            settlement_id = validated_data.get('settlement_id'),
            zone = validated_data.get('zone'),
            city_code = validated_data.get('city_code')
        )

    class Meta:
        model = Zipcode
        fields = (
            'id',
            'zipcode',
            'settlement',
            'settlement_type',
            'municipality',
            'state',
            'city',
            'settlement_zipcode',
            'state_code',
            'office_zipcode',
            'settlement_type_code',
            'municipality_code',
            'settlement_id',
            'zone',
            'city_code'
        )


