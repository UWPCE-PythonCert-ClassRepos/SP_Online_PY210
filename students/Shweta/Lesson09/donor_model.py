#!/usr/bin/env python

'''thankyou message for donation'''
mty_msg="\n".join(("Thankyou {}",
                   "for your generous donation of {:.2f}",))


ltr="\n".join(("", "Dear {},",
              "Thank you for your very kind donation of ${:.2f}.",
              "It will be put to very good use.",
              "           Sincerely,",
              "               -The Team"))

class Donor:

    def __init__(self,name,tamt):
        self.name = name
        self.tamt = tamt

    def add_donationamt(self,damt):
        self.tamt.append(damt)

    @property
    def tn_times(self):
        return len(self.tamt)
    
    @property 
    def total_sum(self):
        return sum(self.tamt)

    @property
    def avg(self):
        return (self.total_sum/self.tn_times)


    def ind_letter(self):
        indv_letter=ltr.format(self.name,self.total_sum)
        return indv_letter
    
    def formatting(self):
        self.frmt='{:20} ${:>20.2f}   {:18}   ${:20.2f}'.format(self.name,self.total_sum,self.tn_times,self.avg)
        return self.frmt

    def ind_thankyou(self):
        '''write thankyou letter for individual donor'''
        indv_letter = self.ind_letter()
        indv_name=self.name.replace(" " ,"_") + ".txt"
        with open(indv_name,'w') as infile:
             infile.write(indv_letter)


##########DonorCollection Class#################

class DonorCollection(object):
    '''for generating report about all the donors and send thankyou letter'''

    def __init__(self, *args):
        self.donors = {donor.name: donor for donor in args}

    def add_donor(self,dname,damt):
        ''' add any new donor and print thankyou message else add the amount 
            for already available donor'''
        if self.donors.get(dname) == None:
            self.donors[dname] = Donor(dname,[damt])
        else:
            self.donors[dname].add_donationamt(damt)
        return (mty_msg.format(dname,damt))

    def create_report(self):
        lines=[]
        for donor_all in self.donors.values():
            lines.append(donor_all.formatting())
        return lines

    def send_letter(self):
        for dname in self.donors.values():
            letter= dname.ind_thankyou()

        




        
