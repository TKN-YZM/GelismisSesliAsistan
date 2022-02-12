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


r=sr.Recognizer()

class SesliAsistan():


    def seslendirme(self,metin):
        xtts=gTTS(text=metin,lang="tr")
        dosya="dosya"+str(random.randint(0,1242312412312))+".mp3"
        xtts.save(dosya)
        playsound(dosya)

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

        elif "video aç" in gelen_ses or "müzik aç" in gelen_ses or "youtube aç" in gelen_ses:
            self.seslendirme("Ne açmamı istersiniz?")
            veri=self.ses_kayit()
            self.seslendirme("{} açılıyor...".format(veri))
            time.sleep(1)
            url="https://www.youtube.com/results?search_query={}".format(veri)
            tarayici=webdriver.Chrome()
            tarayici.get(url)
            buton=tarayici.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()

        elif "google aç" in gelen_ses or "arama yap" in gelen_ses:
            self.seslendirme("Ne aramamı istersiniz")
            veri=self.ses_kayit()
            self.seslendirme("{} için bulduklarım bunlar".format(veri))
            url="https://www.google.com/search?q={}".format(veri)
            tarayici=webdriver.Chrome()
            tarayici.get(url)
            buton=tarayici.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div[1]/a/h3").click()

        elif "film aç" in gelen_ses:
            self.seslendirme("Hangi filmi açmamı istersiniz")
            veri=self.ses_kayit()
            self.seslendirme("{} filmini açıyorum....".format(veri))

            url="https://www.google.com/search?q={}+izle".format(veri)

            tarayici=webdriver.Chrome()
            tarayici.get(url)

            buton=tarayici.find_element_by_xpath("//*[@id='rso']/div[2]/div/div[1]/div/a/h3")
            buton.click()




        elif "film önerisi yap" in gelen_ses:
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


        elif "hava durumu tahmini" in gelen_ses or "hava durumu" in gelen_ses:
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
            gunduz = []
            gece = []
            hava = []
            for x in gunduz_sicakliklari:
                x = x.text
                gunduz.append(x)
            for y in gece_sicakliklari:
                y = y.text
                gece.append(y)
            for z in hava_durumları:
                z = z.text
                hava.append(z)
            birleştirme="{} için yarınki hava raporları şöyle {} gündüz sıcaklığı {} gece sıcaklığı {}".format(cevap,hava[1],gunduz[1],gece[1])

            self.seslendirme(birleştirme)




asistan=SesliAsistan()

while True:
    ses=asistan.ses_kayit()
    if(ses!=" "):
        ses=ses.lower()
        print(ses)
        asistan.ses_karsilik(ses)
