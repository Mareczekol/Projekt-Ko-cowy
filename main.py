import customtkinter
from customtkinter import *

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
        self.viewTab.pack(padx=20, pady=20)

        self.viewTab.add("Śniadanie")
        self.viewTab.add("Obiad")
        self.viewTab.add("Kolacja")

        # Tab. 1 - śniadanie
        self.platki_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                    text="Płatki")
        self.platki_btn.grid(padx=80, pady=20, sticky="sw")

        self.jajka_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                   text="Jajka")
        self.jajka_btn.grid(padx=80, pady=25, sticky="sw")

        self.jaglanka_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                      text="Jaglanka")
        self.jaglanka_btn.grid(padx=80, pady=30, sticky="sw")

        self.placki_btn = CTkButton(self.viewTab.tab("Śniadanie"),
                                    text="Placki")
        self.placki_btn.grid(padx=80, pady=35, sticky="sw")

        # Tab 2 - obiad
        self.losos_btn = CTkButton(self.viewTab.tab("Obiad"),
                                   text="Łosoś")
        self.losos_btn.grid(padx=80, pady=20, sticky="sw")

        self.kurczak_btn = CTkButton(self.viewTab.tab("Obiad"),
                                     text="Kurczak")
        self.kurczak_btn.grid(padx=80, pady=25, sticky="sw")

        self.beef_btn = CTkButton(self.viewTab.tab("Obiad"),
                                  text="Wołowina")
        self.beef_btn.grid(padx=80, pady=30, sticky="sw")

        self.pork_btn = CTkButton(self.viewTab.tab("Obiad"),
                                  text="Wieprzowina")
        self.pork_btn.grid(padx=80, pady=35, sticky="sw")

        # Tab. 3 - kolacja
        self.light_btn = CTkButton(self.viewTab.tab("Kolacja"),
                                   text="Lekka kolacja")
        self.light_btn.grid(padx=80, pady=20, sticky="sw")

        self.warm_btn = CTkButton(self.viewTab.tab("Kolacja"),
                                  text="Kolacja na ciepło")
        self.warm_btn.grid(padx=80, pady=25, sticky="sw")


if __name__ == "__main__":
    app = App()
    app.mainloop()
