from django import forms
School =(
    ("1", "A İlköğretim Okulu"),
    ("2", "B İlköğretim Okulu"),
    ("3", "C İlköğretim Okulu"),
)
jobT =(
    ("Müdür", "Müdür"),
    ("Öğretmen", "Öğretmen"),
    ("Öğrenci", "Öğrenci"),
)
Class =(
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50 , label="Adınız")
    usersurname=forms.CharField(max_length=50,label="Soyadınız")
    password=forms.CharField(max_length=20,label="Parolanız",widget=forms.PasswordInput)
    JobType=forms.MultipleChoiceField(choices = jobT,label="Göreviniz")
    #confirm=forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    SchoolType= forms.MultipleChoiceField(choices = School,label="Okulunuz")
    ClassType= forms.MultipleChoiceField(choices = Class,label="Sınıfınız")
     
    
   

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50 , label="Adınız")
    password=forms.CharField(max_length=20,label="Parolanız",widget=forms.PasswordInput)
    #schoolId=forms.MultipleChoiceField(required=False, label="Okulunuz",widget=forms.CheckboxSelectMultiple, choices=SCHOOL_CHOICES)

class UpdateFormTeacher(forms.Form):
    username = forms.CharField(max_length = 50 , label="Adınız")
    usersurname=forms.CharField(max_length=50,label="Soyadınız")
    #confirm=forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    ClassType= forms.MultipleChoiceField(choices = Class,label="Sınıfınız")

class UpdateFormStudent(forms.Form):
    username = forms.CharField(max_length = 50 , label="Adınız")
    usersurname=forms.CharField(max_length=50,label="Soyadınız")
    #confirm=forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    ClassType= forms.MultipleChoiceField(choices = Class,label="Sınıfınız")

