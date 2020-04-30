"""
Program: colorpicker.py
Alexa 4/29/2020

Python program that uses a GUI and a dialog to present a color wheel from which the user can choose a color, and then display it in a canvas widget.
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
    #displays the results of picking a color

    def __init__(self):
        #sets up window and widgets
        EasyFrame.__init__(self, title="Color Chooser Demo")

        #labels and output field
        self.addLabel('R', row=0, column=0)
        self.addLabel('G', row=1, column=0)
        self.addLabel('B', row=2, column=0)
        self.addLabel('Color', row=3, column=0)
        self.r = self.addIntegerField(value=0, row=0, column=1)
        self.g = self.addIntegerField(value=0, row=1, column=1)
        self.b = self.addIntegerField(value=0, row=2, column=1)
        self.hex = self.addTextField(text="#000000", row=3, column=1, width=10)

        #canvas with an initial black background
        self.canvas = self.addCanvas(row=0, column=2, rowspan=4, width=50, background="#000000")

        #command button
        self.addButton(text="Choose color", row = 4, column=0, columnspan=3, command=self.chooseColor)

    #event handling method
    def chooseColor(self):
        #pops up a color chooser and outputs the results
        colorTuple = tkinter.colorchooser.askcolor()
        if not colorTuple[0]: return
        ((r, g, b), hexString) = colorTuple
        self.r.setNumber(int(r))
        self.g.setNumber(int(g))
        self.b.setNumber(int(b))
        self.hex.setText(hexString)
        self.canvas["background"] = hexString

def main():
    ColorPicker().mainloop()

main()

