fav_yt = []

fav_yt.append("idk")
fav_yt.append("idk2")
fav_yt.append("idk3")
fav_yt.append("idk4")
fav_yt.append("idk5")

for yt in fav_yt:
    print(yt)

print(fav_yt[-1])

fav_yt[1] = "i still dont know2" 
print(fav_yt)

fav_yt.sort()
print(fav_yt)
print(len(fav_yt))

test_list = [x for x in range(1,60) if x % 2 == 0]
print(test_list)

addition_list = [1,2,3,4,5]
newaddition_list = [x + 10 for x in addition_list]
print(newaddition_list)

ages_list = [17,20,46,13,29,30,15,10]
under20 = [x for x in ages_list if x <20]
print(under20)




while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        print("Goodbye!")
        break  # exit the loop
    else:
        print("You typed:", text)







#