from django.shortcuts import render
from .models import Users,Questions,Answer
from django.db import IntegrityError, transaction
from .forms import *
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def assessment(request):
    if request.method == 'POST':

        return render(request, 'assessment.html')
    else:
        questions = Questions.objects.all()
        print(questions)
        context = {
            'hquestions': questions
        }
        return render(request, 'assessment.html',context=context)





def Registration(request):
    if request.method == 'POST':
        #user_id = request['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile=request.POST['mobile']
        email = request.POST['email']
        degree=request.POST['degree']
        print(first_name,last_name,mobile,email,degree)

        # print(fname,lname,email)
        context = {'error': False}
        try:
            #Users.objects.create( first_name=first_name, last_name=last_name, mobile=mobile,email=email,degree=degree)

            user = Users()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.mobile=mobile
            user.degree=degree
            user.save()
            print("user object created")

        except IntegrityError:
            print("Integrity Error")
            # print([p.pub_date for p in queryset])
            context['error'] = "Integrity error"
        except Exception as e:
            print("exception e",e)
            context['error'] = e
        finally:
            print("Entered into finally")
            users_retrived = Users.objects.all()
            # print([p.first_name for p in users_retrived])
            # print([p.pub_date for p in queryset])
            context['Users'] = users_retrived
        # print(user.validate_unique())
        print(context)

        # print(users_retrived)
        # for value in range(users_retrived.count()):
        # print(users_retrived.field_object)
        return render(request, 'index.html', context=context)

    else:
        return render(request, 'index.html')



def addQuestion(request):
    #if request.user.is_staff:
    form = addQuestionform()
    if (request.method == 'POST'):
        form = addQuestionform(request.POST)
        if (form.is_valid()):
            form.save()
            #return redirect('/')
            return render(request, 'index.html')
    context = {'form': form}
    return render(request, 'addQuestion.html',context)
    #else:
        #return render(request, 'index.html')



def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'home/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home/assessment.html',context)

