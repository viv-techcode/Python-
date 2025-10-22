

#  Convert digits/numbers to words (small example 0-999)

print(" Number to words (0-999 simple)")
n = 345
print("Number:", n)
ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
def num_to_words(x):
    if x < 10:
        return ones[x]
    elif x < 20:
        return teens[x-10]
    elif x < 100:
        if x%10 == 0:
            return tens[x//10]
        else:
            return tens[x//10] + "-" + ones[x%10]
    elif x < 1000:
        if x%100 == 0:
            return ones[x//100] + " hundred"
        else:
            return ones[x//100] + " hundred and " + num_to_words(x%100)
    else:
        return "Number out of range for this simple converter"
print("In words:", num_to_words(n))


# Output: 123 → “One Hundred Twenty Three”