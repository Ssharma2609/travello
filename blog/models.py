from django.db import models
from django.contrib.auth.models import User


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

# class Comment(models.Model):
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=50)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1) 
    review_text = models.TextField()
    image = models.ImageField(upload_to="review_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.title} ({self.rating}★)"