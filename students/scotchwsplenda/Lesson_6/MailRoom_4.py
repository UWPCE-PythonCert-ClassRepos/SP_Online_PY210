
from operator import itemgetter
import sys


# donors
donators = {"Gordian": [30.0, 45.0], "Tiberius": [60.0],
            "Maximus": [65.0, 12.0], "Tacitus": [33.0, 22.0, 25.00],
            "Commodus": [43.0, 11.0]}


def mainy():
    print('''
  Welcome to the MAILROOM main menu
  Please choose from below options:
  1 - Initiate Grovel Sequence
  2 - Data Metrics 3000
  3 - Quit
  4 - Send thank you notes to all donors
              ''')
    while True:
        try:
            choice = int(input('Main Indicate your choice: '))
            swit_dic = {1: send_note, 2: data_metrics,
                        3: exit_program, 4: mass_mail}
            swit_dic[choice]()
        except KeyError:
            print('You have entered a non-choice'
                  ' , please get your shit together')
        except ValueError:
            print('You have entered a non-number'
                  ' , please get your shit together')
            continue


# Option 1: Content of Thank you note
def send_note():
    print('''
Please select from the below Thank You Note options:
1 - Print list of extant donors
2 - Enter donor name and donation
3 - Exit Program
    ''')
    while True:
        try:
            respondy = int(input("send_note: Indicate your choice:"))
            if respondy == 1:
                print_donors()
                continue
            if respondy == 2:
                try:
                    donor_inp = input("Input donor: ")
                    if donor_inp in donators.keys():
                        don_amount = input("That's a known donor,"
                                           " input donation amount: ")
                    else:
                        don_amount = input(f"{donor_inp}'s an unknown donor,"
                                           " input donation amount: ")
                    don_amount = float(don_amount)
                    update_dons(donor_inp, don_amount)
                    send_thanks(donor_inp, don_amount)
                    continue
                except ValueError:
                    print('You have entered a non-number'
                          ' , for the donation amount start over')
            if respondy == 3:
                mainy()
            if respondy > 3:
                print('You have entered a non-choice'
                      ' , please get your shit together')
                continue
            if respondy < 1:
                print('You have entered a non-choice'
                      ' , please get your shit together')
                continue
        except ValueError:
            print('You have entered a non-number'
                  ' , please get your shit together')
            continue
# break - exits program entirely
# continue - stays in send_note() [have to quit terminal]
# exit() - exits program entirely
# False - stays in send_note() [have to quit terminal]
# done - stays in send_note() [have to quit terminal]
# return - exits program entirely
# True - stays in send_note() [have to quit terminal]


# option 1d: update donor database
def update_dons(donor_inp, don_amount):
    donators.update({donor_inp: [don_amount]})
    return {donor_inp: [don_amount]}


# Option 1a: sub-function
def send_thanks(donor_inp, don_amount):
    thanks = (f'Wow {donor_inp}, only ${don_amount}?'
              ' Give til it hurts you capitalist swine')
    print(thanks)
    return thanks


# option 1c: print list:
def print_donors():
    butt = list()
    for k in donators:
        butt.append(k)
    print(butt)
    return butt


# Option 2: create report
def data_metrics():
    total_giv = [(name, sum(donat), len(donat),
                 round((sum(donat)/len(donat)), 1))
                 for (name, donat) in donators.items()]
    ranked_d = sorted(total_giv, key=itemgetter(1), reverse=True)
    print('Name'+'-'*30+'Sum'+'-'*28+'Count'+'-'*30+'Avg')
    for a, b, c, d in ranked_d:
        print(f'{a:<33}{b:<33}{c:<33}{d:<33}')
    return ranked_d

# https://www.youtube.com/watch?v=AhSvKGTh28Q


# Option 3: get out of this program
def exit_program():
    print("Bye!")
    sys.exit()  # THIS IS TO EXIT THE PROGRAM AND START OVER


# Option 4: send a note to all donoators
def mass_mail():
    for key, value in donators.items():
        with open(f'{key}.txt', 'w') as f:
            sumy = str(sum(value))
            f.write(f'Thanks {key} for donating ${sumy}.'
                    ' Your mother would be so proud.')


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically
    # if this module is imported
    mainy()
