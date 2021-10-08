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


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    image_description = models.TextField()  
    image_location = models.ForeignKey('location')
    image_category = models.ForeignKey('category')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, image_description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, image_description = image_description ,image_location = image_location,image_category = image_category)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__name__contains=image_category)
        return images

    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(image_location__id=image_location)
        return images_location

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

          