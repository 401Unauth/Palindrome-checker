function checkIfPalindrome(string) {
  var reversed = string.split("").reverse().join(""); // Reverses the string - found on https://medium.freecodecamp.org/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb
  if ( string == reversed ) {
    // Runs this if the input is a palindrome
    console.log("\"" + string + "\"" + ' is a palindrome!');
  }
  else {
    // Runs this if the input is not a palindrome
    console.log("\"" + string + "\"" + ' is not a palindrome!');
  }
}

checkIfPalindrome("Racecar"); //Palindrome
checkIfPalindrome("Palindrome"); //Not a palindrome
