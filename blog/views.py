from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import ReviewForm
from .models import Destination, DestinationImage

def home(request):
    featured = Destination.objects.filter(is_featured=True)
    return render(request, 'home.html', {'featured': featured})

def destination_detail(request, id):
    dest = get_object_or_404(Destination, pk=id)
    images = DestinationImage.objects.filter(destination=dest)
    reviews = dest.reviews.all().order_by('-created_at') 
    
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.destination = dest
                review.user = request.user
                review.save()
                return redirect('destination_detail', id=dest.id)
            
            else:
                return redirect("login")
            
    else:
        form = ReviewForm()

    return render(request, 'destination_detail.html', {
        'dest': dest,
        'images': images,
        'reviews': reviews,
        'form': form
    })

    # if request.method == 'POST':
    #     if not request.user.is_authenticated:
    #         messages.info(request, 'You must be logged in to comment.')
    #         return redirect('login')
        
    #     name = request.POST.get('name')
    #     comment = request.POST.get('comment')
        
    #     if name and comment:
    #         Comment.objects.create(destination=dest, name=name, comment=comment)
    #         messages.success(request, 'Your comment has been posted.')
    #         return redirect('destination_detail', id=dest.id)

    # return render(request, 'destination_detail.html', 
    #      {'dest': dest, 'images': images})

def login(request):
    if request.method== 'POST':
         username = request.POST['username']
         password = request.POST['password']
         
         user = auth.authenticate(username=username, password= password)
         
         if user is not None:
             auth.login(request, user)
             return redirect('/')
         else:
             messages.info(request, 'Invalid credentials')
             return redirect('login')
    else:
        return render(request, 'login.html')    
        


def register(request): 
    
    if request.method == 'POST':
        # Handle the registration logic here
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']  
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                  messages.info(request,'Username Taken')
                  return redirect('register')
              
              
            elif User.objects.filter(email=email).exists():
                  messages.info(request,'Email Taken')
                  return redirect('register')
              
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created successfully... ')
                return redirect('login')
                
        else:
            messages.info(request, "password not matching....")
            return redirect('register')
            return redirect('home')  # Redirect to home or another page after registration
        
    else:
        return render(request, 'register.html')  # Render the registration template
    
def logout(request):
    auth.logout(request)
    return redirect('/')  # Redirect to home or another page after logout   