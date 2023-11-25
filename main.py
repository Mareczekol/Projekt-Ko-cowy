import random
import smtplib
from email.mime.text import MIMEText
import customtkinter
import requests
from bs4 import BeautifulSoup
from customtkinter import *
from email.mime.multipart import MIMEMultipart


set_appearance_mode("Dark")
set_default_color_theme("blue")
appWidth, appHeight = 1000, 1300


def get_recipe_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    skladniki = soup.find("div", class_="group-skladniki "
                                        "field-group-div")
    przygotowanie = soup.find("div",
                              class_="field field-name-field-przygotowanie "
                                     "field-type-text-long field-label-"
                                     "above")
    scraped_skladniki = ' '.join(
            element.get_text() for element in skladniki)
    scraped_przygotowanie = ' '.join(
            element.get_text() for element in przygotowanie)
    return scraped_skladniki, scraped_przygotowanie


class GUI(customtkinter.CTk):
    """
       A class to design the graphic interface:
        - buttons
        - labels
        - view tabs
       """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food App")
        self.geometry(f"{appWidth}x{appHeight}")

        self.viewTab = CTkTabview(self)
        self.viewTab.grid(padx=200, pady=10, sticky="e")
        self.viewTab.add("Śniadanie")
        self.viewTab.add("Obiad")
        self.viewTab.add("Kolacja")

        # Tab. 1 - śniadanie
        self.platki_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                    text="Płatki", command=self.platki_btn)
        self.platki_btn.grid(padx=80, pady=20, sticky="sw")

        self.jajka_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                   text="Jajka", command=self.jajka_btn)
        self.jajka_btn.grid(padx=80, pady=25, sticky="sw")

        self.jaglanka_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                      text="Jaglanka",
                                      command=self.jaglanka_btn)
        self.jaglanka_btn.grid(padx=80, pady=30, sticky="sw")

        self.placki_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                    text="Placki", command=self.placki_btn)
        self.placki_btn.grid(padx=80, pady=35, sticky="sw")

        # Tab 2 - obiad
        self.losos_btn = CTkButton(self.viewTab.tab("Obiad"),
                                   text="Łosoś", command=self.losos_btn)
        self.losos_btn.grid(padx=80, pady=20, sticky="sw")

        self.kurczak_btn = CTkButton(self.viewTab.tab("Obiad"),
                                     text="Kurczak", command=self.kurczak_btn)
        self.kurczak_btn.grid(padx=80, pady=25, sticky="sw")

        self.beef_btn = CTkButton(self.viewTab.tab("Obiad"),
                                  text="Wołowina", command=self.beef_btn)
        self.beef_btn.grid(padx=80, pady=30, sticky="sw")

        self.pork_btn = CTkButton(self.viewTab.tab("Obiad"),
                                  text="Wieprzowina", command=self.pork_btn)
        self.pork_btn.grid(padx=80, pady=35, sticky="sw")

        # Tab. 3 - kolacja
        self.light_btn = CTkButton(self.viewTab.tab("Kolacja"),
                                   text="Lekka kolacja", command=self.light_btn)
        self.light_btn.grid(padx=80, pady=20, sticky="sw")

        self.warm_btn = CTkButton(self.viewTab.tab("Kolacja"),
                                  text="Kolacja na ciepło",
                                  command=self.warm_btn)
        self.warm_btn.grid(padx=80, pady=25, sticky="sw")

        self.recipe_text = CTkTextbox(self, width=800, height=800)
        self.recipe_text.grid(row=7, column=0, columnspan=4, padx=20, pady=20,
                              sticky="nsew")

        # email button
        self.email_btn = CTkButton(self, text="Wyślij na email",
                                   command=self.email_btn)
        self.email_btn.grid(row=8, column=0, padx=30, pady=30,
                            sticky="nsew")

    def platki_btn(self):
        urls = [
            "https://www.kwestiasmaku.com/przepis/musli-z-jablkiem",
            "https://www.kwestiasmaku.com/przepis/owsianka-z-chia-i-granatem",
            "https://www.kwestiasmaku.com/dania_dla_dwojga/sniadania/chia/"
            "przepis.html"
        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def jajka_btn(self):
        urls = [
            "https://www.kwestiasmaku.com/przepis/pasztet-jajeczny",
            "https://www.kwestiasmaku.com/przepis/tosty-z-omletem",
            "https://www.kwestiasmaku.com/przepis/tortille-z-cukinii"
        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def jaglanka_btn(self):
        urls = [
            "https://www.kwestiasmaku.com/przepis/jaglanka-z-owocami-"
            "egzotycznymi",
            "https://www.kwestiasmaku.com/przepis/jaglanka-z-jagodami",
            "https://www.kwestiasmaku.com/dania_dla_dwojga/sniadania/jaglanka_"
            "z_mlekiem_kokosowym_zurawina/przepis.html"
        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def placki_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/zielony_srodek/salatki_jablka/"
                "placki_serowe_z_jablkami_rodzynkami/przepis.html",
                "https://www.kwestiasmaku.com/kuchnia_polska/placki/placki_"
                "bezglutenowe/przepis.html",
                "https://www.kwestiasmaku.com/przepis/placki-twarogowe-z-"
                "jablkiem"
        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def kurczak_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/souvlaki-z-kurczaka",
                "https://www.kwestiasmaku.com/przepis/stripsy-z-kurczaka",
                "https://www.kwestiasmaku.com/przepis/makaron-udon-z-mielonym-"
                "miesem-drobiowym-warzywami-i-sosem-satay"

        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def losos_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/makaron-z-lososiem-"
                "szpinakiem-i-suszonymi-pomidorami",
                "https://www.kwestiasmaku.com/przepis/losos-pieczony-w-"
                "czerwonym-pesto",
                "https://www.kwestiasmaku.com/przepis/losos-pieczony-w-"
                "syropie-klonowym"

        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def beef_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/stir-fry-z-wolowina-i-"
                "brokulami",
                "https://www.kwestiasmaku.com/przepis/gulasz-wolowy-z-"
                "ziemniakami-i-marchewka",
                "https://www.kwestiasmaku.com/przepis/steki-wolowe-po-francusku"

        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def pork_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/schab-z-suszonymi-"
                "pomidorami",
                "https://www.kwestiasmaku.com/przepis/karkowka-pieczona-w-"
                "plastrach",
                "https://www.kwestiasmaku.com/przepis/schab-w-sosie-wlasnym"

        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def light_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/koktajl-bananowy",
                "https://www.kwestiasmaku.com/przepis/salatka-z-truskawkami-"
                "feta-i-orzechami",
                "https://www.kwestiasmaku.com/przepis/warzywne-curry-z-cukinia"

        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    def warm_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/makaron-kokardki-z-"
                "boczkiem-i-smietanka",
                "https://www.kwestiasmaku.com/przepis/medaliony-warzywne",
                "https://www.kwestiasmaku.com/przepis/placki-z-batatow-na-"
                "slodko"
        ]
        url = random.choice(urls)
        scraped_skladniki, scraped_przygotowanie = get_recipe_data(url)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", scraped_przygotowanie)
        self.recipe_text.insert("1.0", scraped_skladniki)

    """
    Funkcja wysyłania maila nie działa ze względu na zablokowany przez GOOGLE 
    dostęp mniej zaufanych aplikacji
    """
    def email_btn(self):
        input_field = CTkInputDialog(text="Podaj email")
        email = input_field.get_input()
        print(email)

        # Get the recipe data, Retrieve the text from the recipe_text widget
        recipe_data = self.recipe_text.get("1.0", "end-1c")

        # Wywołaj funkcję send_email z przekształconą wartością zmiennej email
        self.send_email('mailbot028@gmail.com',
                        'Mare8Czekol', email, 'Przepis',
                        recipe_data)

    @staticmethod
    def send_email(sender_email, sender_password, recipient_email,
                   subject, message):
        # Utwórz wiadomość e-mail
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Dodaj treść wiadomości
        msg.attach(MIMEText(message, 'plain'))

        # Zapisz treść wiadomości do pliku przepis.txt
        with open('przepis.txt', 'w') as file:
            file.write(message)

        # Dodaj plik przepis.txt jako załącznik
        with open('przepis.txt', 'rb') as file:
            attachment = MIMEText(file.read(), 'plain', 'utf-8')
            attachment.add_header('Content-Disposition', 'attachment',
                                  filename='przepis.txt')
            msg.attach(attachment)

        # Utwórz połączenie z serwerem SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Wyślij wiadomość e-mail
        server.send_message(msg)
        server.quit()


class FoodApp(GUI):
    """
    a class that builds the app based on the design of the class
    """
    def build(self):
        return GUI()


if __name__ == "__main__":
    FoodApp().mainloop()
