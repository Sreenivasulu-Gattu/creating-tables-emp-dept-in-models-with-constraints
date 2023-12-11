from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.PositiveIntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    def __str__(self):
        self.a = str(self.deptno) + ' ' + self.dname + ' ' + self.loc
        return self.a

class Emp(models.Model):
    empno = models.PositiveIntegerField(primary_key=True)
    ename = models.CharField(max_length=100,null=False)
    job = models.CharField(max_length=100,null=False)
    mgr = models.PositiveIntegerField(null=False)
    hiredate = models.DateField(null=False)
    sal = models.PositiveIntegerField(null=False)
    comm = models.PositiveIntegerField(blank=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)


    def __str__(self):
        self.a = str(self.empno) + ' ' + self.ename + ' ' + self.job + ' ' + str(self.hiredate) + ' ' + str(self.sal) + ' ' + str(self.comm) + ' ' + str(self.deptno)
        return self.a

class Salgrade(models.Model):
    grade = models.PositiveIntegerField(primary_key=True)
    losal = models.PositiveIntegerField(null=False)
    hisal = models.PositiveIntegerField(null=False)