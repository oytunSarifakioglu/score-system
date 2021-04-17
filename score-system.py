ogr_sayisi = int(input("Lütfen öğrenci sayısını giriniz: "))

ogr_sayac = basariliOgranciSayisi = basarisizOgrenciSayisi = OrtalamaOgrenciSayisi = ustunBasariliOgrenciSayisi = 0;
kadinToplamNot = erkekToplamNot = 0
kadinSayisi = erkekSayisi = 0
azDersAlanOgrenciSayisi = 0
basarıOranı75 = 0
yuksekBursMiktari = 0
enYuksekOrtalama = 0
enYuksekIsim = ""
enYuksekDersSayisi = 0
enYuksekToplamKredi = 0
enBasariliOgrBurs = 0

totalBursOdenek = 0

maxBurs = 0
maxBursİsim = ""
maxBursDersSayisi = 0
maxBursKredi = 0
maxBursOrtalama = 0

while ogr_sayac != ogr_sayisi:
    ogr_sayac += 1

    dersSayisi = toplamKredi = basariliDersSayisi = basariliKrediSayisi = agirlikliNot = bursMiktari = 0
    ogrenciNumarasi = int(input("Öğrenci Numarasını Giriniz:"))
    ogrenciName = input("Öğrenci adını giriniz:")
    gender = input("Cinsiyetini Giriniz:")

    while gender != "K" and gender != "k" and gender != "E" and gender != "e":
        gender = input("Cinsiyetini Giriniz:")

    ikametgah = input("İkamet Yerini Giriniz:\n(Ailesi ile Yaşıyorsa A/a\n"
                      "Yurtta Kalıyorsa Y/y\n"
                      "Evde Kalıyorsa E/e)")
    while (
            ikametgah != "E" and ikametgah != "e" and ikametgah != "A" and ikametgah != "a" and ikametgah != "Y" and ikametgah != "y"):
        ikametgah = input("İkamet Yerini Giriniz:\n(Ailesi ile Yaşıyorsa A/a\n"
                          "Yurtta Kalıyorsa Y/y\n"
                          "Evde Kalıyorsa E/e)")
    dersKredisi = int(input("Dersin Kredi Sayısını Giriniz:"))

    while dersKredisi > 0:
        toplamKredi += dersKredisi
        dersSayisi += 1;
        dersNotu = int(input("Ders ortalamasını giriniz:"))

        while dersNotu < 0 or dersNotu > 100:
            dersNotu = int(input("Ders ortalamasını giriniz:"))

        agirlikliNot += dersKredisi * dersNotu
        if dersNotu > 60:
            basariliDersSayisi += 1
            basariliKrediSayisi += dersKredisi
        dersKredisi = int(input("Dersin Kredi Sayısını Giriniz:"))

    if basariliKrediSayisi / toplamKredi * 100 >= 75 or basariliDersSayisi / dersSayisi * 100 > 75:
        basarıOranı75 += 1
    if dersSayisi < 3 or toplamKredi < 10:
        azDersAlanOgrenciSayisi += 1
    agirlikliNot = agirlikliNot / toplamKredi

    if enYuksekOrtalama < agirlikliNot:
        enYuksekOrtalama = agirlikliNot
        enBasariliOgrBurs = bursMiktari
        enYuksekDersSayisi = dersSayisi
        enYuksekIsim = ogrenciName
        enYuksekToplamKredi = toplamKredi

    basariDurumu = ""
    if gender == "E" or gender == "e":
        erkekSayisi += 1
        erkekToplamNot += agirlikliNot
    else:
        kadinSayisi += 1
        kadinToplamNot += agirlikliNot
    if agirlikliNot < 35:
        basariDurumu = "Başarısız"
        basarisizOgrenciSayisi += 1



    elif agirlikliNot < 60:
        basariDurumu = "Ortalama"
        OrtalamaOgrenciSayisi += 1
        if ikametgah == "Y" or ikametgah == "y":
            bursMiktari = 120
        elif ikametgah == "E" or ikametgah == "e":
            bursMiktari = 130
    elif agirlikliNot < 85:
        if agirlikliNot < 70:
            if ikametgah == "Y" or ikametgah == "y":
                bursMiktari = 140 * 1.2 * 120 / 100
            elif ikametgah == "E" or ikametgah == "e":
                bursMiktari = 140 * 1.2 * 130 / 100
        elif agirlikliNot < 80:
            if ikametgah == "Y" or ikametgah == "y":
                bursMiktari = 170 * 1.3 * 120 / 100
            elif ikametgah == "E" or ikametgah == "e":
                bursMiktari = 170 * 1.3 * 130 / 100
        else:
            if ikametgah == "Y" or ikametgah == "y":
                bursMiktari = 190 * 1.5 * 120 / 100
            elif ikametgah == "E" or ikametgah == "e":
                bursMiktari = 190 * 1.5 * 130 / 100
        basariDurumu = "Başarılı"
        basariliOgranciSayisi += 1
    else:
        if agirlikliNot < 90:
            if ikametgah == "Y" or ikametgah == "y":
                bursMiktari = 190 * 1.5 * 120 / 100
            elif ikametgah == "E" or ikametgah == "e":
                bursMiktari = 190 * 1.5 * 130 / 100
        else:
            if ikametgah == "Y" or ikametgah == "y":
                bursMiktari = 200 * 1.8 * 120 / 100
            elif ikametgah == "E" or ikametgah == "e":
                bursMiktari = 200 * 1.8 * 130 / 100
        basariDurumu = "Üstün Başarılı"
        ustunBasariliOgrenciSayisi += 1


    totalBursOdenek += bursMiktari

    if bursMiktari > maxBurs:
        maxBurs = bursMiktari
        maxBursİsim = ogrenciName
        maxBursDersSayisi = dersSayisi
        maxBursKredi = toplamKredi
        maxBursOrtalama = agirlikliNot
    if bursMiktari > 300:
        yuksekBursMiktari += 1

    print("Öğrenci numarası {} İsim {}\n".format(ogrenciNumarasi, ogrenciName))
    print("Aldığı ders Sayısı: {} , toplam kredi: {}\n".format(dersSayisi, toplamKredi))
    print("Başarılı Ders Sayısı: {} toplam kredisi: {} \n"
          "Sayı olarak % : {}  Kredi olarak % : {}\n".format(basariliDersSayisi, basariliKrediSayisi,
                                                           basariliDersSayisi / dersSayisi * 100,
                                                           basariliKrediSayisi / toplamKredi * 100))
    print("Ağırlıklı Not Ortalaması: {}\n".format(agirlikliNot))
    print("Başarı Durumu: {}\n".format(basariDurumu))
    print("Burs Miktarı: {}\n".format(bursMiktari))

print("Başarısız Ogrenci Sayısı  {}:    Yüzdesi:  {}\n"
      "Ortalama Öğrenci Sayısı {}:    Yüzdesi:  {}\n"
      "Başarılı Öğrenci Sayısı  {}:    Yüzdesi:  {}\n"
      "Üstün Başarılı Öğrenci Sayısı  {}:    Yüzdesi: {}\n".format(basarisizOgrenciSayisi,
                                                                 basarisizOgrenciSayisi / ogr_sayisi * 100,
                                                                 OrtalamaOgrenciSayisi,
                                                                 OrtalamaOgrenciSayisi / ogr_sayisi * 100,
                                                                 basariliOgranciSayisi,
                                                                 basariliOgranciSayisi / ogr_sayisi * 100,
                                                                 ustunBasariliOgrenciSayisi,
                                                                 ustunBasariliOgrenciSayisi / ogr_sayisi * 100))
print("Kadınlar için Ağırlıklı Not Ortalamasi:  {}\n"
      "Erkekler için Ağırlıklı Not Ortalaması:  {}\n"
      "Genel Ağırlıklı Not Ortalaması:  {}\n".format(kadinToplamNot / kadinSayisi, erkekToplamNot / erkekSayisi,
                                                   erkekToplamNot + kadinToplamNot / ogr_sayisi))

print("Aldığı Derslerin Kredileri Toplamı 10dan az \n"
      "Olan ya da 3'ten Daha Az Ders Alan Öğrencilerin:\n"
      "Sayisi:  {}\n"
      "Yüzdesi:  {}\n".format(azDersAlanOgrenciSayisi, azDersAlanOgrenciSayisi / ogr_sayisi * 100))

print("O Dönem Aldığı Derslerin Kredi ya da Sayısına göre %75ten \n"
      "Daha Fazla Derste Başarılı Olmuş Öğrenci Sayısı:  {}  Yüzdesi:  {}\n".format(basarıOranı75,
                                                                                  basarıOranı75 / ogr_sayisi * 100))

print("300Tl den Fazla Burs Alan Öğrenci Sayısı:  {}".format(yuksekBursMiktari))

print("Okul 1.Sinin: \n"
      "İsim Soyisimi:  {}\n"
      "Aldığı Ders Sayısı:  {}\n"
      "Aldığı Derslerin Kredisi:  {}\n"
      "Not Ortalaması:  {}\n"
      "Gelecek Dönem Alacağı Burs Miktarı:  {}\n".format(enYuksekIsim, enYuksekDersSayisi, enYuksekToplamKredi,
                                                       enYuksekOrtalama, enBasariliOgrBurs))

print("Gelecek Dönem En Çok Burs Alacak Olan Öğrencinin:\n"
      "İsim Soyisimi:  {}\n"
      "Aldığı Ders Sayısı:  {}\n"
      "Aldığı Derslerin Kredisi:  {}\n"
      "Not Ortalaması:  {}\n"
      "Gelecek Dönem Alacağı Burs Miktarı:  {}\n".format(maxBursİsim,maxBursDersSayisi,maxBursKredi,maxBursOrtalama,maxBurs))

print("Gelecek Dönem Ödenecek Aylık Burs Miktarı:  {}\n".format(totalBursOdenek))
