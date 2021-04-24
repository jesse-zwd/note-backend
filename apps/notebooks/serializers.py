from rest_framework import serializers
from django.db.models import Q
# from django.contrib.auth import get_user_model

from .models import Note, Notebook

# User = get_user_model()


class NotebookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Notebook
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = '__all__'


class NotebooksSerializer(serializers.ModelSerializer):
    notes = serializers.SerializerMethodField()

    def get_notes(self, instance):
        notebook_notes = Note.objects.filter(Q(notebook=instance.id)).order_by('-createdAt')
        notes_serializer = NotesSerializer(notebook_notes, many=True, read_only=True)
        return notes_serializer.data
    
    class Meta:
        model = Notebook
        fields = '__all__'
