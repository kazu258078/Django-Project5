from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('account.urls')),
]

# django-admin startproject config .
# 仮想環境を構築
# pipenv install
# 仮想環境を有効にする
# pipenv shell
# 最新のDjangoをinstallする 
# pipenv install django
# version指定も可
# pipenv install django=1.9
# python manage.py startapp blog

# setting.pyを編集

# models.pyを編集を作成後にmigrations
# python manage.py makemigrations
# python manage.py migrate

# adminのページを使うにはスパーユーザーという管理者の登録が必要
# python manage.py createsuperuser