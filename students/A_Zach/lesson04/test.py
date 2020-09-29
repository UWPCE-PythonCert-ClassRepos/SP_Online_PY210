#Create a database
Jen = ['Jenny Jones', [272.00, 8700.11, 4.22]]
Ste = ['Steve Martin', [85000.00, 12345.67, 54321.99]]
Che = ['Cher', [0.01, 0.01]]
Aba = ['Aba Ababa', [101.01, 10101.01, 1100.10]]
Wan = ['Wan Do Nation', [1.00]]   
#Combine donors into a database
Database = [Jen, Ste, Che, Aba, Wan]
#create a dictionary of donor information
Donor_dict = {}
for name in Database:
    Donor_dict[name[0]] = name[1]
print(Donor_dict)

aves = []
for name in Donor_dict:
    aves.append(sum(Donor_dict[name])/len(Donor_dict[name]))
print(aves)

def ave_don(dict):
    aves = []
    for name in dict:
      aves.append(sum(dict[name])/len(dict[name])
    return
    
print(ave_don(Donor_dict))