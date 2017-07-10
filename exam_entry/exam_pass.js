'use strict'

// Create a function that determines if a string is a palindrome

const palindrome = 'abBba';

const palindromeDetector = function isPalindrome(string) {
  let reverse = '';
  for (let i = (string.length - 1); i >= 0; i-= 1) {
    reverse += string[i];
  }
  if (reverse === string) {
    return 'This string is a palindrome.';
  }
  else {
    return 'This string is not a palindrome.';
  }
}

console.log(palindromeDetector(palindrome));
