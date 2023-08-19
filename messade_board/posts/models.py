from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=False)


class Category(models.Model):
    TANK = 'TN'
    HEAL = 'HL'
    DD = 'DD'
    TRADER = 'TR'
    GUILD_MASTER = 'GM'
    QUEST_GIVER = 'QG'
    BLACKSMITH = 'BS'
    TANNER = 'TN'
    POTIONS_MASTER = 'PM'
    SPELL_MASTER = 'SM'

    CATEGORY_CHOICE = [
        (TANK, 'Танк'),
        (HEAL, 'Хил'),
        (DD, 'ДД'),
        (TRADER, 'Торговец'),
        (GUILD_MASTER, 'Гилдмастер'),
        (QUEST_GIVER, 'Квестгивер'),
        (BLACKSMITH, 'Кузнец'),
        (TANNER, 'Кожевник'),
        (POTIONS_MASTER, 'Зельевар'),
        (SPELL_MASTER, 'Мастер заклинаний'),
    ]

    category_name = models.CharField(max_length=2, choices=CATEGORY_CHOICE)


class Post(models.Model):
    post_header = models.TextField()
    post_text = models.TextField()
    post_user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.OneToOneField(Category, on_delete=models.CASCADE)


class Response(models.Model):
    response_text = models.TextField()
    response_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    response_post = models.ForeignKey(Post, on_delete=models.CASCADE)
