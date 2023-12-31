jeslyn-theodora-tugas<br>
# current_items (W6)
<p><b>Jelaskan perbedaan antara <i>asynchronous programming</i> dengan <i>synchronous programming</i>.</b><br>
 <i>Asynchronous programming</i> adalah programming dimana suatu program tidak harus menunggu satu proses selesai untuk memulai proses lain. Sebaliknya, di <i>synchronous programming</i> ada suatu urutan yang harus diikuti dimana proses baru tidak bisa dimulai sebelum proses sebelumnya selesai. Dengan kata lain, asynchronous menggunakan multithreading, sedangkan synchronous menggunakan singlethreading. Ini membuat asynchronous memiliki throughput yang lebih tinggi karena lebih banyak dari satu proses dapat berjalan dalam waktu yang sama. Dalam konteks web programming, <i>synchronous programming</i> memerlukan halaman di refresh untuk menunjukkan perubahan, sedangkan <i>asynchronous programming</i> hanya sebagian/beberapa elemen.</p>
<p><b>Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma <i>event-driven programming</i>. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.</b><br>
Paradigma <i>event-driven programming</i> adalah paradigma dimana jalannya program dependen terhadap event seperti mengklik mouse. Ini berarti bahwa program merespon kepada kelakuan user dan menunggu untuk input. Dalam tugas ini, tabel (atau di tugas saya, accordian) akan refresh saat user mengisi form AJAX.</p>
<p><b>Jelaskan penerapan <i>asynchronous programming</i> pada AJAX.</b><br>
AJAX jenis asynchronous (Asynchronuos AJAX) membuat page tidak usah refresh untuk setiap kali menjalankan proses. Setelah terjadi suatu event yang mentrigger handler,  Javascript akan membuat XMLHttpRequest (XHR) dan object XHR akan mengirim request HTML, yang nanti akan diproses oleh server dan dikembalikan ke browser. Response yang didapat dari server diproses dengan Javascript dan proses dieksekusi tanpa memerlukan refresh/load ulang halaman.</p>
<p><b>Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.</b><br>
Fetch API menggunakan <i>Promises</i> yang hanya akan reject dalam kondisi masalah network atau ada hal yang mencegah request itu selesai. Fetch API lebih baru dibandingkan jQuery, dan memiliki syntax yang lebih readable dibandingkan jQuery. Selain itu, jQuery juga memerlukan adanya file javascript jQuery yang dapat mengambil tempat, dimana Fetch API tidak mengambil tempat yang sebanding. Secara umum, Fetch API lebih modern, lebih mudah dibaca, dan memiliki performance yang lebih baik. </p>
<p><b>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</b><br>
1. AJAX GET<br>
Pada berkas main.html, bagian script dipindahkan kebawah dan ditambahkan fungsi getItems yang menggunakan get_item_json untuk mendapatkan data item yang sudah dibuat, fungsi addItem yang menggunakan add_item_ajax untuk menambahkan data item. Juga fungsi refreshItems yang digunakan untuk mengupdate list item tanpa refresh halaman dibuat dengan menghapus isi dari div yang sebelumnya ditaruh accordian, dan isi itu dipindahkan kedalam refreshItems.</p>
<p>2. AJAX POST<br>
Saya membuat fungsi get_item_ajax dan add_item_ajax untuk mengembalikan data dengan JSON dan menambahkan item dengan AJAX, dan menambahkan keduanya ke urls.py. Setelah itu, di main.html saya membuat suatu button yang memunculkan form untuk membuat item baru, dan juga refresh list item tanpa harus reload halaman.</p>
<p>3. Melakukan perintah <code>collectstatic</code>.<br>
Saya buka settings.py dan menambahkan <code>STATIC_ROOT = BASE_DIR/ 'static'</code>. Setelah itu, saya membuat folder static pada root direktori dan menjalankan <code>python manage.py collectstatic</code>.</p>

# current_items (W5)
<p><b>Jelaskan manfaat dari setiap <i>element selector</i> dan kapan waktu yang tepat untuk menggunakannya.</b><br>
 - Simple Selector merupakan selector yang memilih elemen berdasarkan tag, nama atau id. Ini berguna saat ada formatting yang ingin dilakukan hanya untuk elemen dengan salah satu dari tag/nama/id spesifik itu. Sebagai contoh, semua label dengan id="green" diberi warna hijau.<br>
 - Combinator Selector adalah selector yang memilih elemen berdasarkan hubungan diantaranya/relasinya, seperti elemen yang merupakan child dari elemen lain. Selector ini berguna untuk memilih elemen yang memiliki relasi yang sama, namun tidak memiliki tag/nama/id yang sama. Sebagai contoh, semua elemen yang muncul persis setelah elemen yang lain selallu berada pada align center.<br>
 - Pseudo-class Selectors adalah suatu selector yang memilih elemen berdasarkan special-state/kondisi suatu elemen, sebagai contoh lagi di klik/di hover. Ini berguna untuk elemen yang memiliki special-state yang sama, supaya kodingan tidak harus ditulis secara berulangan.<br>
 - Pseudo-element Selectors adalah suatu selector yang memilih bagian dari tertentu dari suatu elemen, sebagai contoh huruf pertama dari suatu teks. Ini berguna untuk formatting elemen yang besar, atau bagian spesifik dari suatu elemen.<br>
 - Attribute Selector adalah selector yang memilih elemen berdasarkan suatu atribut spesifik/value dari atribut. Ini berguna untuk memilih elemen yang memliki atribut/sifat yang spesifik.</p>

<p><b>Jelaskan HTML5 Tag yang kamu ketahui.</b><br>
  - &lt;a&gt;, untuk membuat hyperlink<br>
  - &lt;b&gt;, untuk membuat <b>bold</b> suatu teks<br>
  - &lt;body&gt;, define body dari suatu dokumen HTML<br>
  - &lt;br&gt;, untuk membuat line break<br>
  - &lt;button&gt;, membuat elemen button yang bisa dipencet<br>
  - &lt;code&gt;, teks yang didalam daerah ini merupakan code<br>
  - &lt;div&gt;, menspesifikasikan suatu bagian dari dokumen<br>
  - &lt;em&gt;, digunakan untuk memberi emphasis ke suatu teks (secara semantik). Biasanya terender sebagai italic.<br>
  - &lt;form&gt;, mendefinisikan suatu form HTML untuk mendapatkan input user<br>
  - &lt;h1&gt;, h1 sampai denga h6 mendefinisikan header HTML<br>
  - &lt;i&gt;, untuk membuat suatu teks <i>italic</i>. Berbeda dengan em secara semantik, dimana italic biasanya digunakan untuk style<br>
  - &lt;input&gt;, mendefinisikan pengontrol input<br>
  - &lt;label&gt;, membuat suatu label<br>
  - &lt;p&gt;, mendefinisikan suatu paragraf<br>
  - &lt;script&gt;, tempat memasukan code yang dijalankan<br>
  - &lt;style&gt;, untuk memasukan style (formatting/sifat) ke dalam suatu dokumen. Biasaya CSS<br>
  - &lt;table&gt;, mendefinisikan suatu tabel data<br>
  - &lt;td&gt;, mendefinisikan cell didalam tabel<br>
  - &lt;th&gt;, mendefinisikan cell header pada tabel<br>
  - &lt;tr&gt;, mendefinisikan baris cell dari suatu tabel<br>
  - &lt;title&gt; mendefinisikan judul dari suatu dokumen<br>
  - &lt;u&gt;, untuk <u>underline/menggaris bawah</u> suatu teks</p>
  
<p><b>Jelaskan perbedaan antara <i>margin</i> dan <i>padding.</i></b><br>
Margin merupakan daerah (space yang disisihkan) disekitar element, sedangkan padding merupakan daerah didalam elemen. Sebagai contoh, jika ada suatu button kotak yang didalamnya ada teks "TEXT", margin merupakan spasi diantara button dan elemen diluar button, sedangkan padding merupakan spasi diantara teks dan border button.</p>

<p><b>Jelaskan perbedaan antara <i>framework</i> CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?</b><br>
Bootstrap merupakan suatu UI kit yang datang dengan komponen secara langsung, sedangkan Tailwind hanya memberikan utility class dan widget. Karena sudah ada komponen yang <i>built-in</i>, cenderungan banyak website yang menggunakan Bootstrap terlihat generic. Secara umum, jika kita ingin memprioritaskan desain dan kustomisasi full dalam development website, sebaiknya menggunakan Tailwind. Jika kita lebih memprioritaskan suatu framework yang kurang <i>time-consuming</i> dan sudah mengcover banyak hal ang diperlukan dalam web design, sebaiknya menggunakan Bootstrap.</p>

# current_items (W4)
<p><b>Apa itu Django <code>UserCreationForm</code>, dan jelaskan apa kelebihan dan kekurangannya?</b><br>
Django <code>UserCreationForm</code> adalah suatu form yang digunakan untuk membuat user dalam suatu aplikasi. Formnya memiliki tiga field, yaitu username, password1, dan password2 (digunakan untuk konfirmasi password).<br>
- Kelebihan: Proses pembuatan user dipendekkan sehingga developer hanya harus membuat view untuk menampilkan form pembuatan user.<br>
- Kekurangan: Dari Django tidak langsung ada view yang menampilkan pembuatan user, jadi harus dibuat secara manual. Juga, tidak datang dengan email field, jadi jika ingin menambahkan functionality untuk verifikasi email, harus dilakukan sendiri. Secara umum, fitur lain harus ditambahkan secara manual.</p>

<p><b>Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?</b><br>
Secara singkat, autentikasi adalah proses yang verifikasi suatu user yang pastikan bahwa user yang sedang menggunakan aplikasi beneran merupakan user itu, sedangkan otorisasi merujuk pada apa yang user itu boleh lakukan. Keduanya penting karena keberadaan data yang tidak kita ingin diubah/dilihat oleh user. Otorisasi membuatnya supaya mereka tidak dapat mengakses data tersebut dan autentikasi membuatnya supaya seorang user tidak bisa <i>circumvent</i> otorisasi dengan mengubah diri menjadi user yang memiliki akses.</p>

<p><b>Apa itu <i>cookies</i> dalam konteks aplikasi web, dan bagaimana Django menggunakan <i>cookies</i> untuk mengelola data sesi pengguna?</b><br>
Cookies adalah file kecil yang didalamya berisi data yang digunakan untuk identifikasi suatu komputer. Suatu server/network membuat dan mengirim cookie, dan cookie disebut digunakan sebagai ID untuk komputer. Ini juga membuatnya supaya network dapat mengetahui user tanpa melakukan autorisasi secara berulang (selama ada cookie). Django menggunakan cookies untuk menyimpan suatu <i>value</i> dan menyimpan session ID (bukan ID untuk user) untuk waktu yang telah ditetapkan.</p>

<p><b>Apakah penggunaan <i>cookies</i> aman secara <i>default</i> dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</b><br>
Secara umum, cookies aman untuk digunakan secara pengembangan web, tapi semua hal ada risikonya. Untuk cookies, bisa terjadi suatu cookie tidak secure akibat dari masalah dari website, atau ada hacker yang menyelipkan software problematic yang terlihat sebagai cookie.</p>

<p><b>Jelaskan bagaimana cara kamu mengimplementasikan <i>checklist</i> di atas secara <i>step-by-step</i>.</b><br>
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.<br>
Saya mengimport Django UserCreationForm, redirect, messages, authenticate, login, dan logout ke views.py yang di subdirektori main, serta membuat fungsi register, login_user, dan logout_user. Setelah itu, saya membuat berkas register.html dan login.html di templates di main dan menambahkan path masing-masing fungsi ke ke urls.py.</p>

<p>2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.<br>
Menjalankan <code>python manage.py runserver</code> dan membuka http://localhost:8000/ melalui firefox (virtual environment sudah nyala dan command prompt sudah berada di direktori). Saat page login muncul, saya registrasi dan login dengan data yang telah diinput, serta mengisi form untuk membuat item. Ini diulang sekali lagi sehungga ada dua akun pengguna.</p>

<p>3. Menghubungkan model Item dengan User.<br>
Buka models.py, import User, dan menambahkan kode tersebut ke dalam model Item:
 
```
 user = models.ForeignKey(User, on_delete=models.CASCADE)
```
<br>Setelah itu, didalam views.py, fungsi insert_item diubah menjadi berikut:
```
form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))

 ...
```
</p>
<p>4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.<br>
Buka views.py dan mengimport datetime, lalu menambahkan request cookie datetime now untuk fungsi <code>login_user</code>. Dalam show_main ditambahkan objek last_login untuk mengakses cookie yang baru ditambahkan, dan di main.html disisipkan <code>{{ last_login }}</code> agar muncul di tampilan website. Untuk menampilkan username, di views.py, pada bagian context, bagian name diubah menjadi kode berikut:
 
```
'name': request.user.username,
```
</p>

# current_items (W3)
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
1. Mempersiapkan command prompt dengan ubah path direktori ke current_items dan aktifkan virtual environment dengan memasukkan command <code>env\Scripts\activate.bat</code>.<br>
2. Buke file <code>urls.py</code> yang berada di folder current_items dan path 'main/' pada urlpatterns diubah menjadi ''.<br>
3. Buat folder templates di direktori root dan didalamnya dibuat file <code>base.html</code> dengan isi kode berikut:<br>
 
```
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
```

4. Buka <code>settings.py</code> yang berada di subdirektori current_items dan tambahkan kode tersebut ke baris <code>TEMPLATES</code>:
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```
 
5. Ubah kode di berkas ```main.html``` yang berada di direktori main menjadi kode berikut:<br>
```
{% extends 'base.html' %}

{% block content %}
   <h1>Shopping List Page</h1>
    
   <h5>Name:</h5>
   <p>{{name}}</p>

   <h5>Class:</h5>
   <p>{{class}}</p>
{% endblock content %}
```
6. Buat berkas ```forms.py``` pada direktori main dengan isi kode berikut (ini untuk membuat struktur form):<br>
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "type"]
```

7. Tambahkan kode tersebut ke file ```views.py``` yang ada pada direktori main untuk import data yang diperlukan:<br>
```
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
```
8. Buat fungsi baru ```insert_item``` seperti berikut:<br>
```
def insert_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "insert_item.html", context)
```
9. Ubah fungsi ```show_main``` pada file yang sama menjadi:<br>
```
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Jeslyn Theodora', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'items': items
    }

    return render(request, "main.html", context)
```
10. Buka ```urls.py``` di direktori main dan import fungsi yang tadi dibuat:<br>
```from main.views import show_main, insert_item```
11. Tambahkan path berikut ke urlpatterns di file ```urls.py``` yang sama:<br>
```path('insert_item', insert_item, name='insert_item'),```
12. Buat berkas HTML baru ```insert_item.html``` pada subdirektori templates di main dengan kode berikut:<br>
```
{% extends 'base.html' %} 

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
```
13. Dalam ```main.html``` tambahkan kode berikut yang akan menampilkan data, serta redirect ke form yang menambahkan item:<br>
```
<table>
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
```
14. Pada ```views.py``` di direktori main ditambahkan fungsi tersebut:<br>
```
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
15. Ubah kode import dari main.views pada ```views.py``` menjadi:<br>
```
from main.views import show_main, insert_item, show_xml, show_json, show_xml_by_id, show_json_by_id
```
17. Tambahkan path url berikut ke urlpatterns:<br>
```
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
```
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
