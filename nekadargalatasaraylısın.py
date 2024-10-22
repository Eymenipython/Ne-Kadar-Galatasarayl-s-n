def giris():
    print("Ne Kadar Galatasaraylısın oyununa hoş geldiniz.")
    print("Oyunumuz 5 sorudan oluşmaktadir.")
    print("Her sorunun değeri katlanarak artmaktadir.")
    print("Sorulari yanitlamak için 'A', 'B', 'C' veya 'D' tuşlarina basiniz.")
    print("Oyundan çikmak için 'Q' tuşuna basiniz.")
    print("Başarilar dileriz.")
    print("****************************************************")

def dosyadan_soru_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            sorular = dosya.read()
    except:
        print("Dosya okuma hatasi!")
        return None
    
    soru_listesi = sorular.split("*")
    return soru_listesi

def soru_yazdir(soru):
    print(soru)

def cevap_al():
    while True:
        cevap = input("Cevabinizi giriniz: ")
        if cevap.upper() == "Q":
            print("Oyundan çikiliyor...")
            exit()
        elif cevap.upper() in ["A", "B", "C", "D"]:
            return cevap
        else:
            print("Geçersiz cevap! Lütfen 'A', 'B', 'C' veya 'D' tuşlarina basiniz.")

def cevap_kontrol(cevap, dogru_cevap):
    dogru_cevap = dogru_cevap.strip()  # Doğru cevabı temizlemek
    return cevap.upper() == dogru_cevap

def puan_hesapla(dogru_cevap_sayisi):
    return dogru_cevap_sayisi**3 * 4000

def oyun():
    dogru_cevap_sayisi = 0
    soru_listesi = dosyadan_soru_oku("C:\Python Dersleri\proje günü/gssorular.txt")
    if soru_listesi is None:
        return
    
    giris()
    i = 0
    while i < len(soru_listesi) - 1:
        soru = soru_listesi[i]
        dogru_cevap = soru_listesi[i + 1]
        soru_yazdir(soru)
        kullanici_cevap = cevap_al()
        if cevap_kontrol(kullanici_cevap, dogru_cevap):
            print("Tebrikler! Doğru cevap!")
            dogru_cevap_sayisi += 1
        else:
            print("Yanliş cevap!")
            break
        i += 2
    
    odul = puan_hesapla(dogru_cevap_sayisi)
    print("Toplam kazanciniz: ", odul, "TL")

def main():
    oyun()

main()
