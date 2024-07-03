from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
  # Check to see if logging in
  if request.method == 'POST':
    # Get the username and password
    username = request.POST['username']
    password = request.POST['password']
    # Check if the username and password are correct
    user = authenticate(request, username=username, password=password)
    # If the user is correct
    if user is not None:
      # Log in the user
      login(request, user)
      messages.success(request, ('You have been logged in!'))
      return redirect('home')
    else:
      # If the user is not correct
      messages.error(request, ('Error logging in - Please try again'))
      return redirect('home')
  else:
    # If not logging in
    return render(request, 'home.html', {})

def logout_user(request):
  logout(request)
  messages.success(request, ('You have been logged out'))
  return redirect('home')