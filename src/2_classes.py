
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



if __name__ == "__main__":

    cookie_one = Cookie('green')
    cookie_two = Cookie('blue')

    print(f'Cookie one color is: {cookie_one.get_color()}')
    print(f'Cookie two color is: {cookie_two.get_color()}')
    