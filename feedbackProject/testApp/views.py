from django.shortcuts import render
from . import forms

def feedback_view(request):
    if request.method == 'GET':
        form = forms.FeedBackForm()
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("Form Submitted Successfully & Printing Feedback Information")
            print("Student Name:", form.cleaned_data['name'])
            print("Student Roll No.:", form.cleaned_data['rollno'])
            print("Student Email Id:", form.cleaned_data['email'])
            print("Student Feedback:", form.cleaned_data['feedback'])
    #   else:
    #       print("Form is not valid")
    #       print(form.errors)  # Print form errors for debugging
    #else:
    #    form = forms.FeedBackForm() 

    return render(request, 'testApp/feedback.html', {'form': form})
