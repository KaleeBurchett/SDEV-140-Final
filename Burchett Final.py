
from breezypythongui import EasyFrame
from tkinter import PhotoImage, N, S, W, E
from tkinter.font import Font
import random


class BestLife(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Best Life Demo",
                           width=1500, height=1000)

        self.fall_romper = 0
        self.bw_dress = 0
        self.earth_dress = 0

        self.addLabel(text="Best Life ", row=0, column=1)

# Fall Romper

        romper_text = self.addLabel(text="Fall Romper",
                                    row=0, column=0,
                                    sticky=N + S + W + E)

        romper_label = self.addLabel(text="details:",
                                     row=1, column=0,
                                     sticky=N + S + W + E)

        romper_caption = self.addLabel(text="details:",
                                       row=2, column=0,
                                       sticky=N + S + W + E)

        self.image = PhotoImage(file="Fall Romper.png")
        romper_label["image"] = self.image

        font = Font(family="Verdana", size=20, slant="italic")
        romper_text["font"] = font
        romper_text["foreground"] = "blue"

        romper_add = self.addButton(text="Add to cart",
                                    row=3, column=0,
                                    command=self.cart_add)


#Earth Dress

        earth_text = self.addLabel(text="Earth Dress",
                                   row=0, column=1,
                                   sticky=N + S + W + E)

        earth_label = self.addLabel(text="details:",
                                    row=1, column=1,
                                    sticky=N + S + W + E)

        earth_caption = self.addLabel(text="details:",
                                      row=2, column=1,
                                      sticky=N + S + W + E)

        self.image = PhotoImage(file="Earth Dress.png")
        earth_label["image"] = self.image

        font = Font(family="Verdana", size=20, slant="italic")
        earth_text["font"] = font
        earth_text["foreground"] = "blue"

        earth_add = self.addButton(text="Add to cart",
                                   row=3, column=1,
                                   command=self.earth_add)



# Cart

        cart = self.addButton(text="Go to cart",
                              row=0, column=4,
                              command=self.cart)

    def cart_add(self):
        self.fall_romper = self.fall_romper + 1

    def earth_add(self):
        self.earth_dress = self.earth_dress + 1

    def cart(self):
        EasyFrame.__init__(self, title="Cart",
                           width=1500, height=1000)
        self.addLabel(text="Cart total: ", row=1, column=1)
        fall_price = 120
        bw_price = 150
        earth_price = 150
        fall_total = self.fall_romper * fall_price
        bw_total = self.bw_dress * bw_price
        earth_total = self.earth_dress * earth_price
        total = fall_total + bw_total + earth_total
        self.addLabel(text=total, row=1, column=2)


BestLife().mainloop()
