from rest_framework import serializers
from mj.models import Condition

# Condition Serializer
class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'