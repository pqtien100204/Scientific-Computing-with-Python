
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size_dict = {"width": width, "height": height}

    def set_width(self, width):
        # self.size_dict["width"] = width
        self.size_dict.update({"width": width})

    def set_height(self, height):
        self.size_dict.update({"height": height})

    def get_area(self):
        area = self.size_dict["width"] * self.size_dict["height"]
        return area

    def get_perimeter(self):
        perimeter = (self.size_dict["width"] + self.size_dict["height"]) * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.size_dict["width"] ** 2 + self.size_dict["height"] ** 2) ** .5
        return diagonal

    def __str__(self):
        string_of_picture = f"Rectangle(width={self.size_dict['width']}, height={self.size_dict['height']})"
        return string_of_picture


    def get_picture(self):
        if self.size_dict["width"] > 50 or self.size_dict["height"] > 50:
            return "Too big for picture."
        else:
            picture = ""
            raw_picture = (self.size_dict["width"] * "*")
            times_of_iteration = 0
            while times_of_iteration < self.size_dict["height"]:
                picture += f"{raw_picture}\n"
                times_of_iteration += 1

            return picture
            
    def get_amount_inside(self, fitin_obj):
        width_fit = self.size_dict["width"] / fitin_obj.size_dict["width"]
        height_fit = self.size_dict["height"] / fitin_obj.size_dict["height"]
        amount_fit = height_fit * width_fit
        return int(amount_fit)

class Square(Rectangle):
    def __init__(self, width, height=False):
        super().__init__(width, height)
        self.size_dict = {"width": width, "height": width}

    def set_side(self, side):
        self.size_dict.update({"width": side, "height": side})

    def __str__(self):
        string_of_picture = f"Square(side={self.size_dict['height']})"
        return string_of_picture
# TESTING

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
rect.set_width(51)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(2)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))