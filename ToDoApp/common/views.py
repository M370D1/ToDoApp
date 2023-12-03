from django.shortcuts import render

from ToDoApp.accounts.forms import UserLoginForm


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserLoginForm()

    return render(request, 'home-page.html', {'form': form})
