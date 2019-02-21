from django.db import models
from django.utils import timezone


# Model that creates the Question table in the database.
class Question(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    phonenumber = models.TextField(null=True)
    email =  models.EmailField(null=True)
    state = models.CharField(max_length=200, null=True)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200, null=True)
    course = models.CharField(max_length=200, null=True)
    university_start = models.DateField(null=True)
    university_end = models.DateField(null=True)
    employment_status = models.CharField(max_length=20, null=True)
    parent_employment = models.CharField(max_length=20, null=True)
    prog_knowledge = models.CharField(max_length=20, null=True)
    database_knowledge = models.CharField(max_length=20, null=True)
    operatingsystem_knowledge = models.CharField(max_length=20, null=True)
    othercomputing_courses = models.CharField(max_length=20, null=True)
    benefitof_prog = models.CharField(max_length=20, null=True)
    created_date = models.DateField(default=timezone.now)
    approved_student = models.BooleanField(default=False)
    note = models.TextField(max_length=20, null=True)

    #function that approves a student 
    def approve(self):
        self.approved_student = True
        self.save()

    #function that displays the approved comments 
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
        # return self.comments.get().order_by('-created_date')


    def __str__(self):
        return self.fullname   
         

 # model that creates the Comment table in our database    
class Comment(models.Model):
    post = models.ForeignKey('cloudinter.Question', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return self.text   

