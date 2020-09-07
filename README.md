# Önyüz Projesi

### Kullanılan Kütüphaneler

- Django Web Framework

- matplotlib

- requests

- pandas

- numpy

- django-sass-processor

## Uygulama İçeriği

### Başlangıç Sayfası:
- Uygulamanın ana sayfasına ulaşım Django backend servisi kontrolündedir.
- Uygulamadaki Login ve Register formları arkadaki backend servis kontrolündedir.
- Login olduktan sonra anasayfa görüntülenmektedir.

### Ana Sayfa:
- İçerik Panelinde ratesapi.io adresinden alınan 1 haftalık USD/TRY döviz kuru grafiği yer almaktadır.
- Uygulama döviz kuru servisine doğrudan bağlantı kurmaktadır.
- Başlık bölümünde sol tarafta bir logo, sağ tarafta kullanıcı adı, profil bilgilerini düzenlemek için ve oturumu kapatmak için butonlar bulunmaktadır.

### Profil Sayfası:
Profil sayfası seçildiğinde; 
- Kullacıcı adı,
- Ad,
- Soyad,
- Email adresi

bilgileri güncellenebilmektedir.

## Zorlanılan Noktalar:
Django web framework üzerinde daha önce authentication işlemlerinin nasıl yapıldığının bilinmemesi sebebiyle; 
- oturum açma, login, logout, şifre güncelleme gibi işlemlerin gerçekleştirilmesi fazlaca zaman almıştır.
- Ana sayfada olması istenen sol navigasyon menüsü gibi özellikler daha sonra projeye dahil edilecektir.

## Uygulamanın Kurulması

- Uygulama Jetbrain Pycharm IDE üzerinde geliştirlimiştir. Projenin kurulumu için Jetbrains'in aşağıdaki sitesindeki kurulum adımları izlenmiştir:
[Create and Run your first Django project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-django-project.html)

### Django projesinin setup kısmı tamamandıktan sonra kullanılan kütüphaneler terminal üzerinden aşağıdaki komutlarla yüklenmiştir:

- requests
```shell
$ pip install requests
```
- matplotlib
```shell
$ pip install matplotlib
```
- pandas
```shell
$ pip install pandas
```
- django-sass-processor  
```shell
$ pip install libsass django-compressor django-sass-processor
```
- numpy
```shell
$ pip install numpy
```

### kodları projeye aktardıktan sonra, komut satırından aşağıdaki komutlar sırasıyla çalıştırılarak proje localhost üzerinde test edilebilir:
```shell
$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver
```
