from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User,Report, Status
from .forms import ReportForm, MyUserCreationForm, UserForm

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('staff-reports')
            else:
                return redirect('user-reports')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('user-reports')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def createReport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        report = form.save(commit=False)
        report.user = request.user
        report.save()
        return redirect('user-reports')

    else:
        form = ReportForm()
    
    context = {'form': form}
    return render(request, 'base/create_report.html', context)


@login_required(login_url='login')
def report(request):
    reports = Report.objects.filter(user=request.user)
    context = {'reports': reports}
    return render(request, 'base/report.html', context)

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
@login_required(login_url='login')
def staffReports(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'base/staff_reports.html', context)

@user_passes_test(is_staff)
@login_required(login_url='login')
def updateReport(request, pk):
    report = Report.objects.get(id=pk)
    form = ReportForm(instance=report)
    status = Status.objects.all()
    
    if request.method == 'POST':
        status_name = request.POST.get('status')
        status, created = Status.objects.get_or_create(name=status_name)
        report.description = request.POST.get('description')
        report.barangay = request.POST.get('barangay')
        report.location = request.POST.get('location')
        report.status = status
        report.save()
        return redirect('staff-reports')
    
    context = {'form': form, 'statuses': status, 'report': report}
    return render(request, 'base/update_report.html', context)



@user_passes_test(is_staff)
@login_required(login_url='login')
def deleteReport(request, pk):
    report = Report.objects.get(id=pk)

    if request.method == 'POST':
        report.delete()
        return redirect('/staff-reports')
    return render(request, 'base/delete.html', {'obj': report})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/update-user.html', {'form': form})
