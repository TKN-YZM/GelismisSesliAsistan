import random
import time
import webbrowser
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from selenium import webdriver
from bs4 import  BeautifulSoup
import requests

r=sr.Recognizer()

class Asistan():
    def seslendirme(self,metin):
        tts=gTTS(text=metin,lang="tr")
        dosya="ses"+str(random.randint(0,23132321321))+".mp3"
        tts.save(dosya)
        playsound(dosya)

    def mikrofon(self):
        with sr.Microphone() as source:
            print("Sizi dinliyoruz")
            listen=r.listen(source)
            voice=" "
            try:
                voice=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("Ne dediğinizi anlayamadım...")
            return voice

    def karsilik(self,veri):
        if "selam" in veri :
            self.seslendirme("Selamlar Efendim")

        elif "merhaba" in veri or "naber" in veri:
            self.seslendirme("Merhaba efendim")

        elif "film aç" in veri :
            self.seslendirme("Hangi filmi açmamı istersiniz?")
            film_ismi=self.mikrofon()
            time.sleep(1)
            self.browser=webdriver.Chrome()
            self.browser.get("https://www.google.com/search?q={}".format(film_ismi))
            self.seslendirme("{} filmi açılıyor...".format(film_ismi))
            veri=self.browser.find_element_by_xpath("//*[@id='rso']/div[2]/div/div[1]/div/a/h3")
            veri.click()

        elif "film türü" in veri or "film önerisi" in veri or "öneri film" in veri:
            self.seslendirme("hangi tür film istersin?")
            film = self.mikrofon()

            if "bilim kurgu" in film:
                film = 'bilim-kurgu'
            elif "aile filmleri" in film or "aile" in film:
                film = 'aile-filmleri'
            elif "kült filmler" in film or "kült" in film:
                film = 'kult-filmler-izle'
            elif "komedi" in film:
                film = "hd-komedi-filmleri"

            webbrowser.get().open("https://www.filmmodu2.com/kategori/{}".format(film))
            self.seslendirme("{} tür filmler için bulduklarım bunlar".format(film))
            time.sleep(2)


        elif "müzik aç" in veri or "video aç" in veri or "youtube aç" in veri:
            self.seslendirme("Ne açmamı istersiniz? ")
            isim=self.mikrofon()
            url="https://www.youtube.com/results?search_query={}".format(isim)
            self.seslendirme("{} açılıyor...".format(isim))
            browser2=webdriver.Chrome()
            browser2.get(url)
            browser2.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()


        elif "hava durumu tahmini" in veri or "hava durumu" in veri or "yarın hava ne olacak" in veri:
            self.seslendirme("Hangi sehrin hava durumunu istersiniz?")
            sehir_ismi=self.mikrofon()

            url = "https://www.ntvhava.com/{}-hava-durumu".format(sehir_ismi)
            response = requests.get(url)
            html_icerigi = response.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            gunduz = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-box-bottom-degree-big"})
            gece = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-box-bottom-degree-small"})
            hava = soup.find_all("div", {"class", "daily-report-tab-content-pane-item-text"})

            gunduz_sicakliklari = []
            gece_sicakliklari = []
            hava_olayi = []

            for y in gunduz:
                gunduz_sicakliklari.append(y.text)

            for x in gece:
                gece_sicakliklari.append(x.text)

            for a in hava:
                hava_olayi.append(a.text)

            yarin_durum="Yarınki hava tahmini şu şekilde: {} gündüz sıcaklığı: {} gece sıcaklığı {}".format(hava_olayi[0],gunduz_sicakliklari[0],gece_sicakliklari[0])

            self.seslendirme(yarin_durum)


asistan=Asistan()
while True:
    ses=asistan.mikrofon()
    if(ses!=" "):
        ses=ses.lower()
        print(ses)
        asistan.karsilik(ses)




