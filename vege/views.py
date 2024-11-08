from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum

# Create your views here.
@login_required(login_url= "/login")
def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        files = request.FILES
        receipe_image = files.get("receipe_image")

        print(request.POST)
        print()
        print(request.FILES)
        # creating a receipe object
        # receipe = Receipe(receipe_name = receipe_name, receipe_description = receipe_description)
        # receipe.save()

        # alternative way
        Receipe.objects.create(receipe_name = receipe_name , receipe_description = receipe_description, receipe_image = receipe_image)
        # Does below line of code make any sense, it is written in order to refresh the page, or the data of the past form will get erased, but this issue is not happening in my case, data already get erased.
        # return redirect('/receipe') 
    
    return render(request, "vege/receipe.html")

@login_required(login_url= "/login")
def show_receipe(request):
    queryset = Receipe.objects.all()

    # Was just using filter in wrong way, that's why giving receipe_name error
    # and no need of directly specifying request.method == "GET" and all, it will give wrong result as after clicking on show button first request will be get, so it won't print all the items name.

    # if request.method == "GET":
    #     data = request.GET
    #     key = data.get('search')
    #     print("key is ", key)
    #     queryset = queryset.filter(receipe_name__icontains = key)
    #     print("query is", queryset)
    #     context = {"receipes":queryset}
    #     return render(request,"vege/show.html",)


    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__contains = request.GET.get('search'))
    
    context = {"receipes": queryset}
    print(queryset)
    return render(request, "vege/show.html",context)

@login_required(login_url= "/login")
def update_receipe(request,id):
    print("i am inside update function")
    receipe = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        receipe.receipe_name = data.get('receipe_name')
        receipe.receipe_description = data.get('receipe_description')

        files = request.FILES
        receipe_image = files.get("receipe_image")
        if files:
            receipe.receipe_image = receipe_image

        receipe.save()
        return redirect("/show-receipe")
    
    return render(request, "vege/update.html", {"receipe":receipe})

@login_required(login_url= "/login")
def delete_receipe(request,id):
   
    print("i am inside delete function.")
    receipe = Receipe.objects.all().get(id = id)
    
    print(receipe.receipe_name)
    receipe.delete()

    return redirect('/show-receipe')

def get_student_data(request):
    
    # key = request.GET.get('search')
    # if key == None:
    #     student_obj = Student.objects.all()
    

    # else:
        
    #     student_obj = Student.objects.filter(
    #                 Q(student_name__icontains = key)|
    #                 Q(student_age = key) |
    #                 Q(department__department = key)
    #         )
        
    student_obj = Student.objects.all().order_by('student_id__student_id')
    if request.GET.get('search'):
        key= request.GET.get('search')
        try:
            key_int = int(key)
            student_obj = student_obj.filter(Q(student_age=key_int)).order_by('student_id__student_id')
        except ValueError:
            student_obj = student_obj.filter(
                Q(student_name__icontains=key) |
                Q(department__department__icontains=key)
            ).order_by('student_id__student_id')
        
        # print(key,"key is ")
        # print("key type is ",type(key))
        # student_obj = Student.objects.filter(
        #     Q(student_name__contains = key) |
        #     Q(department__department__contains = key) |
        #     Q(student_age = int(key))
        # )

    paginator = Paginator(student_obj, 10)
        
    # Few examples
    # print(paginator.num_pages,"no. of pages is")
    # print(type(paginator.page_range),"count is")
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(request, 'vege/student_db/student_data.html',{'student_obj':page_obj, 'page_obj':page_obj})

def view_marks(request, student_id):

    query_set = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    fail_count = 0
    for query in query_set:
        if query.marks < 33:
            fail_count+=1
        
    total_marks = query_set.aggregate(total_marks  = Sum('marks'))['total_marks']
 
    return render(request,"vege/student_db/student_marks.html",{"query_set":query_set, "total_marks":total_marks,"fail_count":fail_count})