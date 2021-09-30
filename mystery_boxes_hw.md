def mystery_box1(string, lower):

    if lower:
        return string.lower()[::-1]
    else:
        return string[::-1]
        


print(mystery_box1("Hello", False))




def mystery_box2(email):

    name = ""
    name_list = email.split("@")[0].split(".")
    for i in name_list:
        name += i[0].upper() + i[1:] + " "
    platform = email.split("@")[1]
    return name + " " + platform


print(mystery_box2("john.doe@gmail.com"))




def mystery_box3(num_list):

    first_num = num_list[0]
    i = 1
    while i:
        prod = first_num * i
        if prod % num_list[1] == 0 and prod % num_list[2] == 0:
            return prod
        i += 1


print(mystery_box3([18, 4, 7]))




def mystery_box4(score_list):

    average = 0
    for i in score_list:
        if i > 7:
            score_list.remove(i)
    for j in score_list:
        average += j/len(score_list)
    output = str(average) + " " + str(score_list)
    return output


print(mystery_box4([5, 6, 3, 8, 1, 7, 9]))
