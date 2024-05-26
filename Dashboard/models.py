from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY =(
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),
)

class Product(models.Model):
    name= models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity=models.PositiveIntegerField(null=True)


    

   # class Meta:
     #   verbose_name = _("")
#        verbose_name_plural = _("s")

    def __str__(self):
        return f'{self.name}'

  #  def get_absolute_url(self):
   #     return reverse("_detail", kwargs={"pk": self.pk})
