from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    book_title = models.CharField(max_length=20)
    # 出版日期
    book_publish_data = models.DateField()
    # 阅读量
    book_read = models.IntegerField(default=0)
    # 评论量
    book_comment = models.IntegerField(default=0)
    # 删除标记
    is_Delete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄人物类"""
    # 英雄名字
    hero_name = models.CharField(max_length=20)
    # 性别
    hero_gender = models.BooleanField(default=False)
    # 备注
    hero_comment = models.CharField(max_length=200)
    # 关系属性
    hero_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)  # hero_book = models.ForeignKey(‘BookInfo’)
    # 删除标记
    is_Delete = models.BooleanField(default=False)
