from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):

    board_id = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    class Meta:
        model = Board
        fields = '__all__'