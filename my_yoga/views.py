from django.shortcuts import render, redirect
from .models import TimetableEntry

def index(request):
    # Your index view logic goes here
    return render(request, 'my_yoga/index.html')

def trainings(request):
    # Your trainings view logic goes here
    return render(request, 'my_yoga/trainings.html')

def timetable(request):
    # Retrieve all timetable entries from the database
    timetable_entries = TimetableEntry.objects.all()
    
    # Pass the timetable entries to the template context
    return render(request, 'my_yoga/timetable.html', {'timetable_entries': timetable_entries})

def nutrition(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/nutrition.html')
    
def khichidi(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/khichidi.html')

def golden_milk(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/golden_milk.html')
def Sambar(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/Sambar.html')
    
def vegetable_soup(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/vegetable_soup.html') 

def side_plank_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/side_plank_pose.html') 
def tree_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/tree_pose.html') 
    
def warrior_pose1(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/warrior_pose1.html') 
    
def bridge_pose(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/bridge_pose.html') 

def bee_breath(request):
    # Your nutrition view logic goes here
    return render(request, 'my_yoga/bee_breath.html')
    
def contacts(request):
    # Your contacts view logic goes here
    return render(request, 'my_yoga/contacts.html')
    
    

#####################################################
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')  # Replace 'home' with your desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'my_yoga/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired URL after signup
    else:
        form = UserCreationForm()
    return render(request, 'my_yoga/signup.html', {'form': form})
