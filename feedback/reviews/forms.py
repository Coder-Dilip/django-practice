from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(max_length=100,required=True,label='Your Name',error_messages={
#         'required':'Your name must not be empty',
#         'max_length':'please enter a shorter name'
#     })
#     review_text=forms.CharField(label='your feedback',widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label='Your Rating',min_value=1, max_value=5)



# this is alternative by directly linking models with rendering html 
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        # exclude=['owner_comment']
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"
        }
        error_messages={
            "user_name":{
                "required":"your name must not be empty!",
                "max_length":"please enter a shorter name"
            }
        }
