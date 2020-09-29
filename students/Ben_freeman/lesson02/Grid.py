def grid(gridsize=1,griddist=1): #gridsize is how many rows and columns this grid will have, while grid dist is how far apart each \"+\" will be from each other\n",
    plus="+"
    minus=" -"
    space="  "
    orthminus= "|"
    for i in range (0,gridsize+1):                        #prints multiple "vertical blocks"
        if i==gridsize:
            for k in range (0,gridsize+1):              #how we make sure the next column after a + is written
                        if k==gridsize:                 # makes sure we end with a plus and not a +-----
                            print(plus)
                        else:    
                            print(plus+minus*griddist,end=" ")
        else:
            for j in range (0,griddist+1):
                if j==0:                                #prints the +----... rows uptil the next +
                    for k in range (0,gridsize+1):      #how we make sure the next column after a + is written
                        if k==gridsize:                 # makes sure we end with a plus and not a +-----
                            print(plus)
                        else:    
                            print(plus+minus*griddist,end=" ")
                else:                                  #prints the | lines
                    for k in range (0,gridsize+1):
                        if k==gridsize:
                            print(orthminus)
                        else:
                            print(orthminus+space*griddist,end=" ")