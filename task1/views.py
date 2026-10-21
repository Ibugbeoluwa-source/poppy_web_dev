from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewTaskForm
# Create your views here.

tasks = ["Learn Python", "Learn Django", "Build"]
context = {"tasks": tasks}
def index(request):
    # return HttpResponse("Welcome world!!")
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "task1.html/index.html", {
        "tasks": request.session["task"]
    })

# after validation:
#request.session["tasks"] += [tasks]


def task(request):
    return render(request, "task1/home.html", context)

def AboutUs(request):
    return render(request, "task1/AboutUs.html")

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append("Learn Django")
            # tasks.append(task)
    
        else:
            return render(request,"task1/form.html", 
                          {
                    "form": form}
                    )
    return render(request, "task1/form.html", {
        "form": NewTaskForm()
    })

