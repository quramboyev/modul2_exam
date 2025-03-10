from django.db import models

class MainListModel(models.Model):
    img = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.img
    
    class Meta: 
        db_table = 'background_img'
