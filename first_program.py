class my_first_class:
    def __init__(self, print_this):
        pass

    def print_element(self):
        print(self.print_this)
        


obj = my_first_class('hello')
obj.print_element()