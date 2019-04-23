<?php
function palindromeCheck($string) {
  $string = htmlspecialchars($string); // Sanitizes input
  $reversed = htmlspecialchars(strrev($string)); //Sanitizes input and reverses original string
  if ($string == $reversed) { //https://www.geeksforgeeks.org/php-reverse-string/
    print nl2br("$string is a palindrome!\n");
  }
  else {
    print nl2br("$string is not a palindrome!\n");
  }
}
palindromeCheck("racecar");
palindromeCheck("palindrome");
 ?>
