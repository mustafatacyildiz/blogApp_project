from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='profile_pics', blank=True)

    CATEGORY = [
        ("Django", 'Django'),
        ("React", 'React'),
        ("Agile", 'Agile'),
        ("Html", 'Html'),
        ("Css", 'Css'),
        ("Bootstrap", 'Bootstrap'),
        ("Github", 'Github'),
        ("Mui", 'Mui'),
    ] 
    category = models.CharField(max_length=9, choices=CATEGORY)

    STATUS = [
        ("Draft", 'Draft'),
        ("Publish", 'Publish'),
        ("Private", 'Private'),
    ] 
    status = models.CharField(max_length=7, choices=STATUS, default="Draft")


    def __str__(self):
        return f"{self.title}"


