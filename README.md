# current_inventory
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

<p><b>BAGAN</b></p>
![image](https://github.com/jteo0/current_inventory/blob/main/bagan.png?raw=true)

<p><b>Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</b><br>
Virtual environment bekerja sebagai suatu lingkungan terisolasi untuk suatu proyek. Sebagai contoh, jika saya memiliki dua proyek berbeda yang menggunakan versi modul python yang berbeda, kedua proyek dapat memiliki virtual environmentnya sendiri supaya keduanya bisa dirun tanpa error. Juga, penginstallan/perubahan modul secara tanpa mengerti secara penuh tentang sistem komputer dapat menyebabkan masalah pada jalannya sistem. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment (virtual environment hanya lingkungan), tapi secara umum lebih baik tetap digunakan.</p>

<p><b>Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</b><br>
 - MVC: MVC atau Model-View-Controller adalah sebuah pola arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan Controller. Model merupakan bagian yang mengolah data dan mewakili struktur data, View merupakan bagian yang mengatur tampilan ke user, dan Controller merupakan jembatan diantara Model dan View (berisi perintah/command yang memproses data dan mengirimkannya ke halaman web).<br>
 - MVT: MVT atau Model-View-Template adalah pola arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan Template. Model dan View memiliki fungsi yang sama seperti Model dan View pada MCV. Template merupakan bagian yang menentukan tampilan layar user tergantung dengan apa yang telah ditulis di template (biasanya dalam bentuk html).<br>
 - MVVM: MVVM atau Model-View-ViewModel adalah pola struktur arsitektur aplikasi web yang membagikan pengembangan aplikasi menjadi tiga komponen, yaitu Model, View, dan ViewModel. Model dan View memiliki fungsi yang sama seperti pada MCV dan MVT. ViewModel adalah penghubung View dan Model yang mengimplementasi suatu <i>binder</i> yang mengimplementasi dan mengomunikasikan data yang relevan untuk view.</p>
