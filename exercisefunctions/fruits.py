# Writing the initial class
class fruit:
    def __init__(self, name, color, sizecategory):
        self.name = name
        self.color = color
        self.sizecategory = sizecategory
        self.percentage = 100

    def get_fruit_name(self):
        return self.name

    def get_fruit_color(self):
        return self.color

    def get_fruit_size(self):
        return self.sizecategory

    def bite(self):
        self.percentage -= 10

    def get_balance(self):
        return self.percentage
