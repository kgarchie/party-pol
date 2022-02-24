from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from .models import CustomUser, Party
from django.contrib.auth import login


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('app:party')
    else:
        return render(request, 'registration/login.html')


def party(request):
    parties = Party.objects.all()
    context = {
        'parties': parties,
    }
    return render(request, 'parties.html', context)


@login_required(login_url='/accounts/login/')
def welcomeParty(request, id):
    user = request.user
    db_user = CustomUser.objects.get(email=user.email)
    if db_user.party is None:
        chosen_party = Party.objects.get(id=id)
        db_user.party = chosen_party
        db_user.save()
        context = {
            'Success': 'Successfully Joined New Party',
            'chosen_party': chosen_party,
        }
    else:
        in_party = db_user.party
        context = {
            'party': in_party,
        }
    return render(request, 'welcome.html', context)


def register(request):
    form = UserCreationForm
    context = {
        'form': form,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = CustomUser.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('app:home')
    return render(request, 'register.html', context)
