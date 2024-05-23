from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
         print(request.method)
         print(request.POST)
         name=request.POST.get('name')
         email=request.POST.get('email')
         contact=request.POST.get('contact')
         password=request.POST.get('password')
         request.session['name']=name
         request.session['email']=email
         request.session['contact']=contact
         request.session['password']=password
    return render(request,'home.html')
#in cookies data save in client side and in session data save in server end 
#in cookies data save in text format and in session data save in encrypted form
# cookies are less secure and session is more secure
def login(request):    
    return render(request,'login.html')
def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        print(email)
        password=request.POST.get('password')
        print(password)
        email1=request.session.get('email')
        print(email1)
        password1=request.session.get('password')
        print(password1)
        name=request.session.get('name')
        print(name)
        contact=request.session.get('contact')
        print(contact)
        if email==email1:
            if password==password1:
                return render(request,'dashboard.html')
        else:
            mssg="Login credential does not match "
            return render(request,'login.html',{'key':mssg})
            
def dashboard(request):
    return render(request,'dashboard.html')
        
   