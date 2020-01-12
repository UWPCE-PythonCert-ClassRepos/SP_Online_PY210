import mailroom4
import os
dummy_dictionary={"Test1":[1,2,3]}
def test_1():
    assert mailroom4.send_thanks_print("Santa",20)==print("\nThank you Santa for your donation of $20, your donations make the work of the 'American society for taking donations' possible.\n\n"
                                                "Sincearly,\n\n"
                                                "A low paid intern\n")

def test_2():
    assert mailroom4.send_thanks_list()==print('\n'.join(mailroom4.donor_list))

def test_3():
    assert mailroom4.send_thanks_add_donor("Santa",20)==mailroom4.donor_list["Santa"].append(20)

def test_4():
    mailroom4.send_thanks_update_donor("Santa2",20)
    assert mailroom4.donor_list["Santa2"]==[20]

def test_5():
    mailroom4.sorting_function({"Test1":[1,2,3],"Test2":[4,5,6]})==[[15,"Test2",3,5],[6,"Test1",3,2]]

def test_6():
    title=["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    listy=[6,"Test1",3,2]
    assert mailroom4.create_report({"Test1":[1,2,3]})==print(f"{title[0]:<20} | {title[1]:>10} | {title[2]:<} | {title[3]:<}"
                                                    "\n-------------------------------------------------------------"
                                                    f"\n {listy[1]:<21} ${listy[0]:>12.2f}{listy[2]:>11}  ${listy[3]:>12.2f}")

def test_7():
    assert mailroom4.mass_send_thanks_text("Test1",dummy_dictionary)==(f"\nThank you Test1 for your donation of ${6:.2f}, your donations make the work of the 'American society for taking donations' possible.\n\n"
        "Sincearly,\n\n"
        "A low paid intern\n")
def test_8():
    mailroom4.mass_send_thanks(dummy_dictionary)
    assert os.path.exists("Letters/Test1.txt")==True