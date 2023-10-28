#tạo model(đoạn class, đoạn from..import có sẵn r)
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass 


class BaseModel(models.Model):
    #null=True for nếu thêm 3 cái mới vào, ta điền dữ liệu gì vào đấy => thêm null(giải pháp 2)/ thêm giá trị mặc định (giải pháp 1)
    created_date = models.DateField(auto_now_add=True, null = True)
    updated_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default = True) #không thêm null=True vì nó là mặc định


    #ngăn việc tự nhiên tạo thêm 2 bảng mới
    class Meta:
        abstract = True #lớp này bị hóa trừu tượng


#tập trung cái này
class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)


    def __str__(self):
        return self.name
    

class Course(BaseModel):
    subject = models.CharField(max_length=255,null=False)
    desc = models.TextField()
    image = models.CharField(max_length=100) #nơi chứa đường dẫn ảnh của khóa học
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#on_delete khi xóa khóa học nó sẽ ntn (thầy hay hỏi), 2 cái đấy bắt buộc


    def __str__(self):
        return self.subject 