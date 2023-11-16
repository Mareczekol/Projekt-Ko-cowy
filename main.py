import requests
from bs4 import BeautifulSoup
import customtkinter
from customtkinter import *
import random
from PIL import ImageTk, Image

set_appearance_mode("Dark")
set_default_color_theme("blue")
appWidth, appHeight = 1000, 1300


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food App")
        self.geometry(f"{appWidth}x{appHeight}")

        # img = ImageTk.PhotoImage(Image.open(""))
        # l1 = CTkLabel(master=app, image=img)
        # l1.pack()
        #
        # View Tab
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

    def platki_btn(self):
        urls = ["https://www.kwestiasmaku.com/przepis/musli-z-jablkiem",
                "https://www.kwestiasmaku.com/przepis/owsianka-z-chia-i-"
                "granatem",
                "https://www.kwestiasmaku.com/dania_dla_dwojga/sniadania/chia/"
                "przepis."
                "html",
                ]
        url = random.choice(urls)
        response = requests.get(url)
        # print(response.content)  # Debug: Print the response content
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        # skladniki_1 = soup.find(soup.find("div", class_="recipe--"
        #                                                 "ingredients--list"))
        # przygotowanie_1 = soup.find("div", class_="recipeStepsComponent")

        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)
        # scraped_1 = ' '.join(element.get_text() for element in przygotowanie_1)
        # self.recipe_text.insert("1.0", scraped_1)
        # scraped_text_1 = ' '.join(element.get_text() for element in skladniki_1)
        # self.recipe_text.insert("1.0", scraped_text_1)

        # debug
        # print(scraped_text)
        # print(scraped)

    def jajka_btn(self):
        urls = [
            "https://www.kwestiasmaku.com/przepis/pasztet-jajeczny",
            "https://www.kwestiasmaku.com/przepis/tosty-z-omletem",
            "https://www.kwestiasmaku.com/przepis/tortille-z-cukinii"
        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", str.format(scraped))
        scraped_text = ' '.join(element.get_text() for element in skladniki)

        self.recipe_text.insert("1.0", str.format(scraped_text))

    def jaglanka_btn(self):
        urls = [
            "https://www.kwestiasmaku.com/przepis/jaglanka-z-owocami-"
            "egzotycznymi",
            "https://www.kwestiasmaku.com/przepis/jaglanka-z-jagodami",
            "https://www.kwestiasmaku.com/dania_dla_dwojga/sniadania/jaglanka_"
            "z_mlekiem_kokosowym_zurawina/przepis.html"
        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

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
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

    def kurczak_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/souvlaki-z-kurczaka",
                "https://www.kwestiasmaku.com/przepis/stripsy-z-kurczaka",
                "https://www.kwestiasmaku.com/przepis/makaron-udon-z-mielonym-"
                "miesem-drobiowym-warzywami-i-sosem-satay"

        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

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
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

    def beef_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/stir-fry-z-wolowina-i-"
                "brokulami",
                "https://www.kwestiasmaku.com/przepis/gulasz-wolowy-z-"
                "ziemniakami-i-marchewka",
                "https://www.kwestiasmaku.com/przepis/steki-wolowe-po-francusku"

        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

    def pork_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/schab-z-suszonymi-"
                "pomidorami",
                "https://www.kwestiasmaku.com/przepis/karkowka-pieczona-w-"
                "plastrach",
                "https://www.kwestiasmaku.com/przepis/schab-w-sosie-wlasnym"

        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

    def light_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/koktajl-bananowy",
                "https://www.kwestiasmaku.com/przepis/salatka-z-truskawkami-"
                "feta-i-orzechami",
                "https://www.kwestiasmaku.com/przepis/warzywne-curry-z-cukinia"

        ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)

    def warm_btn(self):
        urls = [
                "https://www.kwestiasmaku.com/przepis/makaron-kokardki-z-"
                "boczkiem-i-smietanka",
                "https://www.kwestiasmaku.com/przepis/medaliony-warzywne",
                "https://www.kwestiasmaku.com/przepis/placki-z-batatow-na-"
                "slodko"
                ]
        url = random.choice(urls)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        skladniki = soup.find("div", class_="group-skladniki field-group-"
                                            "div")
        przygotowanie = soup.find("div", class_="field field-name-field-"
                                                "przygotowanie field-type-text-"
                                                "long field-label-above")
        self.recipe_text.delete("1.0", "end")
        scraped = ' '.join(element.get_text() for element in przygotowanie)
        self.recipe_text.insert("1.0", scraped)
        scraped_text = ' '.join(element.get_text() for element in skladniki)
        self.recipe_text.insert("1.0", scraped_text)


if __name__ == "__main__":
    app = App()
    app.mainloop()
