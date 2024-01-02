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
