from rest_framework import serializers
from fibonacci.models import Fibonacci


class FibonacciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fibonacci
        fields = ['id', 'total', 'resultado', 'created', 'status']