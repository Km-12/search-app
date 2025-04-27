from django.forms import ModelForm
from .models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ["company", "name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["company"].required = False
        self.fields["name"].required = False
