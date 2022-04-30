class Cell:
    def __init__(self):
        self.status = 'Dead'

    def set_dead(self):
        self.status = 'Dead'

    def set_alive(self):
        self.status = 'Alive'

    def is_alive(self):
        if self.status == 'Alive':
            return True
        else:
            return False

    def get_print_character(self):
        if self.isalive() == True:
            return '■'
        else:
            return '□'