// A program that takes input from the console.
// It will ask the user for their name, and give a reply back
// using the input name.

#include <iostream>
#include <string> 
// Since we will deal with strings,
// we will include string header file from the c++ standard library.

int main()
{
    std::string name; // Here, we declare the variable 'name' of type string.
    std::cout << "What is your name?" << std::endl; // Asking the user for their name, a prompt.
    std::cin >> name;
    // cin is another object of the iostream file, in the standard library.
    // It is used to take the input from the user (character input).
    // It is used with the >> (extraction) operator, which puts the thing on its left into the thing on its left (Extracting from).
    // So, here the cin object takes a string of input from the user and it is then put into the 'name' vaariable
    
    std::cout << "\nHave a good day, " << name << "!" << std::endl;
    // A cout statement can be written with more than one insertion operators too.
    // This sequence works as a concatenation of all the objects and finally inserting
    // it into the cout object.
    // Here, we have also used a \n character, which is a newline character.
    // It is a escape character, which has a special meaning, to go to the new line.
    // Escape characters are written using a back slash (\)

    // Note: The cin object cannot take strings with whitespaces,
    // entering such strings into cin may have unexpected results.
    // You have to use a special function getline() to take string inputs with spaces.
    return 0;
}