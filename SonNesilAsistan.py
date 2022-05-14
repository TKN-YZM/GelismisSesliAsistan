import random
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import cv2

r=sr.Recognizer()

class SesliAsistan():

    def seslendirme(self,metin):
        xtts=gTTS(text=metin,lang="tr")
        dosya="dosya"+str(random.randint(0,1242312412312))+".mp3"
        xtts.save(dosya)
        playsound(dosya)
        #os.remove("C:/Users/apoba/Desktop/PythonProje/dosya")

    def ses_kayit(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyoruz...")
            listen=r.listen(kaynak)
            voice=" "

            try:
                voice=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("Ne söylediğinizi anlayamadım.Lutfen tekrar ediniz")

            return voice


    def ses_karsilik(self,gelen_ses):

            if "selam" in gelen_ses:
                self.seslendirme("Size de selamlar")
            elif "merhaba" in gelen_ses:
                self.seslendirme("Size de merhabalar")
            elif "nasılsın" in gelen_ses:
                self.seslendirme("iyim siz nasılsınız")
            elif "nasıl gidiyor" in gelen_ses:
                self.seslendirme("iyi sizin?")

            elif "video aç" in gelen_ses or "müzik aç" in gelen_ses or "youtube aç" in gelen_ses:

                try:
                    self.seslendirme("Ne açmamı istersiniz?")
                    veri=self.ses_kayit()
                    self.seslendirme("{} açılıyor...".format(veri))
                    time.sleep(1)
                    url="https://www.youtube.com/results?search_query={}".format(veri)
                    tarayici=webdriver.Chrome()
                    tarayici.get(url)
                    buton=tarayici.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()
                except:
                    self.seslendirme("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")

            elif "google aç" in gelen_ses or "arama yap" in gelen_ses:

                try:
                    self.seslendirme("Ne aramamı istersiniz")
                    veri=self.ses_kayit()
                    self.seslendirme("{} için bulduklarım bunlar".format(veri))
                    url="https://www.google.com/search?q={}".format(veri)
                    tarayici=webdriver.Chrome()
                    tarayici.get(url)
                    buton=tarayici.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div[1]/a/h3").click()

                except:
                    self.seslendirme("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")

            elif "film aç" in gelen_ses:
                try:
                    self.seslendirme("Hangi filmi açmamı istersiniz")
                    veri=self.ses_kayit()
                    self.seslendirme("{} filmini açıyorum....".format(veri))

                    url="https://www.google.com/search?q={}+izle".format(veri)

                    tarayici=webdriver.Chrome()
                    tarayici.get(url)

                    buton=tarayici.find_element_by_xpath("//*[@id='rso']/div[2]/div/div[1]/div/a/h3")
                    buton.click()
                except:
                    self.seslendirme("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")

            elif "film önerisi yap" in gelen_ses:
                try:
                    self.seslendirme("hangi tür film istersinz")
                    veri=self.ses_kayit()
                    self.seslendirme("{} türü için bulduğum filmler şunlar...".format(veri))
                    url="https://www.filmmodu2.com/kategori/{}".format(veri)
                    tarayici=webdriver.Chrome()
                    tarayici.get(url)
                    self.seslendirme("Eğer kararsızsanız size film önerisinde bulunmak istiyorum")
                    cevap=self.ses_kayit()
                    print(cevap)
                    time.sleep(2)

                    if cevap=="Evet":
                        self.seslendirme("Filminizi hemen getiriyorum....")
                        rastgele_sayi=random.randint(1,24)
                        buton=tarayici.find_element_by_xpath("/html/body/main/div[2]/div[{}]/div/a".format(rastgele_sayi))
                        buton.click()
                        veri1=buton.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[2]/div/div/p[1]/text()")
                        print(veri1)

                        self.seslendirme("Keyifli seyirler...")
                    else:
                        self.seslendirme("Keyifli seyirler...")

                except:
                    self.seslendirme("internetten kaynaklı bir hata meydana geldi.lütfen internetinizi kontrol ediniz")


            elif "hava durumu" in gelen_ses or "hava durumu tahmini" in gelen_ses:

                try:
                    self.seslendirme("hangi şehrin hava durumunu istersiniz")
                    cevap=self.ses_kayit()
                    url = "https://www.ntvhava.com/{}-hava-durumu".format(cevap)
                    request = requests.get(url)
                    html_icerigi = request.content
                    soup = BeautifulSoup(html_icerigi, "html.parser")
                    gunduz_sicakliklari = soup.find_all("div",
                                                        {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
                    gece_sicakliklari = soup.find_all("div",
                                                      {"class": "daily-report-tab-content-pane-item-box-bottom-degree-small"})
                    hava_durumları = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})

                    gun_isimleri = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-date"})

                    gunduz = []
                    gece = []
                    hava = []
                    gunler = []

                    for x in gunduz_sicakliklari:
                        x = x.text
                        gunduz.append(x)
                    for y in gece_sicakliklari:
                        y = y.text
                        gece.append(y)
                    for z in hava_durumları:
                        z = z.text
                        hava.append(z)

                    for a in gun_isimleri:
                        a = a.text
                        a = a[0:3:]
                        if (a == "Cmt"):
                            a = "Cumartesi"
                        elif (a == "Paz"):
                            a = "Pazar"
                        elif (a == "Pzt"):
                            a = "Pazartesi"
                        elif (a == "Sal"):
                            a = "Salı"
                        elif (a == "Çar"):
                            a = "Çarşamba"
                        elif (a == "Per"):
                            a = "Perşembe"
                        elif (a == "Cum"):
                            a = "Cuma"
                        gunler.append(a)

                    self.seslendirme("{} şehiri için günlük , yarının ya da 5 günlük hava raporlarını mı istersiniz".format(cevap))
                    cevap2=self.ses_kayit()

                    if(cevap2=="bugünün" or cevap2=="günlük"):
                        saat=datetime.now().strftime("%H:%M")
                        if(saat<="17:00"):
                            self.seslendirme("{} için hava durumu bugün şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[0],gunduz[0],gece[0]))
                        else:
                            self.seslendirme("{} için hava durumu bu akşam şöyle: {} gece sıcaklığı :{}".format(cevap,hava[0],gece[0]))

                    elif(cevap2=="yarın" or cevap2=="yarınınki" or cevap2=="ertesi günün"):
                        self.seslendirme("{} için yarın hava durumu şöyle: {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[1],gunduz[1],gece[1]))

                    elif(cevap2=="beş günlük" or cevap2=="haftalık"):
                        saat=datetime.now().strftime("%H:%M")
                        if(saat<="17:00"):
                            self.seslendirme("{} için hava durumu bugün şöyle: {} gündüz sıcaklığı {} gece sıcaklığı: {}"
                                             "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                             "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                             "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                             "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap,hava[0],gunduz[0],gece[0],hava[1],gunduz[1],gece[1],gunler[2],hava[2],gunduz[2],gece[2],gunler[3],hava[3],gunduz[3],gece[3],gunler[4],hava[4],gunduz[4],gece[4]))

                        else:
                            self.seslendirme("{} için hava durumu bugün şöyle: {} gece sıcaklığı: {}"
                                                "yarın {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}"
                                                "{} {} gündüz sıcaklığı: {} gece sıcaklığı: {}".format(cevap, hava[0],
                                                                                                        gece[0],
                                                                                                        hava[1], gunduz[1],
                                                                                                        gece[1], gunler[2],
                                                                                                        hava[2], gunduz[2],
                                                                                                        gece[2], gunler[3],
                                                                                                        hava[3], gunduz[3],
                                                                                                        gece[3], gunler[4],
                                                                                                        hava[4], gunduz[4],
                                                                                                        gece[4]))
                except:
                    self.seslendirme("istediğinz şehre göre bir içerik bulunamadı.lütfen istediğinz şehri veya internetinizi kontrol ediniz")

            elif "fotoğraf çek" in gelen_ses or "fotoğraf" in gelen_ses:
                self.seslendirme("kameranızı hemen açıyorum...")
                kamera=cv2.VideoCapture(0)
                x,resim=kamera.read()
                cv2.imwrite("denemeresim.jpg",resim)
                self.seslendirme("gülümseyin çekiyorum...")
                kamera.release()
                cv2.destroyAllWindows()
                time.sleep(2)
                self.seslendirme("fotoğrafınızı görmek istiyor musunuz")
                cevap=self.ses_kayit()
                if(cevap=="Evet"):
                    resim=cv2.imread("denemeresim.jpg")
                    cv2.imshow("Deneme Resim",resim)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    pass

            elif "oyun zamanı" in gelen_ses or "oyun aç" in gelen_ses:
                self.seslendirme("oynunuzu hemen açıyorum.keyifli oyunlar dilerim")
                os.startfile("uplay://launch/46/0")


asistan=SesliAsistan()

def uyanma_fonksiyonu(metin):
    if(metin=="hey siri" or metin=="siri"):
        asistan.seslendirme("dinliyorum...")
        cevap=asistan.ses_kayit()
        if(cevap!=""):
            asistan.ses_karsilik(cevap)

while True:
    ses=asistan.ses_kayit()
    if(ses!=" "):
        ses=ses.lower()
        print(ses)
        uyanma_fonksiyonu(ses)
