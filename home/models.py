from django.db import models
from django.urls import reverse
# Create your models here.

# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Users(models.Model):
    """Model representing an author."""
    #user_id = models.AutoField(primary_key=True, serialize=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, null=True)
    degree = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['first_name', 'last_name', 'mobile', 'email', 'degree']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('user_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id},{self.first_name}, {self.last_name}'


# questions model
class Questions(models.Model):
    """Model representing an Questions."""
    #qid = models.AutoField(primary_key=True,serialize=False)
    question = models.CharField(max_length=1000, null=True)
    op1 = models.CharField(max_length=100, null=True)
    op2 = models.CharField(max_length=100, null=True)
    op3 = models.CharField(max_length=100, null=True)
    op4 = models.CharField(max_length=100, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular question instance."""
        return reverse('question_detail', args=[str(self.id)])

    def __str__(self):
        return self.question


# answer model
class Answer(models.Model):
    #uqaid = models.AutoField(primary_key=True,serialize=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    # user_id = models.ForeignKey('Questions', on_delete=models.SET_NULL, null=True)
    # user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    # qid=models.ForeignKey('Questions',on_delete=models.SET_NULL, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.ans

