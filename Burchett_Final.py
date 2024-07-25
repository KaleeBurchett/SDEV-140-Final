
from breezypythongui import EasyFrame
from tkinter import PhotoImage, N, S, W, E
from tkinter.font import Font
import random


class BestLife(EasyFrame):

    # Main window displaying products.
    def __init__(self):
        EasyFrame.__init__(self, title="Best Life Demo",
                           width=1500, height=1000)

        # Loading in all images.
        self.image1 = PhotoImage(file="Fall Romper.png")
        self.image2 = PhotoImage(file="Earth Dress.png")
        self.image3 = PhotoImage(file="BW Dress.png")

        # Defining the number of times each product has been added to cart.
        self.fall_romper = 0
        self.bw_dress = 0
        self.earth_dress = 0

        # Fall Romper heading display.
        fall_text = self.addLabel(text="Fall Romper", row=0, column=0, columnspan=1, rowspan=1)

        # Adding canvas for product image and details.
        self.canvas1 = self.addCanvas(row=1, column=0, width=self.image1.width(), height=self.image1.height())
        self.canvas1.create_image(0, 0, anchor="nw", image=self.image1)
        self.canvas1.drawText(text="Price: $120", x=175, y=315)
        self.image = PhotoImage(file="Fall Romper.png")

        # Add Fall Romper to cart button.
        self.addButton(text="Add to cart",
                       row=2, column=0,
                       command=self.cart_add)

        # Variable to keep track of how many times product has been added. For displaying number.
        self.fall_romper_label = self.addLabel(text="0 added", row=2, column=0)

        # Font syntax for product name.
        font = Font(family="Verdana", size=20, slant="italic")
        fall_text["font"] = font
        fall_text["foreground"] = "blue"

        # Earth Dress heading display.
        earth_text = self.addLabel(text="Earth Dress", row=0, column=1)

        # Adding canvas for product image and details.
        self.canvas2 = self.addCanvas(row=1, column=1, width=self.image2.width(), height=self.image2.height())
        self.canvas2.create_image(0, 0, anchor="nw", image=self.image2)
        self.canvas2.drawText(text="Price: $150", x=175, y=315)
        self.image = PhotoImage(file="Earth Dress.png")

        # Add Earth Dress to cart button.
        self.addButton(text="Add to cart",
                       row=2, column=1,
                       command=self.earth_add)

        # Variable to keep track of how many times product has been added. For displaying number.
        self.earth_dress_label = self.addLabel(text="0 added", row=2, column=1)

        # Font syntax for product name.
        font = Font(family="Verdana", size=20, slant="italic")
        earth_text["font"] = font
        earth_text["foreground"] = "blue"

    # BW Dress heading display.
        bw_text = self.addLabel(text="Black and White Dress", row=3, column=0)

        # Adding canvas for product image and details.
        self.canvas3 = self.addCanvas(row=4, column=0, width=self.image3.width(), height=self.image3.height())
        self.canvas3.create_image(0, 0, anchor="nw", image=self.image3)
        self.canvas3.drawText(text="Price: $150", x=175, y=315)
        self.image = PhotoImage(file="BW Dress.png")

        # Add BW to cart button.
        self.addButton(text="Add to cart",
                       row=5, column=0,
                       command=self.bw_add)

        # Variable to keep track of how many times product has been added. For displaying number.
        self.bw_dress_label = self.addLabel(text="0 added", row=5, column=0)

        # Font syntax for product name.
        font = Font(family="Verdana", size=20, slant="italic")
        bw_text["font"] = font
        bw_text["foreground"] = "blue"

        # Go to Cart button.
        self.addButton(text="Go to cart",
                       row=0, column=4,
                       command=self.cart)

    # Calculates and displays number of times Fall Romper has been added to cart.
    def cart_add(self):
        self.fall_romper = self.fall_romper + 1
        self.fall_romper_label["text"] = f"{self.fall_romper} added"

    # Calculates and displays number of times Earth Dress has been added to cart.
    def earth_add(self):
        self.earth_dress = self.earth_dress + 1
        self.earth_dress_label["text"] = f"{self.earth_dress} added"

    # Calculates and displays number of times Black and White Dress has been added to cart.
    def bw_add(self):
        self.bw_dress = self.bw_dress + 1
        self.bw_dress_label["text"] = f"{self.bw_dress} added"

    # Cart window
    def cart(self):
        # Open new window, and close previous window.
        BestLife.destroy(self)

        class CartWindow(EasyFrame):
            # Define new window and title.
            def __init__(self, parent):
                EasyFrame.__init__(self, title="Cart",
                                   width=1500, height=1000)
                # Calling on the main window in order to use variables.
                self.parent = parent

                # Add labels for the total and details.
                self.cart_text = self.addLabel(text="Cart total: ", row=1, column=0)
                self.outputArea = self.addTextArea("Details:  \n"
                                                   f"Fall Rompers $120: {self.parent.fall_romper}\n"
                                                   f"Earth Dresses $150: {self.parent.earth_dress}\n"
                                                   f"Black and White Dresses $150: {self.parent.bw_dress}",
                                                   row=2, column=0,
                                                   columnspan=1, width=50, height=50)

                # Setting price for each product.
                fall_price = 120
                bw_price = 150
                earth_price = 150

                # Calculating total price per number of products.
                fall_total = self.parent.fall_romper * fall_price
                bw_total = self.parent.bw_dress * bw_price
                earth_total = self.parent.earth_dress * earth_price
                total = fall_total + bw_total + earth_total

                # Displaying total.
                self.cart_text["text"] = f"Cart total: ${total}"

                # Exit Button.
                self.addButton(text="Exit Cart",
                               row=0, column=4,
                               command=self.cart_close)

            # Close cart, open main window.
            def cart_close(self):
                CartWindow.destroy(self)
                BestLife().mainloop()

        CartWindow(self).mainloop()


BestLife().mainloop()
