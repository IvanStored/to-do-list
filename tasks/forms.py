from django import forms

from tasks.models import Tag, Task


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Your task"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )
