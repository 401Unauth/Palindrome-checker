def palindromeCheck(string):
  reversed = string[::-1] #string[::-1] Reverses string. Found at https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
  if string == reversed:
    print(string + " is a palindrome!") #Output if it is a palindrome
  else:
    print(string + " is not a palindrome!") #Output if it is not a palindrome

palindromeCheck("palindrome") #Sample non-palindrome
palindromeCheck("racecar") #Sample palindrome
