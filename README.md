Sabrina Aviana Dewi - 2206030520
Link Deploy: https://tokopbpsabrina.adaptable.app/

## Membuat Proyek Django
1. Membuat direktori baru dengan nama proyek toko_pbp
2. Membuat virtual environment di command prompt dengan menjalankan perintah:
    ```shell
    python -m venv env
    ```
3. Mengaktifkan virtual environment di Windows dengan perintah:
    ```shell
    env\Scripts\activate.bat
    ```
4. Membuat berkas requirements.txt di dalam direktori toko_pbp. Berkas berisi dependencies berikut:
    ```shell
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Memasang dependencies (untuk install Django) dengan perintah:
    ```shell
    pip install -r requirements.txt
    ```
6. Membuat proyek Django bernama toko_pbp dengan perintah:
    ```shell
    django-admin startproject toko_pbp .
    ```
7. Menambahkan '*' pada 'ALLOWED_HOST' di settings.py dalam direktori proyek toko_pbp
    ```shell
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```

## Membuat Aplikasi Main
1. Masih dalam virtual environment dan direktori 'toko_pbp', membuat aplikasi baru bernama 'main' dengan perintah:
    ```shell
    python manage.py startapp main
    ```
2. Mendaftarkan aplikasi main ke dalam proyek dengan menambahkan 'main' ke variabel INSTALLED_APPS:
    ```shell
    INSTALLED_APPS = [
    ...,
    'main',
    ...
    ]
    ```

## Membuat Model Aplikasi Main
1. Mengisi berkas models.py pada direktori aplikasi main dengan kode:
    ```shell
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        amount = models.IntegerField()
        description = models.TextField()
    ```
2. Mendaftarkan migrasi model
    ```shell
    python manage.py makemigrations
    ```
3. Melakukan migrasi model
    ```shell
    python manage.py migrate
    ```

## Membuat Fungsi views.py untuk Dikembalikan ke Template HTML
1. Membuat direktori templates di dalam direktori aplikasi main
2. Membuat berkas main.html di dalam direktori templates dengan isi:
    ```shell
    <h1>Toko PBP</h1>

    <h5>App Name: </h5>
    <p>{{ app name }}</p>
    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ```
3. Mengisi views.py pada direktori aplikasi main dengan:
    ```shell
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app name': 'main',
            'name': 'Sabrina Aviana Dewi',
            'class': 'PBP C'
        }

        return render(request, "main.html", context)
    ```

## Routing urls.py Aplikasi Main
Membuat berkas urls.py di dalam direktori main dengan kode berikut:
```shell
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

## Routing URL Proyek untuk Menjalankan Main
Mengisi urls.py di direktori proyek toko_pbp dengan kode berikut:
```shell
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
## Melakukan Deployment ke Adaptable
1. Menambahkan berkas .gitignore pada direktori toko_pbp (bukan direktori proyek) dengan kode berikut:
    ```shell
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak 

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod] 
    *$py.class 

    # Distribution / packaging 
    .Python build/ 
    develop-eggs/ 
    dist/ 
    downloads/ 
    eggs/ 
    .eggs/ 
    lib/ 
    lib64/ 
    parts/ 
    sdist/ 
    var/ 
    wheels/ 
    *.egg-info/ 
    .installed.cfg 
    *.egg 
    *.manifest 
    *.spec 

    # Installer logs 
    pip-log.txt 
    pip-delete-this-directory.txt 

    # Unit test / coverage reports 
    htmlcov/ 
    .tox/ 
    .coverage 
    .coverage.* 
    .cache 
    .pytest_cache/ 
    nosetests.xml 
    coverage.xml 
    *.cover 
    .hypothesis/ 

    # Jupyter Notebook 
    .ipynb_checkpoints 

    # pyenv 
    .python-version 

    # celery 
    celerybeat-schedule.* 

    # SageMath parsed files 
    *.sage.py 

    # Environments 
    .env 
    .venv 
    env/ 
    venv/ 
    ENV/ 
    env.bak/ 
    venv.bak/ 

    # mkdocs documentation 
    /site 

    # mypy 
    .mypy_cache/ 

    # Sublime Text
    *.tmlanguage.cache 
    *.tmPreferences.cache 
    *.stTheme.cache 
    *.sublime-workspace 
    *.sublime-project 

    # sftp configuration file 
    sftp-config.json 

    # Package control specific files Package 
    Control.last-run 
    Control.ca-list 
    Control.ca-bundle 
    Control.system-ca-bundle 
    GitHub.sublime-settings 

    # Visual Studio Code
    .vscode/* 
    !.vscode/settings.json 
    !.vscode/tasks.json 
    !.vscode/launch.json 
    !.vscode/extensions.json 
    .history
    ```
2. Membuat repositori Github bernama toko_pbp dengan visibilitas public
3. Inisiasi direktori lokal toko_pbp sebagai repositori Git dengan menjalankan perintah berikut di command prompt (masih di dalam environment dan direktori toko_pbp):
    ```shell
    git init
    git remote add origin https://github.com/pershyfon/toko_pbp.git
    git commit -m "membuat proyek baru"
    git push -u origin master
    ```
4. 


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya