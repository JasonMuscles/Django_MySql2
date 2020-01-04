from django.shortcuts import render, redirect  # 重定向函数
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    """显示图书信息"""
    # 1.查询出所有图书的信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    """新增一个图书"""
    # 1.创建BookInfo对象
    b = BookInfo()
    b.book_title = '流星蝴蝶剑'
    b.book_publish_data = date(1990, 1, 1)
    # 2.保存到数据库
    b.save()
    # 3.返回应答，让浏览器在访问/index页面（这个过程叫做重定向）
    # return HttpResponseRedirect('/index')  # 比较复杂的写法
    return redirect('/index')  # 简写的重定向方式


def delete(request, bid):
    """添加删除点击的图书功能"""
    # 1.通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2.删除
    book.delete()
    # 3.重定向（/index）
    # return HttpResponseRedirect('/index')  # 比较复杂的写法
    return redirect('/index')  # 简写的重定向方式
