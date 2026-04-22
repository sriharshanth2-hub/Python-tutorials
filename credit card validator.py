sum_odd_digits = 0
sum_even_digits = 0
card_no = input("Enter a card number : ")
card_no = card_no.replace("-","")
card_no = card_no.replace(" ","")
card_no = card_no[::-1]

for i in card_no[::2] :
    sum_odd_digits += int(i)

for x in card_no[1::2] :
    x = int(x)*2
    if x >= 10 :
        sum_even_digits += (x%10)+1
    else :
        sum_even_digits += x

total = sum_even_digits + sum_odd_digits

if total % 10 == 0 :
    print("valid")
else :
    print("invalid")

