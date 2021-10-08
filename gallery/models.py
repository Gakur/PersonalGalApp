from django.db import models

# Create your models here.
class location(models.Model):
    name = models.CharField(max_length=30)


    @classmethod
    def get_location_id(cls, id):
        locations = location.objects.get(pk = id)
        return locations

    def __str__(self):
        return self.name   

    @classmethod
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()     

class category(models.Model):
    name = models.CharField(max_length=30)


    @classmethod
    def get_category_id(cls, id):
        categories = category.objects.name(pk = id)
        return categories

    def __str__(self):
        return self.name  

    
    @classmethod
    def save_category(self):
        self.save()

    def delete_category(self):
        self.save()

    def update_category(self, update):
        self.name = update
        self.save()

          