#!/bin/sh
function palindromeCheck {
  local reverse=$(rev<<<$1) #Reverses original string. Found at https://www.cyberciti.biz/faq/how-to-reverse-string-in-unix-shell-script/
  local string=$1
  if [[ $string == $reverse ]]; then
    echo "$string is a palindrome!"
  else
    echo "$string is not a palindrome!"
  fi
}

palindromeCheck "test"
palindromeCheck "racecar"
