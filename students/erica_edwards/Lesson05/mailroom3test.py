
donors = {'Sandy Pie' : [75],
          'Judy Smith': [75, 100, 1000],
          'Mike Jones': [75, 1000],
          'Joe Smith' : [75, 100, 2000],
          'Kelly Blue': [75, 150, 275]}

named_list = [{"donor_name": n, "total": sum(d)} for n, d in donors.items()]

print(named_list)