from django.shortcuts import render

# Create your views here.


def home(request):

    context = {'home': home}

    return render(request, 'index.html', context)

def new_account(request):

    context = {'new_account' : new_account}
    return render(request, 'newaccount.html', context)  

def passwordreset(request):

    # context = { 'passwordreset':passwordreset}
    return render(request, 'passwordreset.html')  

def signin(request):
    return render(request, 'signin.html')       

# def team(request):

#     return render(request, 'team.html')

def Team(request):

    return render(request, 'team.html')

# def index(request):
#     return render(request, '1index.html')        
