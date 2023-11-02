from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
    
def start(request):
    greeting = '안녕하세요'
    result = {
        'greeting': greeting,
    }
    return render(request, 'start.html', result)

def root(request): 
    input = request.GET.get('input')
    if input:
        rootnum = int(input) ** 0.5
        if rootnum == int(rootnum):
            rootnum = int(rootnum)
        result = {
            'input': input,
            'rootnum': rootnum,
        }
        return render(request, 'root.html', result)
    else:
        return render(request, 'root.html')
