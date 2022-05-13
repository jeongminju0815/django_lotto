from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.
def index(request):
    #models.py에서 진행한 내용을 views.py에서 진행해도 ok"
    lottos=GuessNumbers.objects.all()

    return render(request, "lotto/default.html",{"lottos":lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):

    if request.method == "POST":
        form=PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect("index")



        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_test)
        # row.generate() # self.save()




        # print("\n\n\n\n\n\======================\n\n\n\n\n")
        # print(request.POST)
        # print(type(request.POST))
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print("\n\n\n\n\n\======================\n\n\n\n\n")
        # form=PostForm()
        # return render(request, "lotto/form.html",{"form":form})
    else:
        form=PostForm()
        return render(request, "lotto/form.html",{"form":form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey) #pk=id
    return render(request, 'lotto/detail.html', {'lotto':lotto})
