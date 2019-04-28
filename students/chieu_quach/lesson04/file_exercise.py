# Author     : Chieu Quach
# Assignment : Lesson 04
# Exercise   : File Exercise (Path and File Processing)
#            : Reads input file "students.txt" and prints out
#            : the report in format form.
# prints the full path for all files in current directory one per line
# wb - means writing

def file_processing():

    
    
    # prints full path for all files in current directory
    
   for root, dirs, files in os.walk("."):

       for z in files:
           p = os.path.join(root,z)
        #  print (p)
           print (os.path.abspath(p))

   print("\n")
   # copy text file from file to filez
   # "wb" is used here to apply for writing out file to both text or binary file
   
   file = open("students.txt", "rb")
   file_cpy = file.read()
   filez = open("cpy_students.txt", "wb")
   filez.write(file_cpy)
 
    #copy binary file from file to filez
    #file2 = open("cpy_file.txt", "wb")
   file = open("sceneryz.jpg", "rb")
   file_cpy = file.read()
   filez = open("cpy_sceneryz.jpg", "wb")
   filez.write(file_cpy)
  #  for v in line:
  #      part = v.split()
  # copy file from file1 into file2   
   file.close()
   filez.close()

    
def reading_parsing():
    
   file1 = open("students.txt", "r")
   line  = file1.readlines()
   file_name = {}
   list_name = set()
   languages = set()
   list_languages = set()
   for z in line:
       parts = z.split()
        
       parts = parts[2:]
        #first_part = parts[:1]
        #print ("parts ", parts)
        
       if len(parts) > 1:
           for o in parts:
            # print ("o ", o)
            # check to make sure no duplicate item is added
             # to set list_name
               if not z in list_name:                
                   list_name.add(o)
   
    
    #print ("list_name ", list_name)
   for z in list_name:
       segment = z.split()
        #print ("segment ", segment[0])
       name_chk = segment[0]
        
       if name_chk[0].isupper():
           # print ("upper name ", segment)
           continue
       else:
           languages.add(name_chk)
        #print ("languages ", languages)
           chk_comma = segment[-1]
        
       
   list_languages = " List of All Languages "
   print (" {:^30}".format(list_languages))  
   print (" --------------------------------------------")
   for v in languages:
       name_languages = v.split()
       show_languages = name_languages[0]
       chk_comma = show_languages[-1:]
       if show_languages[-1:] == ",":
           show_languages = show_languages[:-1] 
          
          #print (show_languages, "\t", show_languages[:-1])
       else:
           show_languages =  show_languages
       print (show_languages)
       
   print("\n")     
   file1.close()
def file_format():

   file1 = open("students.txt", "r")
   line  = file1.readlines()
   name_header      = " Full Name      |"  
   nickname_header  = " Nickname     |"
   languages_header = " Languages                       |"
   
   print ("{:15}  {:15}  {:>34}"
   .format(name_header, nickname_header, languages_header))
   print (" ------------------------------------------------------------------------")
    
   for o in line:
        full_parts = o.split()
        
        len_parts = len(full_parts)
        #print ("len_parts ", len_parts)
        name = full_parts[:2]
        languages = full_parts[2:]
        #print ("full_parts ", full_parts)
       # print ("name ", name)
       # print ("languages ", languages)
        #print ("languages[0]", languages[:1])
        if len_parts > 2:
            nickname = languages[0]
          #  print ("nickname ", nickname)
          #  print ("nickname[0] ", nickname[0])
            if nickname[0].isupper():
                nickname = languages[:1]
               
                languages = languages[1:]

                # use .join(map to remove brackets and commas from list file
                nuname    =   (" ".join(map(str, name)))
                nulanguage= (" ".join(map(str, languages)))
                nickname  = (" ".join(map(str, nickname)))
                #print ("{:<19} {:<15} {:<24}".format{nuname, nickname, nulanguage))
                print ("{:<19} {:<15} {:<21} ".format(nuname, str(nickname), nulanguage))
                
            else:
                nuname    =   (" ".join(map(str, name)))
                nulanguage= (" ".join(map(str, languages)))
                print ("{:<19}  {:>51} ".format(nuname, nulanguage))

        elif len_parts == 2:
                nuname    =   (" ".join(map(str, name)))
                print ("{:<19} ".format(nuname))
                
   file1.close()     


# Main function
if __name__ == "__main__": 

   import os
   file_processing()
   reading_parsing()
   file_format()
