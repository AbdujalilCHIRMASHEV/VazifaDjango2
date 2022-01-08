from django.shortcuts import render, redirect
from main.models import Yonalish, Student

def Index(request):
    context = {
        "yonalish": Yonalish.objects.all(),
        "student": Student.objects.all(),
    }
    if request.method == 'Post':
        data = request.POST
        Yonalish.objects.create(
            nomi=data.get("nomi")
        )
    return render(request, 'index.html', context)

def AddStudent(request):
    if request.method == "POST":
        data = request.POST
        ismi = data.get('nomi')
        yosh = data.get('yosh')
        yonalish = data.get('yonalish')
        rasm = request.FILES['rasm']
        Student.objects.create(yonalish_id=yonalish, ism=ismi, yoshi=yosh, rasmi = rasm)

    return redirect('index')