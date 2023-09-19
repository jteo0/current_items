# current_items
<p><b>Apa perbedaan antara form POST dan form GET dalam Django?</b><br>
Form POST berfungsi untuk mendapatkan input dari form, mengencode datanya, dan menyerahkannya ke server. Form GET berfungsi untuk mengubah data tersebut menjadi string dan string tersebut dipakai untuk membuat URL dimana data harus diserahkan. Secara dasar, POST digunakan untuk <i>send</i> data, sedangkan GET digunakan untuk mengambil. Beberapa perbedaan lain adalah:</br>
 - GET bersifat idempotent (setiap request yang identik pasti akan mengeluarkan hasil yang sama). POST tidak bersifat idempotent.<br>
 - GET dapat di cache dan dapat disimpan di history browser, sedangkan POST tidak.<br>
 - GET tidak dapat memodifikasi data, sedangkan POST bisa.</p>
<p><b>Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?</b><br>
 - <b>HTML:</b> HTML digunakan untuk menampilkan data.<br>
 - <b>XML (Extensible Markup Language):</b> XML digunakan untuk pengiriman dan penyimpanan data dengan menggunakan tag. Juga, XML adalah suatu <i>Markup Language</i>, yakni suatu sistem yang digunakan untuk mengubah struktur dan formatting suatu teks.<br>
 - <b>JSON (Javascript Object Notation):</b> JSON digunakan untuk pengiriman dan penyimpanan data. JSON merupakan suatu format untuk representasi obyek. Juga, JSON mensupport struktur array.<br>
  - Perbedaan utama dari JSON dan XML adalah XML merupakan suatu Markup Language (berorientasi teks/dokumen), sedangkan JSON adalah notasi obyek (berorientasi obyek/data).</p>
<p><b>Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?</b><br>
JSON sering digunakan karena lebih efisien daripada XML.
 - JSON bersifat human readable dan machine readable. Walaupun sistem lain juga memiliki sifat yang sama, JSON secara umum dianggap salah satu sistem yang lebih mudah lagi untuk dibaca.<br>
 - JSON dapat langsung diparse oleh suatu parser JSON, sedangkan untuk XML, suatu developer harus menulis kode tambahan agar dokumen XML bisa dimengerti (Parser XML hanya memisahkan markup dari data). Ini berarti bahwa JSON secara umum memiliki performance yang lebih baik.<br></p>
<p><b>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.</b><br>
1. Mempersiapkan command prompt dengan ubah path direktori ke current_items dan aktifkan virtual environment dengan memasukkan command<code>env\Scripts\activate.bat</code>.<br>
2. Buke file <code>urls.py</code> yang berada di folder current_items dan path 'main/' pada urlpatterns diubah menjadi ''.<br>
3. Buat folder templates di direktori root dan didalamnya dibuat file <code>base.html</code> dengan isi kode berikut:<br></p>
<code>
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
</code>
<p>4. Buka <code>settings.py</code> yang berada di subdirektori current_items dan tambahkan kode tersebut ke baris <code>TEMPLATES</code>:<br>
<code>...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
</code><br>
5. Ubah kode di berkas <code>main.html</code> yang berada di direktori main menjadi kode berikut:<br>
<code>{% extends 'base.html' %}

{% block content %}
    <h1>Shopping List Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
</code><br>
6. Buat berkas <code>forms.py</code> pada direktori main dengan isi kode berikut (ini untuk membuat struktur form):<br>
<code>from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "type"]
</code><br>
7. Tambahkan kode tersebut ke file <code>views.py</code> yang ada pada direktori main untuk import data yang diperlukan:<br>
<code>from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
</code><br>
8. Buat fungsi baru <code>insert_item</i> seperti berikut:<br>
<code>def insert_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "insert_item.html", context)
</code><br>
9. Ubah fungsi <code>show_main</code> pada file yang sama menjadi:<br>
<code>def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Jeslyn Theodora', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'items': items
    }

    return render(request, "main.html", context)
</code><br>
10. Buka <code>urls.py</code> di direktori main dan import fungsi yang tadi dibuat:<br>
<code>from main.views import show_main, insert_item</code><br>
11. Tambahkan path berikut ke urlpatterns di file <code>urls.py</code> yang sama:<br>
<code>path('insert_item', insert_item, name='insert_item'),</code><br>
12. Buat berkas HTML baru <code>insert_item.html</code> pada subdirektori templates di main dengan kode berikut:<br>
<code>{% extends 'base.html' %} 

{% block content %}
<h1>Insert an item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
</code><br>
13. Dalam <code>main.html</code> tambahkan kode berikut yang akan menampilkan data, serta redirect ke form yang menambahkan item:<br>
<code><table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Amount</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.type}}</td>
                <td>{{item.description}}</td>
                <td>{{item.amount}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:insert_item' %}">
        <button>
            Insert an item
        </button>
    </a>
</code><br>
14. Pada <code>views.py</code> di direktori main ditambahkan fungsi tersebut:<br>
<code>def show_xml(request):
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
</code><br>
15. Ubah kode import dari main.views pada <code>views.py</code> menjadi:<br>
<code>from main.views import show_main, insert_item, show_xml, show_json, show_xml_by_id, show_json_by_id</code><br>
16. Tambahkan path url berikut ke urlpatterns:<br>
<code>    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
</code><br>
17. Buka postman dan merequest dengan method GET link berikut satu per satu, dan screenshot semuanya (saya ubah [id] menjadi 1):<br>
 - http://localhost:8000/<br>
 - http://localhost:8000/xml<br>
 - http://localhost:8000/json<br>
 - http://localhost:8000/xml/[id]<br>
 - http://localhost:8000/json/[id] <br>
18. Cari tahu jawaban dari pertanyaan:<br>
 - Apa perbedaan antara form POST dan form GET dalam Django?<br>
 - Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br>
 - Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br>
19. Lakukan add-commit-push ke GitHub.</p>

<p><b>Screenshot Postman</b><br>
 - HTML<br>![HTML](https://github.com/jteo0/current_inventory/blob/main/tugas3_html.png?raw=true)<br>
 - XML<br>![XML](https://github.com/jteo0/current_inventory/blob/main/tugas3_xml.png?raw=true)<br>
 - JSON<br>![JSON](https://github.com/jteo0/current_inventory/blob/main/tugas3_json.png?raw=true)<br>
 - XML by ID<br>![XML by ID](https://github.com/jteo0/current_inventory/blob/main/tugas3_xml.png?raw=true)<br>
 - JSON by ID<br>![JSON by ID](https://github.com/jteo0/current_inventory/blob/main/tugas3_json.png?raw=true)<br></p>

# current_items (W2)
<p>https://jj-pocket-dimension.adaptable.app</p>
<b>Pengimplementasian Checklist:</b><br>
<p>1. Membuat sebuah proyek Django baru:<br>
Membuat direktori bernama current_inventory dan membuat repository dengan nama yang sama di Github. Di dalam direktori, saya membuat file 'requirement.txt' dan mengisinya dengan dependencies yang diperlukan.</p>
<p>2. Membuat aplikasi dengan nama main pada proyek:<br>
Buka command prompt di dalam direktori current_inventory dan mengaktifkan virtual environment. Setelah itu, saya jalankan perintah 'python manage.py startapp main' untuk membuat folder di dalam direktori yang berisi file yang diperlukan untuk aplikasi.</p>
<p>3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main:<br>
Di dalam direktori current_inventory (bukan utama), ada file bernama 'settings.py'. Pada filenya ada bagian INSTALLED APPS dimana ditambahkan "'main'," di dalam list agar main bisa dijalankan.</p>
<p>4. Membuat aplikasi 'main' dengan nama 'Item':<br>
Di dalam file 'models.py', saya membuat class Item dibawah import, memberikannya argumen 'models.Model', dan menambahkan 4 hal, yaitu name (CharField), amount (IntegerField), description (TextField), dan type (CharField).</p>
<p>5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:<br>
Pada file 'views.py' di dalam direktori main, definisikan fungsi 'show_main' yang berisi context dan akan render 'main.html'. Di dalam 'main.html' dibuat header sebagai judul aplikasi, 'Name:' dan 'Class:' sebagai sub header, dan tampilan nama dan kelas (semua dengan formatnya sendiri). Tampilan ditulis sebagai '{{ name }}' dan '{{ class }}'.</p>
<p>6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:<br>
Di bawah import, import lagi 'show_main' dari 'main.views'. Setelah itu, 'app_name' di set ke "'main'" dan buat list urlpatterns yang terhubung ke fungsi 'show_mains' yang berada di file 'views.py'.</p>
<p>7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat:<br>
Buka Adaptable.io, lalu memilih opsi 'create a new app'. Setelah itu, opsi 'connecting an existing repository' dipilih, dan repositori yang digunakan adalah current_inventory. Settingan berikutnya adalah:<br>
 - Deployment branch: main<br>
 - Template deployment: Python App Template<br>
 - Tipe basis data: PostgreSQL<br>
 - Versi python: 3.10<br>
 - Start Command: python manage.py migrate && gunicorn current_inventory.wsgi<br>
 - Nama Aplikasi: jj-pocket-dimension<br>
 - HTTP Listener on PORT: Centang<br>
Setelah itu, saya mendeploy aplikasi.</p>

<p><b>BAGAN</b><br>![image](https://github.com/jteo0/current_inventory/blob/main/bagan.png?raw=true)</p>

<p><b>Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</b><br>
Virtual environment bekerja sebagai suatu lingkungan terisolasi untuk suatu proyek. Sebagai contoh, jika saya memiliki dua proyek berbeda yang menggunakan versi modul python yang berbeda, kedua proyek dapat memiliki virtual environmentnya sendiri supaya keduanya bisa dirun tanpa error. Juga, penginstallan/perubahan modul secara tanpa mengerti secara penuh tentang sistem komputer dapat menyebabkan masalah pada jalannya sistem. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment (virtual environment hanya lingkungan), tapi secara umum lebih baik tetap digunakan.</p>

<p><b>Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</b><br>
 - MVC: MVC atau Model-View-Controller adalah sebuah pola arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan Controller. Model merupakan bagian yang mengolah data dan mewakili struktur data, View merupakan bagian yang mengatur tampilan ke user, dan Controller merupakan jembatan diantara Model dan View (berisi perintah/command yang memproses data dan mengirimkannya ke halaman web).<br>
 - MVT: MVT atau Model-View-Template adalah pola arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan Template. Model dan View memiliki fungsi yang sama seperti Model dan View pada MCV. Template merupakan bagian yang menentukan tampilan layar user tergantung dengan apa yang telah ditulis di template (biasanya dalam bentuk html).<br>
 - MVVM: MVVM atau Model-View-ViewModel adalah pola struktur arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan ViewModel. Model dan View memiliki fungsi yang sama seperti pada MCV dan MVT. ViewModel adalah penghubung View dan Model yang mengimplementasi suatu <i>binder</i> yang mengimplementasi dan mengomunikasikan data yang relevan untuk view.</p>
