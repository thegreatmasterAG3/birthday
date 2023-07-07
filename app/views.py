from django.shortcuts import render

# Create your views here.
def HOME(request):
    return render(request,'home.html')




def INDEX(request):
    return render(request, 'index.html')

def INDEX1(request):
    return render(request,'index1.html')
