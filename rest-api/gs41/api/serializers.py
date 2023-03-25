from rest_framework import serializers
from .models import Singer,Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedfield(many=True, read_only=True)
    # song = serializers.PrimaryRelatedfield(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedfield(many=True, read_only=True, view_name='song_detail')
    song = serializers.SlugRelatedfield(many=True, read_only=True, slug_field='title')
    class Meta:
        model = Singer
        fields = ['id','name','title','gender']