from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm , LoginForm ,UpdateFormStudent,UpdateFormTeacher
from django.contrib import messages
from django.contrib.auth import authenticate
from student.models import Student
from teacher.models import Teacher
from schoolManager.models import SchoolManager
from django.core.exceptions import ObjectDoesNotExist



def manager (request,data):
    schoolid=SchoolManager.objects.get(id=data).schoolId
    name=SchoolManager.objects.get(id=data).name
    count=0
    newString=""
    for i in name:
        if count == 0 :
            newString+=i.upper()
        else:
            newString+=i.lower()
        count+=1

    contextT=Teacher.objects.all().filter(schoolId=schoolid)
    contextS=Student.objects.all().filter(schoolId=schoolid)
    DictTeacher={}
    print(schoolid," ",contextS, " ",contextT)
    DictTeacher["name"]=newString
    DictTeacher["contentT"]=contextT
    DictTeacher["contentS"]=contextS
    return render(request,"SchoolManager.html",DictTeacher)

def teacher (request,data):
    
    name=Teacher.objects.get(id=data).name
    count=0
    newString=""
    for i in name:
        if count == 0 :
            newString+=i.upper()
        else:
            newString+=i.lower()
        count+=1
    schoolid=Teacher.objects.get(id=data).schoolId
    classid=Teacher.objects.get(id=data).classId
    contextS=Student.objects.all().filter(schoolId=schoolid,classId=classid)
    print(contextS)
    DictTeacher={}
    DictTeacher["name"]=newString
    DictTeacher["contentS"]=contextS
    
    return render(request,"Teacher.html",DictTeacher)


def student(request,data):
    count=0
    newString=""
    for i in data:
        if count == 0 :
            newString+=i.upper()
        else:
            newString+=i.lower()
        count+=1
    StudentName = {
            "name" : newString
        }
    return render(request,"Student.html",StudentName)

def register (request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        surname=form.cleaned_data.get("usersurname")
        password = form.cleaned_data.get("password")
        classId=form.cleaned_data.get("ClassType")
        SchoolId=form.cleaned_data.get("SchoolType")
        job=form.cleaned_data.get("JobType")
        print(job[0])

        
        if job[0] == "Öğrenci":
            try:
                StudentControl=Student.objects.get(name=username,password=password)
            except ObjectDoesNotExist:
                StudentControl = None
            print(StudentControl)
            if StudentControl == None:
                newUser = Student(name=username,surname=surname,schoolId=SchoolId[0],password=password,classId=classId[0])
                newUser.save()
                messages.success(request,"Başarıyla kayıt olundu.")
                return redirect("student",data=newUser.name)
            else:
                messages.info(request,"Aynı isim ve şifreyeye sahip öğrenci bulunmaktadır.Lütfen farklı şifre deneyiniz.")

        elif job[0] == "Öğretmen":
            try:
                TeacherControl=Teacher.objects.get(classId=classId[0],schoolId=SchoolId[0])
            except ObjectDoesNotExist:
                TeacherControl = None
            
            if TeacherControl == None:
                newUser= Teacher(name=username,surname=surname,schoolId=SchoolId[0],password=password,classId=classId[0])
                newUser.save()
                messages.success(request,"Başarıyla kayıt olundu.")
                return redirect("teacher",data=newUser.id)
            else:
                messages.info(request,"Bu sınıfın öğretmeni mevcuttur.")
            
            
        elif job[0] =="Müdür":
            try:
                ManagerControl=SchoolManager.objects.get(schoolId=SchoolId[0])
            except ObjectDoesNotExist:
                ManagerControl = None
            if ManagerControl == None:
                newUser= SchoolManager(name=username,surname=surname,schoolId=SchoolId[0],password=password)
                newUser.save()
                messages.success(request,"Başarıyla kayıt olundu.")
                return redirect("manager",data=newUser.id)
            else:
                messages.info(request,"Bu okulun müdürü mevcuttur.")
        
        

        
    context = {
            "form" : form
        }
    
    return render(request,"register.html",context)

def login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        
        try:
            controlS=Student.objects.get(name=username,password=password)
        except ObjectDoesNotExist:
            controlS = None
        try:
            controlM=SchoolManager.objects.get(name=username,password=password)
        except ObjectDoesNotExist:
            controlM = None
        try:
            controlT=Teacher.objects.get(name=username,password=password)
        except ObjectDoesNotExist:
            controlT = None
        
        if controlS is not None:
            messages.success(request,"Başarıyla giriş yapıldı")
            return redirect("student",data=controlS.name)
        elif controlM is not None:
            messages.success(request,"Başarıyla giriş yapıldı")
            return redirect("manager",data=controlM.id)
        elif controlT is not None:
            messages.success(request,"Başarıyla giriş yapıldı")
            return redirect("teacher",data=controlT.id)
        else:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        
        
    return render(request,"login.html",context)
def logout(request):
    
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

def updateTeacher(request,data):
    form = UpdateFormTeacher(request.POST or None)
    if form.is_valid():
        teacherUpdate=Teacher.objects.get(id=data)
        teacherUpdate.name=form.cleaned_data.get("username")
        print("*****",teacherUpdate.name)
        teacherUpdate.surname=form.cleaned_data.get("usersurname")
        teacherUpdate.classId=form.cleaned_data.get("ClassType")
        teacherUpdate.classId=teacherUpdate.classId[0]
        teacherUpdate.save()
        print("-------",teacherUpdate.schoolId)
        managerId=SchoolManager.objects.get(schoolId=teacherUpdate.schoolId).id
        return redirect("manager",managerId)
       

    return render(request,"update.html",{"form" : form})

def deleteTeacher(request,data):
    school=Teacher.objects.get(id=data).schoolId
    Teacher.objects.filter(id=data).delete()    
    managerId=SchoolManager.objects.get(schoolId=school).id
    return redirect("manager",managerId)

def updateStudent(request,data):
    form = UpdateFormStudent(request.POST or None)
    if form.is_valid():
        studentUpdate=Student.objects.get(id=data)
        studentUpdate.name=form.cleaned_data.get("username")
        studentUpdate.surname=form.cleaned_data.get("usersurname")
        studentUpdate.classId=form.cleaned_data.get("ClassType")
        studentUpdate.classId=studentUpdate.classId[0]
        studentUpdate.save()
        managerId=SchoolManager.objects.get(schoolId=studentUpdate.schoolId).id
        return redirect("manager",managerId)
       

    return render(request,"update.html",{"form" : form})

def deleteStudent(request,data):
    school=Student.objects.get(id=data).schoolId
    Student.objects.filter(id=data).delete()    
    managerId=SchoolManager.objects.get(schoolId=school).id
    return redirect("manager",managerId)

def updateStudentTe(request,data):
    form = UpdateFormStudent(request.POST or None)
    if form.is_valid():
        studentUpdate=Student.objects.get(id=data)
        studentUpdate.name=form.cleaned_data.get("username")
        print(studentUpdate.name)
        studentUpdate.surname=form.cleaned_data.get("usersurname")
        studentUpdate.classId=form.cleaned_data.get("ClassType")
        studentUpdate.classId=studentUpdate.classId[0]
        studentUpdate.save()
        TeacherId=Teacher.objects.get(classId=studentUpdate.classId).id
        return redirect("teacher",TeacherId)
       

    return render(request,"update.html",{"form" : form})

def deleteStudentTe(request,data):
    classnum=Student.objects.get(id=data).classId
    Student.objects.filter(id=data).delete()    
    teacherr=Teacher.objects.get(classId=classnum).id
    return redirect("teacher",teacherr)