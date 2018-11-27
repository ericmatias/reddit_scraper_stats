


class Dog:

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name
        self.collar_color = 'red'
        self.__has_kids = True

    @property
    def get_doggo_name(self):
        return '{} of {}'.format(self.name, self.breed)

    def __can_bark(self):
        if isinstance(self, Dog):
            return True
        else:
            return False

    def bark(self):
        if self.__can_bark():
            print('Bark! Bark! Bark!')


