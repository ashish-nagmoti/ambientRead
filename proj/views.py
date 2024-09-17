from django.shortcuts import render
from .forms import SignUpForm, UploadFileForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from .models import UserFile
import os
from django.templatetags.static import static
from django.http import JsonResponse
from textblob import TextBlob
from django.contrib.auth.decorators import login_required

def analyze_sentiment(request):
    # Get the text from the request
    text = request.POST.get('text')
    if text is None:
        return JsonResponse({'error': 'No content provided'}, status=201)
    # Perform sentiment analysis with TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Return the sentiment as a JSON response
    print(sentiment)
    return JsonResponse({'sentiment': sentiment})

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = UserFile(file=form.cleaned_data['file'], user=request.user)
           
            user_file.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def library(request):
    user_files = UserFile.objects.filter(user=request.user)
    return render(request, 'library.html',{'user_files':user_files})

def reader(request, book_id):
    # Get the path to the book file
    book_file = get_book_file(book_id)

    # Render the reader.html template with the book file
    return render(request, 'reader.html', {'book_file': book_file})



def get_book_file(book_id):
    book = UserFile.objects.get(id = book_id )
    file_path = book.file.name.split('/')[-1]
    # return book.file.url
    return static(file_path)