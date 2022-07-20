from django.shortcuts import redirect, render

from Appstudnt.models import studentDetails
  

# Create your views here.


#Load addstudent.html Page........
def addStudent(request):
    return render(request,'addstudent.html')

#Enter student Details...
def add_student_details(request):
    if request.method=='POST':
        sname=request.POST['student_name']
        address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['joining_date']
        email=request.POST['email']
        quali=request.POST['qualification']
        gender=request.POST['gender']
        
        
        
        student=studentDetails(student_name=sname,
                               address=address,
                               age=age,
                               joining_date=jdate,
                               email=email,
                               qualification=quali,
                               gender=gender)
                               
                               
        student.save()
        print("hii")
        return redirect('show_students')
         
        
         #Show student Details...
def show_students(request):
    students=studentDetails.objects.all()
    return render(request,'student.html',{'student':students})

def show(request,pk):
    students=studentDetails.objects.get(id=pk)
    return render(request,'show.html',{'students':students})

#Load Edit Page....
def editpage(request,pk):
    students=studentDetails.objects.get(id=pk) 
    return render(request,'edit.html',{'students':students})

#Editing..
def edit_student_details(request,pk):
    if request.method=='POST':
        students = studentDetails.objects.get(id=pk)
        students.student_name = request.POST.get('student_name')
        students.address=request.POST.get('address')
        students.age=request.POST.get('age')
        students.joining_date=request.POST.get('joining_date')
        students.email = request.POST.get('email')
        students.qualification = request.POST.get('qualification')
        students.gender=request.POST.get('gender')
       
        students.save()
        return redirect('show_students')
    return render(request, 'edit.html',)


#Load delete Page...
def deletepage(request,pk):
    students=studentDetails.objects.get(id=pk)
    return render(request,'delete.html',{'students':students})

#Deleting Product Element..
def delete_student(request,pk):
    students=studentDetails.objects.get(id=pk)
    students.delete()
    return redirect('show_students')

def load_index_page(request,pk):
    return render(request,'index.html')
    


