from django import forms
from .models import Post, Command
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'tag')

class CommandForm(forms.Form):
    title_command = forms.CharField(max_length=50)
    command = forms.CharField(widget=forms.Textarea)

    def save_form(self, post):
        print(self.cleaned_data)
        command = Command()
        command.title_command = self.cleaned_data["title_command"]
        command.command = self.cleaned_data["command"]
        command.post = post
        command.save()

    def clean_title_command(self):
        title_command = self.cleaned_data['title_command']
        if "coba" in title_command:
             raise ValidationError("Jangan memakai kata coba")
        return title_command

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title_command')
        command = cleaned_data.get('command')

        if title and command:
            if "coba" in command and "coba" in title:
                raise ValidationError("Jangan memakai kata coba di title dan isi command")
