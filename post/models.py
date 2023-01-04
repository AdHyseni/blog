from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.get_full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.caption}'

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image= models.FileField(upload_to="posts")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f'{self.title}'

class Comments(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f'{self.user_name} {self.post}'