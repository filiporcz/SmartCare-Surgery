from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from .forms import LoginForm 

User = get_user_model()

# Create your views here.
def home(request):
    return render(request, "patients/home.html")

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return render(request, 'patients/login.html', {'form': form, 'error': 'Account is disabled.'})
            else:
                return render(request, 'patients/login.html', {'form': form, 'error': 'Invalid login credentials.'})
    else:
        form = LoginForm()
    return render(request, 'patients/login.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            surname = form.cleaned_data["surname"]
            password = form.cleaned_data["password"]
            location = form.cleaned_data.get('location') # Make sure your form has a 'location' field

            # Create the user account
            user = User.objects.create_user(userID=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = surname
            # Here, handle the location data as needed, e.g., saving to user profile
            user.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, "patients/sign_up.html", {'form': form})
    

# @login_required
def dashboard(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        return render(request, "patients/dashboard.html")
    else:
        return redirect("user_login")
    

def weekly_schedule(request):
    return render(request, "patients/weekly_schedule.html")

def prescriptions(request):
    return render(request, "patients/prescriptions.html")

def recent_patients(request):
    return render(request, "patients/recent_patients.html")

def patient_records(request):
    return render(request, "patients/patient_records.html")

def invoices(request):
    return render(request, "patients/invoices.html")

def settings(request):
    return render(request, "patients/settings.html")