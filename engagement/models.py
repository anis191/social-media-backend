from django.db import models
from users.models import User
from posts.models import Post

class Reaction(models.Model):
    LIKE = 'like'
    LOVE = 'love'
    HAHA = 'haha'
    SAD = 'sad'
    ANGRY = 'angry'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (HAHA, 'Haha'),
        (SAD, 'Sad'),
        (ANGRY, 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES, default=LIKE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

