# sorting algorithm

# start by creating a bunch of lists defined by letters and digits
zero=[]; one=[]; two=[]; three=[]; four=[]; five=[]; six=[]; seven=[]; eight=[]; nine=[]
a=[]; b=[]; c=[]; d=[]; e=[]; f=[]; g=[]; h=[]; i=[]; j=[]; k=[]; l=[]; m=[]; n=[]; o=[]; p=[]; q=[]; r=[]; s=[]; t=[]; u=[]; v=[]; w=[]; x=[]; y=[]; z=[]

# set add_new = True
add_new = True

# create a list to add new items
item_list = []

# start the process of adding new items
print('\nEnter an item (all lowercase) to be sorted')
print("Enter '_done' when finished\n")

while add_new == True:
    new_item = input('> ').lower()

    match new_item:
        case '_done':
            add_new = False
        case _:
            item_list.append(new_item)

# now, start the process of sorting

# for loop runs through each phrase added and appends them to a list corresponding with the letter at word[1]
for word in item_list:
    match word[0]:
        case '0':
            zero.append(word)
        case '1':
            one.append(word)
        case '2':
            two.append(word)
        case '3':
            three.append(word)
        case '4':
            four.append(word)
        case '5':
            five.append(word)
        case '6':
            six.append(word)
        case '7':
            seven.append(word)
        case '8':
            eight.append(word)
        case '9':
            nine.append(word)
        case 'a':
            a.append(word)
        case 'b':
            b.append(word)
        case 'c':
            c.append(word)
        case 'd':
            d.append(word)
        case 'e':
            e.append(word)
        case 'f':
            f.append(word)
        case 'g':
            g.append(word)
        case 'h':
            h.append(word)
        case 'i':
            i.append(word)
        case 'j':
            j.append(word)
        case 'k':
            k.append(word)
        case 'l':
            l.append(word)
        case 'm':
            m.append(word)
        case 'n':
            n.append(word)
        case 'o':
            o.append(word)
        case 'p':
            p.append(word)
        case 'q':
            q.append(word)
        case 'r':
            r.append(word)
        case 's':
            s.append(word)
        case 't':
            t.append(word)
        case 'u':
            u.append(word)
        case 'v':
            v.append(word)
        case 'w':
            w.append(word)
        case 'x':
            x.append(word)
        case 'y':
            y.append(word)
        case 'z':
            z.append(word)

# after the for loop, the rough sort adds all of the lists in order
# starting with 0-9 then a-z
rough_sort = [zero + one + two + three + four + five + six + seven + eight + nine + a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z]
