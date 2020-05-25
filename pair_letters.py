def solution(s):
    stl = list(s)
    counter = 0
    if len(s) % 2 == 0:
        st = []
        for word in stl:
            if counter%2 == 0:
                my_string = word+stl[counter+1]
                st.append(my_string)
                counter +=1
            else:
                counter +=1
        return st
    else:
        st = []
        for word in stl:
            if counter % 2 == 0 and counter != len(stl)-1:
                my_string = word+stl[counter+1]
                st.append(my_string)
                counter +=1
            elif counter == len(stl)-1:
                my_string = word+"_"
                st.append(my_string)
                counter +=1
            else:
                counter +=1
        return st


# vi na net

import re

def solution(s):
    return re.findall(".{2}", s + "_")
