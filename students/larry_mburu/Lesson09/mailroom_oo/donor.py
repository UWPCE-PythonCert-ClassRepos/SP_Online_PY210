class Donor: 
    """
    Class represents donor information and donation history
    """
    def __init__(self): 
        self._fname = None
        self._lname = None
        self.donation_history = []

    @property 
    def fname(self): 
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value.capitalize()
    
    @property
    def lname(self): 
        return self._lname
    
    @lname.setter 
    def lname(self, value):
        self._lname = value.capitalize()
    
    def add_donation(self, amount): 
        """
        Function adds donation amount to donation history 
        param: amount: amount donated 

        raises an ValueError exception if amount argument
        is a string, that's not numeric

        return: None
        """
        try: 
            self.donation_history.append(float(amount)) #float() in case string is given
        except ValueError:
            raise ValueError('Only dollar amounts allowed!')
    
    def letter(self): 
        """
        Function returns a formatted string, for content to be
        written to each letter file

        return: String: Formatted
        """
        # -1, the latest donation in donation_history list
        letter_template = f"""Dear {self._fname + ' ' + self._lname},
        Thank you for your kind donation of ${self.donation_history[-1]}.

        It will be put to very good use.

        Sincerely,

        - The Cloud Squad"""

        return letter_template
    
    def thank_you_email(self):
        """
        Function composes and email to a donor for their generous donation. 
        assumes that the last donation in donation_history[] is the 
        most recent donation

        return: String: formatted email string. 
        """
        return f"Thank you {self._fname} {self._lname} for your generous donation of ${(self.donation_history[-1]):.2f} dollars"
        