from django.shortcuts import render
#from MTPapp.models import User
from MTPapp.forms import NewUserForm
# Create your views here.
def users(request):
     form=NewUserForm()
     if request.method=="POST":
        form=NewUserForm(request.POST)

     if form.is_valid():
        form.save(commit=True)
        return index(request)
     
     else:
        print("Error Form Invalid")


     return render(request,'users.html',{'form':form})

def index(request):
    return render(request,'index.html')