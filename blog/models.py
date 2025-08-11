from django.db import models


class Destination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='extra_images')
    image = models.ImageField(upload_to='destinations')

    def __str__(self):
        return f"Image for {self.destination.title}"    

class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.destination.title}"