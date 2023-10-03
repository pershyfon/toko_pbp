Sabrina Aviana Dewi - 2206030520

# PBP Tugas 5
## Manfaat Element Selector dan Waktu Penggunaan yang Tepat
Element selector digunakan supaya kita dapat melakukan kustomisasi seragam untuk setiap elemen dengan nama elemen tertentu, misal font atau warna latar belakang. Element selector juga dapat meningkatkan keterbacaan kode dan keefisiensian waktu ketika mengatur tampilan. Gaya yang telah diatur akan dapat diterapkan pada elemen-elemen dengan nama elemen yang sama. Element selector digunakan ketika ingin mengubah tampilan umum atau standar dari suatu elemen yang tidak memerlukan class atau ID spesifik.

## HTML5 Tag
```shell
<!DOCTYPE>: menunjukkan tipe dokumen seperti <!DOCTYPE html>
<a>: anchor adalah teks penanda awalan dan akhiran sebuah hypertext link
<button>: penanda button
<header>, <body>, <p> <footer>, : penanda header, body,paragraph, dan footer dari dokumen
<title>: penanda judul
<div>: penanda sebuah section
<h1> - <h6>: penanda header1 - header6 yang berupa ukuran dan ketebalan font sebagai header
<img>: penanda gambar
<label>: penanda label
<nav>: penanda navigation bar
<table>: penanda tabel
<th>: penanda header tabel
<td>: penanda tabel cell
<tr>: penanda baris tabel
<ul>: penanda unordered list
<li>: penanda item list
```

## Perbedaan Margin dan 
Margin | Padding
--- | ---
Jarak sekitar elemen dari sisi luar atau dengan elemen lain di sekitarnya | Jarak sekitar elemen dari sisi dalam atau dengan konten di dalamnya
Tidak memiliki latar belakang atau warna sendiri dan merupakan area transparan yang memisahkan elemen dari elemen-elemen lainnya | Memiliki latar belakang dan warna yang sama dengan elemen itu sendiri
Misalnya, menambahkan jarak antara dua elemen HTML, bisa dengan mengatur margin salah satu elemen atau keduanya | Misalnya, untuk membuat teks dalam elemen HTML terlihat lebih lega dari tepi elemen


## Perbedaan Framework CSS Tailwind dan Bootstrap
Tailwind | Bootstrap
--- | ---
Pendekatan "utility-first", di mana kita membangun antarmuka dengan menggabungkan class utilitas yang lebih kecil | Pendekatan "component-driven", di mana set class CSS dan komponen telah dirancang sebelumnya dengan tampilan yang cukup terstruktur dan konsisten
Kustomisasi tidak terbatas | Kustomisasi terbatas
File lebih ringan | File lebih berat karena menyediakan banyak fitur dan komponen siap pakai
Tidak menyertakan JavaScript sehingga perlu menulis JavaScript tambahan atau menggunakan framwork terpisah | Menyertaka JavaScript untu beberapa fitur sepertu modals, dropdowns, dan tab

### Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Bootstrap cocok untuk proyek dengan tenggat waktu yang ketat dan komponen pra-dibangun yang banyak. Bootstrap cocok untuk proyek dengan desain tradisional yang membutuhkan kerangka kerja yang stabil dan mudah digunakan. Dokumentasi Bootstrap yang kuat akan mempermudah mendapatkan sumber daya.

Tailwind memberi lebih banyak kendali dan fleksibilitas dalam desain sehingga cocok untuk proyek yang tampilan dan gayanya ingin diubah sesuai keinginan dengan mendefinisikan kelas CSS sendiri. Tailwind juga lebih baik digunakan ketika proyek membutuhkan kode CSS yang lebih ringan.

## Langkah Implementasi Checklist
1. Menambahkan style pada create_item.html, login.html, main.html, dan register.html direktori main.
2. Inventori di main.html ditampilkan menggunakan card
    ```shell
    <div class="product">
        {% for item in items %}
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{item.name}}</h5>
                    <p class="card-text">{{item.description}}</p>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item flex-v">Amount: {{item.amount}}
                        <div>
                            <a href="{% url 'main:add' item.id %}">
                                <button class="secondary-button">
                                    Add
                                </button>
                            </a>
                            <a href="{% url 'main:remove' item.id %}">
                                <button class="secondary-button">
                                    Remove
                                </button>
                            </a>
                        </div>
                    </li>
                    <li class="list-group-item">Price: {{item.price}}</li>
                </ul>
                <div class="card-body">
                    <a href="{% url 'main:delete' item.id %}">
                        <button class="primary-button">Delete</button>
                    </a>
                </div>
            </div>
        {% endfor %}
    </div>
    ```
3. Mengerjakan bonus dengan menambahkan kode berikut di style main.html
    ```shell
    .card:last-child, .card:last-child .flex-v {
        background: #1569C7;
    }
    ```

Referensi:
https://codepolitan.com/blog/perbedaan-bootstrap-dan-tailwind
https://getbootstrap.com/docs/4.0/components/card/

# PBP Tugas 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah sistem otentikasi bawaan Django yang mengirim permintaan POST untuk membuat pengguna baru. is_superuser dan is_staff disetel False, namun is_active disetel True. Untuk menggunakan UserCreationForm, kita perlu mengimpornya dari Django.contrib.auth.forms. 

Kekurangan Django UserCreationForm: 
1. Bidangnya terbatas, yakni hanya ada nama pengguna, kata sandi, dan konfirmasi kata sandi.
2. Tidak ada fitur lain, seperti profil pengguna atau validasi yang lebih kompleks.
3. Tampilannya sederhana.

Kelebihan Django UserCreationForm:
1. Mudah & praktis untuk digunakan.
2. Sudah memvalidasi kata sandi dan memeriksa apakah nama pengguna sudah ada sebelumnya.
3. Terintegrasi dengan model User Django sehingga data yang dimasukkan ke formulir akan langsung disimpan ke penyimpanan data pengguna di basis data
4. Mendukung kustomisasi sesuai kebutuhan untuk melengkapi kekurangan-kekurangan di atas

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi: Verifikasi bahwa pengguna adalah benar-benar siapa yang mereka klaim
Otorisasi: Pengaturan izin untuk pengguna, apa saja yang dapat dilakukan oleh pengguna terautentikasi
Keduanya penting untuk menjaga keamanan data pengguna dan menghindari penyalahgunaan atau akses tidak sah ke fitur/bagian tertentu. Pengaturan izin selain berfungsi untuk keamanan dan privasi, juga untuk meningkatkan pengalaman pengguna untuk hanya dapat mengakses bagian yang relevan dengan kebutuhan mereka.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah informasi berisi identifikasi dan rekam jejak pengguna yang sedang mengakses aplikasi web sebagai cara melakukan holding state. Holding state adalah proses memberi tahu siapa yang mengakses web tanpa terus-terusan login pada aplikasi web yang sama. Cookies memiliki tanggal kedaluwarsa dan akan terhapus otomatis jika sudah kedaluwarsa. Yang disimpan di cookies hanyalah session ID, yaitu suatu token (barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu..

Django menggunakan cookies untuk mengelola data sesi pengguna dengan menggunakan modul django.contrib.sessions.middleware.SessionMiddleware. Pada sesi pertama, Django membuat string acak unik sepanjang 32 karakter yang disebut kunci sesi dan mengaitkannya dengan data sesi. Data sesi ini dikirim dari server ke browser klien untuk disimpan sebagai cookies. Setiap pengguna melakukan permintaan, browser akan mengirimkan cookies bersama permintaan ke server Django. Kemudian akan kunci sesi digunakan untuk mengambil data sesi pengguna yang sesuai dari penyimpanan sesi (default-nya menggunakan basis data).

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Umumnya cookies tidak berbahaya dalam pengembangan web. Dalam kondisi normal, cookies tidak bisa men-transfer malware atau virus. Kecil kemungkinan untuk data hilang melalui cookies. Cookies dari suatu web juga tidak bisa dialihkan ke web lain. Namun, tetap harus hati-hati untuk tidak memberikan cookies ke sembarang web. Jangan lupa untuk hapus cookies secara berkala atau ketika mengakses lewat komputer publik. Penting juga untuk memastikan bahwa data dienkripsi dengan baik sebelum disimpan dalam cookies. Atur atribut HTTPOnly, secure flag, domain, path, session, dan perlindungan CSRF jika diperlukan.


## Langkah Implementasi Checklist
### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
1. Membuat fungsi register menggunakan UserCreationForm, login_user yang menge-set cookie, dan logout_user yang menghapus cookie di views.py aplikasi main
2. Membuat template register.html dan login.html untuk tampilan halaman register dan halaman login
3. Membuat pathnya di urls.py aplikasi main
4. Mengimport login_required di views.py dan menambahkan login_required sebelum fungsi-fungsi seperti ini:
    ```shell
    @login_required(login_url='/login')
    ```

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Register, login, dan add item 3x untuk setiap akun

### Menghubungkan model Item dengan User
1. Mengimport Django User di models.py aplikasi main dan menambahkan atribut user seperti ini:
    ```shell
    ...
    from django.contrib.auth.models import User

    class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
    ```
2. Menghubungkan item yang baru dibuat dengan user dengan menambahkan kode berikut di if form.is_valid() di fungsi create_item views.py aplikasi main:
    ```shell
    ...
    product.user = request.user
    ...
    ```

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
1. Mengubah context fungsi show_main pada views.py aplikasi main menjadi seperti ini untuk mendapatkan username dan last login:
    ```shell
    ...
    context = {
        'app_name': 'main',
        'username': request.user.username,
        'class': 'PBP C',
        'items': items,
        'item_terakhir': item_terakhir,
        'last_login': request.COOKIES.get('last_login'),
    }
    ...
    ```
2. Menambahkan kode berikut di main.html untuk menampilkan last login:
    ```shell
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```

### Implementasi bonus
1. Membuat fungsi add_amount, remove_amount, dan delete_item di views.py aplikasi main
2. Menambahkan path ke fungsi-fungsi tersebut di urls.py aplikasi main
3. Membuat button yang akan memanggil fungsi-fungsi tersebut jika dipencet di main.html

### Melakukan add, commit, push ke GitHub
Memperbarui repositori Github dengan menjalankan kode berikut di command prompt (virtual environment aktif dan di direktori toko_pbp):
    ```shell
    git add .
    git commit -m "tugas 4 selesai"
    git push -u origin master
    ```

referensi:
https://www.javatpoint.com/django-usercreationform
https://stackoverflow.com/questions/37544543/what-is-the-difference-between-authorization-and-authentication-in-django

# PBP Tugas 3
## Apa perbedaan antara form POST dan form GET dalam Django?
POST | GET
--- | ---
Mengirim data ke server untuk diproses | Mengambil atau mengembalikan data dari server tanpa memproses/mengubah status
Mengirimkan data langsung ke action untuk ditampung tanpa menampilkan data pada URL | Menampilkan data pada URL kemudian ditampung oleh action
Menggunakan variabel $_POST untuk menampung data | Menggunakan variabel $_GET untuk menampung data
Pengambilan variabel dengan request.POST.get | Pengambilan variabel dengan request.GET.get
Data tidak terbatas | Data tidak boleh lebih dari 2407 karakter
Lebih aman | Kurang aman
Input data menggunakan form | Input data melalui link
Untuk data penting seperti password | Untuk data tidak penting
Tidak dapat disimpan dalam cache | Dapat disimpan dalam cache browser
URL tidak bisa di-bookmark atau dibagikan | URL bisa di-bookmark atau dibagikan

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML | JSON | HTML
--- | --- | ---
Digunakan untuk menyimpan, mendefinisikan, mengatur, dan mentransfer data | Digunakan untuk transfer data | Digunakan untuk menampilkan susunan depan laman
Tidak mendukung tipe data array | Mendukung tipe data array | Mendukung tipe data array sesuai framework yang digunakan
Menggunakan tag pembuka dan penutup | Lebih sederhana karena tidak menggunakan tag | Menggunakan tag pembuka dan penutup
Struktur pohon | Struktur pasangan kunci-nilai | Struktur pohon
Syntax bertele-tele, menggunakan tag, dan susah dibaca | Syntax sederhana, padat, dan mudah dibaca | Syntax terdapat banyak tag
Memerlukan pengurai XML | Bisa diurai dengan fungsi JavaScript standar | Bisa diurai dengan berbagai bahasa pemrograman menggunakan library & framework yang tersedia
Ada comments | Tidak ada comments | Ada comments
Mendukung lebih banyak jenis encoding | Hanya mendukung encoding UTF-8 | Mendukung banyak jenis encoding

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Karena lebih ringan, sederhana, mudah ditulis, mudah dibaca, dan mudah diuji, baik oleh manusia maupun komputer. JSON didukung oleh hampir semua bahasa pemrograman, seperti JavaScript, Python, Java, PHP, dll. Setiap bahasa pemrograman tersebut menyediakan pustaka bawaan atau pihak ketiga untuk mengurai (deserialize) dan menghasilkan (serialize) data JSON dengan mudah.

JSON mendukung tipe data array sehingga transfer data dapat dilakukan secara terstruktur dan teratur, yang mana sangat penting dalam pengembangan aplikasi web modern yang kompleks. JSON juga memungkinkan pembaruan data secara parsial, yaitu pengembang dapat mengirimkan hanya sebagian data yang berubah

## Screenshot Postman
![view html](https://images2.imgbox.com/2c/05/RTQBMeWZ_o.png)
![view xml](https://images2.imgbox.com/de/bc/y01Sm6uK_o.png)
![view json](https://images2.imgbox.com/a9/6f/lBgQNLlC_o.png)
![view xml by id](https://images2.imgbox.com/98/40/4qFfgsNL_o.png)
![view json by id](https://images2.imgbox.com/ba/5d/XPNlnUMJ_o.png)

## Langkah Implementasi Checklist
### Membuat input form
Membuat berkas forms.py pada direktori main dengan isi:
```shell
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]
```
### Menambahkan 5 fungsi views untuk melihat objek
1. Mengubah fungsi show_main di views.py direktori main menjadi:
    ```shell
    def show_main(request):
        items = Item.objects.all()
        context = {
            'app_name': 'main',
            'name': 'Sabrina Aviana Dewi',
            'class': 'PBP C',
            'items': items
        }

        return render(request, "main.html", context)
    ```
2. Menambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py direktori main dengan:
    ```shell
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
### Membuat routing URL masing-masing views
1. Menambahkan import di urls.py direktori main
    ```shell
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
2. Menambahkan path di urlpatterns
    ```shell
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...
    ```
### Akses URL pada Postman
1. Masukkan satu-satu link berikut di GET, lalu send
http://localhost:8000
http://localhost:8000/xml/
http://localhost:8000/json/
http://localhost:8000/xml/1
http://localhost:8000/json/1

### Bonus fitur pesan
1. Menyimpan item yang ditambahkan ke variabel item_terakhir di views.py direktori main
    ```shell
    if items:
        item_terakhir = items.last()
    else:
        item_terakhir = None
    ```
2. Menambahkan item_terakhir ke context di fungsi show_main views.py direktori main
    ```
    ...
    'item_terakhir': item_terakhir,
    ...
    ```
3. Menambahkan kode berikut di atas tabel di main.html:
    ```shell
    {% if item_terakhir %}
    <h2>Kamu menyimpan {{ item_terakhir.amount }} {{ item_terakhir.name }} pada aplikasi ini</h2>
    {% endif %}
    ```

### Add, commit, push ke Github
Memperbarui repositori Github dengan menjalankan kode berikut di command prompt (virtual environment aktif dan di direktori toko_pbp):
    ```shell
    git add .
    git commit -m "tugas 3 selesai"
    git push -u origin master
    ```

referensi:
https://gist.github.com/rririanto/442f0590578ca3f8648aeba1e25f8762
https://www.dumetschool.com/blog/Perbedaan-Metode-POST-Dan-GET
https://aws.amazon.com/id/compare/the-difference-between-json-xml/



# PBP Tugas 2
Link Deploy: https://tokopbpsabrina.adaptable.app/main/
## Langkah Implementasi Checklist
### Membuat Proyek Django
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

### Inisiasi Repositori Github
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

### Membuat Aplikasi Main
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

### Membuat Model Aplikasi Main
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

### Membuat Fungsi views.py untuk Dikembalikan ke Template HTML
1. Membuat direktori templates di dalam direktori aplikasi main
2. Membuat berkas main.html di dalam direktori templates. main.html memuat hal-hal yang akan ditampilkan pada aplikasi
3. Mengisi views.py pada direktori aplikasi main dengan:
    ```shell
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name': 'main',
            'name': 'Sabrina Aviana Dewi',
            'class': 'PBP C',
            'item_name': 'Bubbly Eau de Toilette',
            'amount': '30',
            'price': '300000',
            'description': 'Experience the light, powdery, and clean scent of freshly laundered linens in a bottle.',
        }

        return render(request, "main.html", context)
    ```

### Routing urls.py Aplikasi Main
Membuat berkas urls.py di dalam direktori main dengan kode berikut:
```shell
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### Routing URL Proyek untuk Menjalankan Main
Mengisi urls.py di direktori proyek toko_pbp dengan kode berikut:
```shell
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
### Melakukan Deployment ke Adaptable
1. Memperbarui repositori Github dengan menjalankan kode berikut di command prompt (masih di virtual environment dan direktori toko_pbp):
    ```shell
    git add .
    git commit -m "membuat aplikasi main"
    git push -u origin master
    ```
2. Masuk ke adaptable.io dengan login menggunakan akun Github
3. Membuka app dashboard di https://adaptable.io/app/dashboard
4. Membuat aplikasi baru dengan menekan tombol + NEW APP
5. Pilih Connect an Existing Repository
6. Pilih repositori toko_pbp
7. Pilih branch master
8. Pilih Python App Template
9. Pilih PostgreSQL
10. Pilih versi Python 3.10 dan masukkan ke bagian Start Command perintah berikut:
    ```shell
    python manage.py migrate && gunicorn shopping_list.wsgi
    ```
11. Masukkan nama aplikasi yang akan menjadi domain situs web aplikasi, yaitu tokopbpsabrina
12. Centang HTTP Listener on PORT
13. Klik Deploy App

### Membuat README.md
1. Buat berkas README.md di direktori toko_pbp berisi permintaan soal
2. Memperbarui ke Github dengan menjalankan perintah:
    ```shell
    git add .
    git commit -m "menambahkan README.md"
    git push -u origin master
    ```
### Membuat Testing Django
Mengisi tests.py pada direktori main dengan:
```shell
from django.test import TestCase, Client

class MainTest(TestCase):
    # test URL
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code,200)

    # test views
    def test_main_using_item_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # test HTML
    def test_template_has_checklist(self):
        response = Client().get('/main/')
        self.assertContains(response, 'App Name: ', html=True)
        self.assertContains(response, 'Name: ', html=True)
        self.assertContains(response, 'Class: ', html=True)
```

## Bagan Request Client ke Web Aplikasi
Bagan:
![bagan](https://images2.imgbox.com/cb/7a/zoczTbst_o.png)

Kaitan antara urls.py, views.py, models.py, dan berkas html:
HTTP Request datang dari client dan akan dicocokkan dengan pola URL yang telah didefinisikan dalam urls.py. Kemudian urls.py mengarahkan permintaan ke views.py yang sesuai untuk menangani permintaan tersebut. View (views.py) mengambil alih permintaan dan dapat berinteraksi dengan mengambil data model.py untuk mengakses atau memanipulasi database. views.py merender berkas HTML (template) dengan menggunakan data yang telah diproses. Template HTML menghasilkan halaman web yang akan dikirimkan sebagai HTTP Response kepada client, yang akhirnya akan dilihat oleh pengguna pada halaman web.

## Kenapa menggunakan virtual environment? 
Virtual environment berguna untuk mengisolasi package serta dependensi dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lainnya. 

Dengan virtual environment, maka proyek dapat berjalan sesuai dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan dan hanya perlu menggunakan requirements.txt  sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam virtual environment tertentu agar mesin host (seperti Adaptable) dapat mengetahui apa saja dependensinya.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun dianjurkan menggunakan environment agar versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. 

Ketika dijalankan di online hoster tanpa virtual environment juga cukup susah karena server host akan mencari daftar dependensi yang ada di dalam "requirements.txt" untuk disesuaikan dengan paket dependensi yang dimiliki mesin hosting.

## MVC, MVT, MVVM dan Perbedaan Ketiganya
### MVC (Model-View-Controller):
Model: Bertanggung jawab untuk mengatur data dan logika bisnis aplikasi
View: Menampilkan informasi kepada pengguna dan mengirim perubahan ke model
Controller: Menghubungkan model dan view, mengendalikan alur logika bisnis, dan menangani permintaan dari pengguna

### MVT (Model-View-Template, digunakan dalam Django):
Model: Bertanggung jawab untuk mengelola data aplikasi dan berinteraksi dengan database
View: Menangani permintaan dari klien, mengambil data dari model, dan merender template dengan menggunakan data ini. View berperan sebagai pengontrol logika bisnis (tidak memiliki controller terpisah
Template: Mengontrol tampilan dan struktur halaman web. Template adalah berkas HTML yang dapat diisi dengan data oleh view

### MVVM (Model-View-ViewModel):
Model: Bertanggung jawab untuk mengelola data dan logika bisnis
View: Menampilkan data kepada pengguna
ViewModel: Berfungsi sebagai perantara antara model dan view. Ini mengelola tampilan data dan berinteraksi dengan model
MVVM adalah pola desain yang umumnya digunakan dalam pengembangan aplikasi berbasis JavaScript dan umumnya tidak digunakan dalam kerangka kerja web Python seperti Django.

Jadi, perbedaan utama antara ketiganya adalah:

MVC memiliki komponen Controller terpisah yang mengendalikan logika bisnis dan alur aplikasi. Ini adalah pola desain yang lebih umum dalam pengembangan perangkat lunak umum.

MVT adalah pola desain khusus Django, di mana Controller digantikan oleh tampilan (view) yang mengintegrasikan logika bisnis dengan permintaan dan respons HTTP.

MVVM adalah pola desain yang sering digunakan dalam pengembangan antarmuka pengguna berbasis JavaScript, tetapi kurang umum dalam pengembangan web dengan Django. Ini menggabungkan Model, View, dan ViewModel untuk mengelola tampilan data.

MVC | MVT | MVVM
--- | --- | ---
Model, View, Controller | Model, View, Template | Model, View, ViewModel
UI tidak eksplisit | Respons berupa UI (template HTML) | Tidak ada UI