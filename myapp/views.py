from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth

from io import StringIO

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import requests
import pandas as p
from datetime import date, timedelta


# Create your views here.
def get_exchange_data():
    """
    ratesapi,io üzerinden 1 haftalık Dolar/TL
    verilerini çekmek amacıyla kullanılacak olan fonksiyon.
    """
    # 1 haftalık dolar/TL verileri bu listede tutulacak
    data_list = []

    # kur verileri çekilecek olan tarihler hesaplanıyor
    # son bir hafta içerisindeki tarihler alınacak
    today = date.today()
    days = []
    days.extend(range(0, 7))
    days = sorted(days, reverse=True)

    date_list = [str(today - timedelta(days=i)) for i in days]

    # parameters to be sent to the API
    parameters = {
        "symbols": ["TRY"],
        "base": "USD"
    }

    for d in date_list:
        # api endpoint
        # url = "https://api.ratesapi.io/api/2020-09-02?symbols=USD,TRY"
        url = "https://api.ratesapi.io/api"

        # url adresinin sonuna tarih bilgisi ekleniyor
        url = url + "/" + d

        # sending get request and saving the response as response object
        my_request = requests.get(url=url, params=parameters)

        # data json nesnesi olarak çıkarılıyor
        data = my_request.json()

        # tarih ve kur oranı çifti
        pair = (data["date"], data["rates"]["TRY"])

        data_list.append(pair)

    data_list = tuple(zip(*data_list))

    # alınan veriler pandas data frame yapısına dönüştürülüyor
    df = p.DataFrame(data_list)
    df = df.transpose()

    # 1 haftalık kur verileri pandas data_frame'i şeklinde return ediliyor.
    return df


def return_plot_image():
    """
    1 haftalık Dolar/TL grafiği grafiğe dönüştürülerek SVG formatında
    döndürülüyor.
    """
    df = get_exchange_data()  # kur verileri alınıyor
    numpy_array = df.to_numpy()  #pandas data frame, numpy array'e dönüştürülüyor

    # Dolar/TL verilerinden grafik oluşturuluyor
    # grafiğin x ve y ekseni için veriler okunuyor
    x = numpy_array[:, 0]
    y = numpy_array[:, 1]

    fig = plt.figure()
    plt.plot(x, y)

    plt.xlabel("Tarih", fontsize=14)
    plt.ylabel("Kur", fontsize=14)
    plt.title("Dolar/TL", fontsize=14)

    # plot grafiği svg formatına dönüştürülüyor
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    plt.close("all")  # close all plots
    return data


def custom_login(request):
    """
    Kullanıcının oturum açmasını düzenleyen fonksiyon.
    """
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                messages.info(request, "geçersiz bilgi girişi.")
                return redirect("login")
        else:
            return render(request, 'login.html')


@login_required(login_url='login')
def homePageView2(request):
    """
    Oturum açtıktan sonra görüntülenecek olan ana sayfanın görüntülenmesi için hazırlanan
    fonksiyon.
    """
    user_pk = request.user.pk

    if request.method == "GET":
        context = {"user_pk": user_pk, "graph": return_plot_image()}
        return render(request, "home.html", context=context)


def registerPage(request):
    """
    Sistemde yeni kullanıcı kaydı oluşturmak için
    oluşturulan fonksiyon.
    """
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():  # girilen bilgiler istenen şartları sağlıyorsa
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, 'Account was created for ' + user)
                return redirect("login")
            else:
                print("form is not valid")
        context = {"form": form}
        return render(request, "signup.html", context=context)


@login_required(login_url='login')
def updateUserView(request, pk):
    """
    Kullanıcı bilgilerini güncelleme işlemlerinden sorumlu fonksiyon
    """
    user = User.objects.get(id=pk)
    form = UpdateUserForm(instance=user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'update.html', context)


def logoutUserView(request):
    """
    Kullanıcının Oturumu bu fonksiyon aracılığı ile kapatılıyor.
    """
    logout(request)
    return redirect("login")
