from django.shortcuts import render

# Create your views here.
def register(request):
    context = {
        'title': 'Register - Echo',
    }
    return render(request, 'accounts/register.html', context);