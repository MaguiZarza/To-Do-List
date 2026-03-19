from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from notes.models import Note


class NotesHomeView(ListView):
    template_name = "notes/notes_home.html"
    model = Note

class CreateNote(CreateView):
    template_name =  "notes/new_note.html"
    model = Note
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('notes_home')
    
class UpdateNote(UpdateView):
    template_name = "notes/update_note.html"
    model = Note
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('notes_home')
    
class DeleteNote(DeleteView):
    template_name = "notes/delete_note.html"
    model = Note
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('notes_home')