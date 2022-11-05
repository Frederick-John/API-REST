from rest_framework import serializers
from .models import Song
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["first_name","last_name","age","Artiste", "title", "date_realeased", "likes", "artiste_id","Song","content","song_id"]