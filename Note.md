# Django 练习

## Day1
1. manage.py 阅读
2. urlpatterns
   1. path(route, view, kwargs, name)
   2. include (route, namespace) 可以继续引用
3. venv
   1. 创建虚拟环境
   ```
    python -m venv venv
   ```
   2. 激活虚拟环境
   ```
   cd venv/Scripts
   activate
   ```
   3. 安装依赖
   ```
    pip install -r requirements.txt
    ```
   4. 导出依赖
   ```
    pip freeze > requirements.txt
    ```
## Day2
1. Django.db.models.Model: Each model have many variables calss. They all represent a column in the database.
   Field: Each field is represented by an instance of a Field class.
2. 激活模型：创建应用程序时，Django会自动生成一个apps.py文件，其中会有一个AppNameConfig的类，所有在INSTALLED_APPS中要写AppName.apps.AppNameConfig

3. 创建模型
   ```
   py manage.py makemigrations polls
   ```
   迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 它们其实也只是一些你磁盘上的文件。
   ```
   py manage.py sqlmigrate polls 0001
   ```
   再次运行 migrate 命令，在数据库里创建新定义的模型的数据表
   ```
   py manage.py migrate
   ```
4. 使用模型
   ```
   py manage.py shell
   ```
   进入简易的命令行

5. model类中 __str__ 方法：返回一个对象的描述信息，是一个字符串，用于在调试时使用，比如在后台管理中显示一个对象时，默认显示它的 __str__ 返回的字符串。
   