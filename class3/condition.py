#is: comparing resources
NUMBER1=10
NUMBER2=10
NUMBER1 is NUMBER2
# if NUMBER1 is NUMBER2:
#     print("they are equal")
# else:
#     print("they are not equal")
# if NUMBER1 is not NUMBER2:
#     print('they are not equal')
# else:
#     print('they are equal')
HIDDEN_FRUIT= "kiwi"
FRUIT_LIST1=("apple","pear","banana")
FRUIT_LIST2=("mango","melon","cherry")
FRUIT_LIST3=("peach","apricot","kiwi")
if HIDDEN_FRUIT in FRUIT_LIST1:
    print('Hidden fruit is in List1')
elif HIDDEN_FRUIT in FRUIT_LIST2:
    print('Hidden fruit is in List2')
elif HIDDEN_FRUIT in FRUIT_LIST3:
    print('Hidden fruit is in List3')
else:
    print ('Hidden fruit is not found')