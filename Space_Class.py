class Space:
    def __init__(self,space = None, dtile = None):
        self.space = space
        self.dtile = dtile
    def get_space(self):
        return self.space
    def change_space(self, new_space):
        self.space = new_space        
    def get_dtile(self):
        return self.dtile
    def change_dtile(self, new_dtile):
        self.dtile = new_dtile