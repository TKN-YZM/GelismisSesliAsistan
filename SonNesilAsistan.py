import speech_recognition as sr
from playsound import playsound
from bs4 import BeautifulSoup
from gtts import gTTS
from random import randint
from datetime import datetime
import webbrowser
import random
import time
import os
import requests

r=sr.Recognizer()

class Asistan():

    def seslendirme(self,ses):
        tts=gTTS(text=ses,lang="tr")
        rand = random.randint(1,100)
        dosya="C:/Users/apoba/Desktop/PythonProje/{}.mp3".format(str(rand))
        time.sleep(1)
        tts.save(dosya)
        time.sleep(1)
        playsound(dosya)
        print(playsound)


    def ses_kayit(self):
        with sr.Microphone() as source:
            print("Seni dinliyorum")
            listen=r.listen(source)
            voice = ''
            try:
                voice=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("Ne dediğiniz anlaşılmadı")

            return voice

    def hava_durumu(self,sehir):

            url = "https://www.ntvhava.com/{}-hava-durumu".format(sehir)
            response = requests.get(url)
            html_icerigi = response.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            day = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-date"})
            gunduz_sicaklik = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-box-bottom-degree-big"})
            gece_sicakligi = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-box-bottom-degree-small"})
            hava_durumu = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-text"})

            liste = []
            liste2 = []
            liste3 = []
            liste4 = []
            liste5 = []

            for x in day:
                for y in x:
                    liste.append(y)

            ses = liste[0]
            yses = ses[0:3:]
            # print(yses)

            ses_1 = liste[1]
            yses_1 = ses_1[0:3:]
            # print(yses_1)

            ses_2 = liste[2]
            yses_2 = ses_2[0:3:]
            # print(yses_2)

            ses_3 = liste[3]
            yses_3 = ses_3[0:3:]
            # print(yses_3)


            # gündüz hava sıcaklığı
            for a in gunduz_sicaklik:
                for b in a:
                    liste2.append(b)

            ses2 = liste2[0]  # bugünki havanın gündüz sıcaklığı (örn perşembe)
            sonses2 = ses2 + "derece"
            # print(sonses2)

            ses2_1 = liste2[3]  # yarınki havanın gündüz sıcaklığı (cuma)
            sonses2_1 = ses2_1 + "derece"
            # print(sonses2_1)

            ses2_2 = liste2[6]  # yarından sonraki günün hava sıcaklığı (cumartesi)
            sonses2_2 = ses2_2 + "derece"
            # print(sonses2_2)

            ses2_3 = liste2[9]  # pazar
            sonses2_3 = ses2_3 + "derece"
            # print(sonses2_3)


            # gece hava sıcaklığı
            for i in gece_sicakligi:
                for x in i:
                    liste3.append(x)

            ses3 = liste3[0]  # bugünkü hava durumu
            ses3 = ses3.replace("/", "")
            sonses3 = ses3 + "derece"
            # print(sonses3)

            ses3_1 = liste3[3]  # yarınki hava durumu
            ses3_1 = ses3_1.replace("/", "")
            sonses3_1 = ses3_1 + "derece"
            # print(sonses3_1)

            ses3_2 = liste3[6]
            ses3_2 = ses3_2.replace("/", "")
            sonses3_2 = ses3_2 + "derece"
            # print(sonses3_2)

            ses3_3 = liste3[9]
            ses3_3 = ses3_3.replace("/", "")
            sonses3_3 = ses3_3 + "derece"
            # print(sonses3_3)

            # hava durumu (parçalı bulutlu vs)
            for w in hava_durumu:
                for k in w:
                    liste4.append(k)

            ses4 = liste4[0]
            if ses4=="Sıcak Hava":
                ses4="güneşli"
            sonses4 = ses4
            # print(ses4)

            ses4_1 = liste4[1]
            if ses4_1=="Sıcak Hava":
                ses4_1="güneşli"
            sonses4_1 = ses4_1
            # print(ses4_1)

            ses4_2 = liste4[2]
            if ses4_2=="Sıcak Hava":
                ses4_2="güneşli"
            sonses4_2 = ses4_2
            # print(ses4_2)

            ses4_3 = liste4[3]
            if ses4_3=="Sıcak Hava":
                ses4_3="güneşli"
            sonses4_3 = ses4_3
            # print(ses4_3)

            self.topluses_bugun = "{} hava durumu bugün şu şekilde: ......".format(sehir) + "gün içinde hava" + sonses4 + "gündüz sıcaklığı" + sonses2 + "................." + "gece sıcaklığı" + sonses3
            self.topluses_yarin = "{} hava durumu yarın şu şekilde:......".format(sehir) + sonses4_1 + "gündüz sıcaklığı" + sonses2_1 + "gecesıcaklığı" + sonses3_1
            time = datetime.now().strftime("%H:%M")
            if time >= "16:00":
                self.topluses_bugun = "{} hava durumu bu gece şu şekilde: ".format(sehir) + sonses3


    def ses_karsilik(self,ses):
        if "merhaba" in ses:
            self.seslendirme("Sanada merhaba patron,umarım iyisindir")
        if "nasılsın" in ses:
            self.seslendirme("iyiyim sen nasılsın???")
        if "nasıl gidiyor" in ses:
            self.seslendirme("iyi gidiyor,seninki nasıl gidiyor?")
        if "saat kaç" in ses:
            saat=datetime.now().strftime("%H:%M")
            a=["Saat: ","hemen bakıyorum","saat şuan: "]
            secenek=random.choice(a)+saat
            self.seslendirme(secenek)

        if "google'da arama yap" in ses:
            self.seslendirme("ne aramamı istersiniz?")
            arama=self.ses_kayit()
            webbrowser.get().open("https://www.google.com/search?q={}".format(arama))
            self.seslendirme("google içindeki aramam bu şekilde")


        if "youtube'dan video aç" in ses or "video aç" in ses or "müzik aç" in ses:
            self.seslendirme("ne açiyim")
            y_ses=self.ses_kayit()
            webbrowser.get().open("https://www.youtube.com/results?search_query={}".format(y_ses))
            self.seslendirme("{} hakkındaki videolar bunlar".format(y_ses))


        if "hava durumu" in ses:
            self.seslendirme("hangi şehrin hava tahminini istersiniz?")
            sehir=self.ses_kayit()
            self.hava_durumu(sehir)
            self.seslendirme(self.topluses_bugun)
            self.seslendirme(self.topluses_yarin)


        if "film aç" in ses:
            self.seslendirme("hangi tür film istersin?")
            film=self.ses_kayit()
            if "bilim kurgu" in film :
                film='bilim-kurgu'
            if "aile filmleri"in film or "aile" in film:
                film='aile-filmleri'
            if "kült filmler"in film:
                film='kult-filmler-izle'

            webbrowser.get().open("https://www.filmmodu.org/kategori/{}".format(film))
            self.seslendirme("{} tür filmler için bulduklarım bunlar".format(film))
            time.sleep(2)
            if "korku" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/korku-293')
                self.seslendirme("bu filmler benim favori filmlerimdendir,keyifli seyirler")
            if "komedi" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/komedi-218')
                self.seslendirme('bu filmler benim komedi türündeki en sevdiklerimdendir,keyifli seyirler')
            if "animasyon" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/aile-78')
                self.seslendirme('bu filmler benim favori filmlerimdendir,keyifli seyirler')
            if "aksiyon" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/aksiyon-307')
                self.seslendirme('bu filmler benim favori filmlerimdendir,keyifli seyirler')
            if "gizem" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/gizem-49')
                self.seslendirme('bu filmler benim favori temalı filmlerimdir,keyifli seyirler')
            if "savaş" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open('https://www.filmmodu.org/liste/savas-97')
                self.seslendirme('bu filmler benim favori filmlerimdendir,keyifli seyirler')
            if "bilim-kurgu" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open("https://www.filmmodu.org/liste/bilim-kurgu-255")
                self.seslendirme("Bilimkurgu türündeki favori filmlerim bunlar,keyifli seyirler")
            if "aile-filmleri" in film:
                self.seslendirme("eğer kararsızsan sana {}  türündeki favori film listemi açıyorum".format(film))
                webbrowser.get().open("https://www.filmmodu.org/liste/aile-78")
                self.seslendirme("Aile türündeki favori filmlerim bunlar,keyifli seyirler")

        if "kripto borsası" in ses:
            self.seslendirme('hemen açıyorum,bol kazançlar')
            webbrowser.get().open("https://pro.btcturk.com/pro/al-sat/BTC_USDT")

        if "robotik kodlama dersleri"in ses:
            self.seslendirme('hemen açıyorum...')
            webbrowser.get().open("https://www.youtube.com/playlist?list=PLDRcccSktQd5mfXDtGv975V77RCrW6H7U")
            self.seslendirme("iyi çalışmalar")

        if "borsa aç" in ses or "dolar grafiği" in ses :
            self.seslendirme("hemen açıyorum")
            webbrowser.get().open("https://tr.tradingview.com/chart/8gqYUUZC/?symbol=FX%3AUSDTRY")
            self.seslendirme("bol kazançlar")


asistan=Asistan()
while True:
    ses=asistan.ses_kayit()
    if ses!="":
        ses=ses.lower()
        print(ses)
        asistan.ses_karsilik(ses)
