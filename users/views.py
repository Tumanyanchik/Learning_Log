from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    # Register new user
    if request.method != 'POST':
        # Output emty form
        form = UserCreationForm()
    else:
        # Proccess completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Login and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Output empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
