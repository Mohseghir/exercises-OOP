"""
class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
rectangle = Rectangle(5,3)


    def calculate_area(self):
        return self.width * self.height
"""


class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def cut_in_part(self):
        print("le gateau est coupé en 4")


cake = Cake("chocolate")
print(cake.flavor)
cake.cut_in_part()
cake.flavor = "banana"
print(cake.flavor)
