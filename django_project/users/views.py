from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #save the user
            form.save()

            username = form.cleaned_data.get('username')    # valid data stored in 'cleaned data' dictionary
            messages.success(request, f'Account created for {username}!')
            
            # re-direct user back to home page
            return redirect('blog-home')
           

    else:   # GET request
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


