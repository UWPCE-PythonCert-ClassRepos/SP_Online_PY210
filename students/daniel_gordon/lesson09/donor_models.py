class Donor():
    """Contains a donors name and a list of donations"""
    def __init__(self, name, donations=[]):
        names = name.split(' ')
        self.first_name = names[0]
        if(len(names) == 1):
            self.last_name = ""
        else:
            self.last_name = names[-1]
    
    @property
    def name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name