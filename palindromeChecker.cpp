// palindrome checker - checks if input is a palindrome

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>

using namespace std;

// Prototype declaration
char palindromeChecker(char String[]);

int main(int nNumberOfArgs, char* pszArgs[]){
 char String[128];
 cout << "Enter string: ";
 cin.getline(String, 128);
 palindromeChecker(String);

 cout << "Press Enter to continue...";
 cin.ignore(10, '\n');
 cin.get();
 return 0;
}

char palindromeChecker(char String[]){
 int flag = 0;
 int len = 0;
 while(String[len]){
  len++;
 }

 for(int i=0;i < len; i++){
  if(String[i] != String[len-i-1]){
   flag = 1;
   break;
  }
 }
 if(flag){
  cout << String << " is not a palindrome!\n";
 } else {
  cout << String << " is a palindrome!\n";
 }
}
