# def reverse_number(number):
#     number_copy = number
#     reversed_number = 0

#     while number_copy > 0:
#         digit = number_copy % 10
#         reversed_number = (reversed_number * 10) + digit
#         number_copy = number_copy // 10

#     return reversed_number

# number = int(input("Entrez un nombre : "))
# reversed = reverse_number(number)
# print("Le nombre inversé est :", reversed)
strf="12213424235523"
str_rev = strf[::-1]
print(str_rev)
