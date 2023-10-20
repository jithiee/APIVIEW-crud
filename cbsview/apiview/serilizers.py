from rest_framework import serializers
from apiview . models import Student

class Studenterializers(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = [
            'id',
            'name',
            'roll',
            'city',
            
            
        ]
 