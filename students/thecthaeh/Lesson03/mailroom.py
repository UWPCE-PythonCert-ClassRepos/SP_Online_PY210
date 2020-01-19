donor_info = [('Frank Miller', [320.00, 100.00, 570.50]), ('Tess Baker', [1000.00, 540.00]), 
('Grant Hugh', [5000.00]), ('Sarah Piper', [40.00]), ('Jim Newton', [1350.00, 1500.00, 5.50])]

actions = input("Choose one of the following options: \n1. Send a Thank You \n2. Create a Report \n3. Quit \n>>> ")

while actions != '3':
    if actions == '1':
        full_name = input("Enter the donor's full name.\n>> ")
        if full_name == 'list':
            for donor in donor_info:
                print(donor[0])
            full_name = input("\nEnter the donor's full name.\n>> ")
            donor_info.append((full_name, []))
        elif full_name not in donor_info:
            donor_info.append((full_name, []))
        
        donate_amt = input("Enter the donation amount.\n>> $")
        donate_amt = float(donate_amt)

        for donor in donor_info:
            if donor[0] == full_name:
                donor[1].append(donate_amt)
        print(donor_info)
        
        print(f"Thank you, {full_name}, for your generous donation.")
        
        actions = input("Choose one of the following options: \n1. Send a Thank You \n2. Create a Report \n3. Quit \n>>> ")
        
    elif actions == '2':
        header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
        
        top_row = "{:30} |{:>20} |{:>15} |{:>20}".format(*header[:])
        print(top_row)
        print('-' * len(top_row))

        for donor in donor_info:
            report = [donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])]
            print("{:30}  ${:>19.2f}  {:>15}  ${:>19.2f}".format(*report[:]))
        
        actions = input("Choose one of the following options: \n1. Send a Thank You \n2. Create a Report \n3. Quit \n>>> ")