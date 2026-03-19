from django.urls import path
from notes.views import NotesHomeView, CreateNote, UpdateNote, DeleteNote

urlpatterns = [
    path('', NotesHomeView.as_view(), name='notes_home'),
    path('new/', CreateNote.as_view(), name='crear_nota' ),
    path('edit/<int:pk>', UpdateNote.as_view(), name='editar_nota'),
    path('delete/<int:pk>', DeleteNote.as_view(), name='eliminar_nota'),
]