from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):

    # check if user is authenticated o kalaban

    # if request.user.is_authenticated:
    #     redirect('dashboard')

    # check if nag send ng post method

    # if request.method == 'POST':
    #     username = request.POST.get('email')
    #     password = request.POST.get('password')

    #     print(f'username: {username}, password: {password}')

        # authenticate user
        # user = authenticate(request, username=username, password=password)

        # if user is not None:

            # Check if user is admin
        #     if user.is_superuser:
        #         return redirect('page pang admin')

        #     login(request, user)
        #     return redirect('dashboard')
        # else:
        #     return render(request, 'index.html', {'error': 'Invalid credentials'})

    return render(request, 'index.html', {})


def register(request):
    return render(request, 'register.html', {})

def user_logout(request):
    logout(request)
    return redirect('index')



# @login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})

# @login_required
def network(request):
    return render(request, 'network.html', {})

# @login_required
def backlogs(request):
    return render(request, 'backlogs.html', {})

# @login_required
def stats_page(request):
    return render(request, 'stats.html', {})