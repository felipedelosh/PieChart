"""
FelipedelosH
"""
from tkinter import *

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.maxX = 720
        self.maxY = 480
        self.canvas = Canvas(self.screem, width=self.maxX, height=self.maxY, bg="snow")
        self.data = {"manzanas":20, "mangos":15, "bananas":45, "piñas": 3}
        self.lblTitle = Label(self.canvas, text="Pie Chart")
        self.vizualized()


    def vizualized(self):
        self.screem.geometry(str(self.maxX)+"x"+str(self.maxY))
        self.canvas.place(x=0, y=0)
        self.lblTitle.place(x=10, y=10)
        self.paintData()
        self.screem.mainloop()


    def paintData(self):
        # paint background circle
        _margin = self.maxX*0.04
        _circleTOP = self.maxY*0.9
        _textMarginX = self.maxX*0.72
        _textMarginY = self.maxY*0.2
        self.canvas.create_oval(_margin, _margin, _circleTOP, _circleTOP, fill="azure", width=5)
        dataToPaint = self._orderData(self.data)
        sumData = self._getSumData(self.data)
        
        # Paint pices of cake
        initAnge = 0
        endAngle = 0
        colorCounter = 1

        for i in dataToPaint:
            _name = i[0]
            _value = i[1]
            
            # Rule of 3
            endAngle = 360 * (_value/sumData)
 
            # Paint ARC
            self.canvas.create_arc(_margin, _margin, _circleTOP, _circleTOP, width=1, fill=self._getColor(colorCounter), start=initAnge, extent=endAngle)
            
            # Put Labels
            self.canvas.create_text(_textMarginX, _textMarginY + (20*colorCounter), fill=self._getColor(colorCounter), text=_name + " : " + str(_value))

            # Update Counters
            initAnge = initAnge + endAngle
            colorCounter = colorCounter + 1

    def _orderData(self, dic):
        """
        Order a dic = {"key":#, "key":#, "key":#, "key":#...}
        """
        all_data = []
        # Copy all data in vect of tuples
        for i in dic:
            all_data.append((i, dic[i]))

        # Bubble Short
        n = len(all_data)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if all_data[j][1] < all_data[j + 1][1]:
                    swapped = True
                    all_data[j], all_data[j+1] = all_data[j+1], all_data[j]

                
            if not swapped:
                return all_data

        return all_data
    

    def _getSumData(self, dic):
        aku = 0

        for i in dic:
            aku = aku + dic[i]

        return aku


    def _getColor(self, id):
        colors = {1: "cyan", 2: "orange", 3: "purple3", 4: "green yellow", 5: "maroon1"}
   
        key = id%len(colors)

        if key == 0:
            key = 1

        return colors[key]

s = Software()
