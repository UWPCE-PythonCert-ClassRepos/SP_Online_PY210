example = (2, 123.4567, 10000, 12345.67)
f_string = f"file_{example[0]:03} : {example[1]:9.2f}, {example[2]:.2e}, {example[3]:.2e}"
print(f_string)
