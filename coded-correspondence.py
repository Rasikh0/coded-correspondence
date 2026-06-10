 importing string module
import string

# storing lower and upper case alphabets in variables
alph_lower = string.ascii_lowercase
alph_upper = string.ascii_uppercase
alph_both = alph_lower + alph_upper

def decoder_caesar(message: str, offset: int):
  return message.translate(str.maketrans(string.ascii_letters, string.ascii_lowercase[offset%26:] + string.ascii_lowercase[:offset%26] + string.ascii_uppercase[offset%26:] + string.ascii_uppercase[:offset%26]))

vishal_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(decoder_caesar(vishal_message, 10))

def coder_caesar(message: str, offset: int):
  return message.translate(str.maketrans(string.ascii_lowercase[offset%26:] + string.ascii_lowercase[:offset%26] + string.ascii_uppercase[offset%26:] + string.ascii_uppercase[:offset%26], string.ascii_letters))

fakhria_message = "Hi Vishal, this is Fakhria. Thanks for your message!"
coded_message = coder_caesar(fakhria_message, 10)
print(coded_message)
print(decoder_caesar(coded_message, 10))

vishal_message1 = decoder_caesar('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10)
print(vishal_message1)

vishal_message2 = decoder_caesar('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14)
print(vishal_message2)

for offset in range(1, 26):
  print("Offset = " + str(offset) + " gives: " + decoder_caesar("vhfinmxkl", offset))

print(decoder_caesar('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.', 7))

# Dictionary assigning number to letters in alphabet
alphabet_dict = {string.ascii_lowercase[i]:i for i in range(26)}

def decoder_vigenere(message: str, codeword: str):
    codeword.lower()
    codeword_index = 0   
    decoded_message = ''
    
    for char in message:
        if char in string.ascii_letters:
            decoded_message += coder_caesar(char, alphabet_dict[codeword[codeword_index]])
            
            if codeword_index == len(codeword) - 1:
                codeword_index = 0
            else:
                codeword_index +=1
        else:
            decoded_message += char
                     
    return decoded_message
  
# testing on example message
print(decoder_vigenere('eoxum ov hnh gvb', 'dog'))

print(decoder_vigenere('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends'))

def coder_vigenere(message: str, codeword: str):
    codeword = codeword.lower()
    codeword_index = 0   
    coded_message = ''
    
    for char in message:
        if char in string.ascii_letters:
            coded_message += decoder_caesar(char, alphabet_dict[codeword[codeword_index]])
            
            if codeword_index == len(codeword) - 1:
                codeword_index = 0
            else:
                codeword_index +=1
        else:
            coded_message += char
                     
    return coded_message

# testing by encoding first example
print(coder_vigenere("barry is the spy", "dog"))

# encoding my message
print(coder_vigenere("This was the most difficult project I had to complete on this platform yet.", "Difficult"))
