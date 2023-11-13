import customtkinter
from customtkinter import *
import random
import pandas as pd


set_appearance_mode("Dark")
set_default_color_theme("blue")

appWidth, appHeight = 600, 800


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food App")
        self.geometry(f"{appWidth}x{appHeight}")

        # View Tab
        self.viewTab = CTkTabview(self)
        self.viewTab.grid(padx=140, pady=10, sticky="e")

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

        self.recipe_text = CTkTextbox(self, width=450, height=450)
        self.recipe_text.grid(row=6, column=0, columnspan=4, padx=20, pady=20,
                              sticky="nsew")

    def platki_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Płatki"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def jajka_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Jajka"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def jaglanka_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Jaglanka"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def placki_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Placki"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def kurczak_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Kurczak"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def losos_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Łosoś"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def beef_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Wołowina"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def pork_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Wieprzowina"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def light_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Na lekko"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)

    def warm_btn(self):
        df = pd.read_excel("Posiłki.xlsx")
        recipes = df["Na ciepło"].tolist()
        recipe = random.choice(recipes)
        self.recipe_text.delete("1.0", "end")
        self.recipe_text.insert("1.0", recipe)


if __name__ == "__main__":
    app = App()
    app.mainloop()
