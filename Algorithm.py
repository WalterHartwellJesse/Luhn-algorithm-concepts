#Make a function 
def main():
    card_num = '4539-1488-0343-6467'
#You can translate your number , in by mean this will delete your excess words that is not in your number
    card_translation = str.maketrans({'-' : '' , ' ': ''})
#Simply like that. Now this is a variable for card translating. Add one more variable 
    card_num_translated = card_num.translate(card_translation)
#print(card_num_translated)
    is_valid = verify_card_num(card_num_translated)
    if is_valid:
        print('valido!')
    else:
        print('non posso!')
#Before make you make second function , make sure to store this variable.
def verify_card_num(card_num):
    sum_of_odd_digits = 0 # when you decrypt , it will keep decrypting , without adding any more numbers to it. Like 7 + 0 = 7 , then encrypt 7 + 7 = 14 without any stop force.
    card_num_reversed = card_num[::-1] # Keep in mind: [start:stop:step]
    odd_digits = card_num_reversed[::2] # Same for that. Keep praticing and youll get use to it
    for nums in odd_digits:
        sum_of_odd_digits+=int(nums) # This means: multiply every number. Could be odd , could be anything.
    sum_of_even_digits = 0 #similar to sum of odd ones # IMPORTANT : DONT PUT IT INTO A LOOP
    even_num = card_num_reversed[1::2] # Find the right num to encode # SECOND NOTES ! : DONT PUT IT ON A FUCKING LOOP
    for nums in even_num: # Now here we are starting with the even num sect.
        num = int(nums) *2
        if num >= 10:
        #print(num)
            num = (num // 10 ) + (num % 10)
        sum_of_even_digits += num
    total = sum_of_even_digits + sum_of_odd_digits
    print(total)
    return total % 10 == 0    


main() 