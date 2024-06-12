from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputform

# Create your views here.
def factorial(request):
    n=6
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return render(request,'factorial.html',{'param1':fact1,'param2':n})

def square(request):
    num=2
    sq=num*num
    return render(request,'square.html',{'p1':sq,'p2':num})

def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def index(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        permutations = get_possibilities(input_string)
        return render(request, 'index1.html', {'permutations': permutations, 'input_string': input_string})
    return render(request, 'index1.html')  

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'student1.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'student1.html',{'form':form1})

# Factorial for number in range(3,8) 
def factorials(request):
    fact_list = []
    for num in range(3, 8):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        fact_list.append((num, fact))
    return render(request, 'factorials.html', {'fact_list':fact_list})
