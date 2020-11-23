#creating a script for 4 basic Python errors
#NameError, TypeError, SyntaxError, AttributeError

def error_one():
    NBA_teams = ["Heat","Lakers","Celtics","Nuggets"]

    print (NBA_team);

error_one()

def error_two():
    NBA_teams = ["Bulls","Warriors","Pelicans"]
    number = 1

    result = number + NBA_teams
    print (result);

error_two()

def error_three():
    x = int(input('Enter a number:'))

    whilee x%2 == 0:
        print ('You have entered an even number')
        break
    else:
        print('You have entered an odd number')

error_three()

def error_four():
    x = 100
    x.append(5)

error_four()

