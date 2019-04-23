def palindromeCheck(string): #Begins function
  reversed = string[::-1] #string[::-1] Reverses string. Found at https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
  if string == reversed: #Begins if tag; checks to see if the original string is equal to itself backwards
    print(string + " is a palindrome!") #Output if it is a palindrome
  else: #Begins else tag, matches everything that is not a palindrome
    print(string + " is not a palindrome!") #Output if it is not a palindrome


my_function("palindrome") #Sample non-palindrome
my_function("racecar") #Sample palindrome
