from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category = models.CharField(max_length=50)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)

    @property
    def rating_average(self):
        sum = 0
        ratings = Rating.objects.filter(video=self)
        for rating in ratings:
            sum = sum + rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    @property
    def comment_list(self):
        comments = Rating.objects.filter(video=self)
        comment_list = []
        for comment in comments:
            comment_list.append(comment.comments)
        return comment_list

    def __str__(self):
        return self.title


class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE,
                              related_name='video_stars')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = (('user', 'video'),)
        index_together = (('user', 'video'),)

    def __str__(self):
        return self.video.title
