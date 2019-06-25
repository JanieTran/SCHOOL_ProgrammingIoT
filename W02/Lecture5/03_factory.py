# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_factory.htm
class Button:
    def __init__(self):
        self.html = ""

    def get_html(self):
        return self.html


class Image(Button):
    def __init__(self):
        super().__init__()
        self.html = "<img></img>"


class Input(Button):
    def __init__(self):
        super().__init__()
        self.html = "<input></input>"


class Flash(Button):
    def __init__(self):
        super().__init__()
        self.html = "<obj></obj>"


class ButtonFactory:
    def create_button(self, type):
        target_class = type.capitalize()
        return globals()[target_class]()

# ==============================================================
# NOTE:
# The globals() function returns a dictionary
# containing the variables defined in the global namespace.
# ==============================================================


button_factory = ButtonFactory()
button = ["image", "input", "flash"]
for b in button:
    print(button_factory.create_button(b).get_html())


# ==============================================================
# NOTE:
# Flow: User -> Factory -> (Product, Product, Product, ...)
# ==============================================================
