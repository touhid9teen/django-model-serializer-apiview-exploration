# -------------------Basic Serializer:
from rest_framework import serializers
from .models import Alumni

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'


#------------------- Serializer with ForeignKey:

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name', 'email']  # Customize as needed

class AlumniWithMentorSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = Alumni
        fields = '__all__'


# -------------------------Serializer with ManyToManyField:

class AlumniNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name', 'email']  # Customize as needed

class AlumniWithNetworkSerializer(serializers.ModelSerializer):
    alumni_network = AlumniNetworkSerializer(many=True, read_only=True)

    class Meta:
        model = Alumni
        fields = '__all__'

#----------------------------------Serializer with OneToOneField:


class OneToOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name', 'email']  # Customize as needed

class AlumniWithOneToOneSerializer(serializers.ModelSerializer):
    one_to_one = OneToOneSerializer(read_only=True)

    class Meta:
        model = Alumni
        fields = '__all__'



