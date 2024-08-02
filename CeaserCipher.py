import string
def getInputFile():
    '''check if the file extension is valid and returns the file(string)'''
    if True:
        filename = input('Enter the input filename: ')   #gets input from user
        txt_word = '.txt'
        if txt_word in filename.lower() and filename[-4:].lower() == '.txt': # checks if filename ends with .txt
            return filename
        else:
            while True:
                filename = input('Invalid filename extension. Please re-enter the input filename: ')  
                if txt_word in filename.lower() and filename[-4:].lower() == '.txt':
                    return filename
                else:
                    None



def decrypt(filename: str):
    """
    Reads file and decrypts it  and returns the decrypted word
    """

    # reading the file, striping the newline and accessing the key and message
    file1 = open(filename, 'r')
    file = file1.readlines()
    key = int(file[0].strip())
    text_list = file[1:]
    text_list2 =[]
    for i in text_list:
        i.strip()
        text_list2.append(i)
    text = ''.join(text_list2)
    
    capital_letters = string.ascii_uppercase  #shows the uppercase alphabet letters
    small_letters = string.ascii_lowercase  #shows the lowercase alphabet letters
   
    final_word = [] # empty list to append all the decrepyted letters
    
    for letter in text:  #accesing letter in the inputed text
        if letter in capital_letters:  # for letters that are capital letters omly
            m = (((ord(letter)-65-key)%26)+65)   #formula incase the word lies between a and c and tells to shift by 3
            ascii_to_letter= chr(m)   #chr converts the ascii numbers to their individual letter form
            final_word.append(ascii_to_letter)  #all the letters are appended into the empty final_word list
        elif letter in small_letters:  # for letters that are lowercase letter only
            m = (((ord(letter)-97-key)%26)+97)  #formula incase the word lies between a and c and tells to shift by 3
            ascii_to_letter = chr(m) #chr converts the ascii numbers to their individual letter form
            final_word.append(ascii_to_letter) #all the letters are appended into the empty final_word list
        else:
            final_word.append(letter)  # to append the spaces ie letters that are neither small or capital
    final_word.append(' ')
    string_decrypted_word = ''.join(final_word).lower()   #converts the list into a string using empty string
    return string_decrypted_word
    
def main():
    '''calls all functions'''
    filehahaha = getInputFile()
    print('The decrypted message is: ')
    print(decrypt(filehahaha))
    # help(getInputFile)
    # help(decrypt)

if __name__ == "__main__":
    main() #call main
