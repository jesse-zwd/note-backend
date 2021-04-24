from rest_framework import mixins, viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Note, Notebook
from .serializers import NotesSerializer, NotebooksSerializer, NotebookSerializer

# Create your views here.

class NotebookViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return NotebookSerializer

        return NotebooksSerializer

    def get_queryset(self):
        return Notebook.objects.filter(user=self.request.user.id).order_by('-createdAt')


class NoteViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    queryset = Note.objects.all().order_by('-createdAt')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotesSerializer
