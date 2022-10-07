/* Important aspects about variables in C++
-> Variables are temporary data storage units.
-> They must be declares prior to being used.
-> The declaration of a variable must specify a type and a name.
-> The declaration may also contain an initialization.

You assign values to your variables in your code.
These vales are knowns as constants or literals.
Syntax for the constants/literals of some types:
A)  int : 123, -5, 023, 0x3A, 0b1100, 23U
    There are special format to specify the radix of the number,
    i.e. to specify in which number system a particular int number is in.
    -> Decimal: 123, -5 are examples of numbers in decimal number system, they are plain numbers
    -> Octal: A number with a leading zero represents an octal. Eg: 023
    -> Hexadecimal: Hexadecimal numbers are specified by starting the number with '0x'. Eg: 0x3A
    -> Binary: For binary numbers, start the number with '0b'. Eg: 0b1100
    -> Unsigned: Unsigned integer can also be specified with a trailing 'U' or 'u'. Eg: 23U, 23u

B) float: 23.0f, 0.0f 
   float numbers are entered with decimal point and at least one digit to its right, even if its an integer.
   It must be specified with a trailing 'f'.

C) double: 25.4, -22.5
   double are the default floating number type.
   They are written like float literal, without the trailing 'f'.

D) char: 'a', 'X', '\0', '\n'
   char may be be entered as integers as long as they fit in 8 bits.
   Their ASCII character interpretation is entered within single quotes.
   \0 and \n are special characters called as excape characters.
   \0 is the null characer to delimit the end of a string.
   \n is newline character.

E) string: "hello world!"
   string characters are written within double quotes.
*/

// Lets write a simple program to demonstrate variable declaration in c++.

#include <iostream>

int a, b =5; // Declaration of variables using the type and name.
// You can declare mmultiple variables of one type on the same line, seperating them using commas.
// Variables may (b) or may not (a) have an initial value.

// Notice how the variables a and b are declared at the same level of indentation as the main() function.
// This means that they are global variables.
// Global variables are accessible to all parts of the code, because of this
// the memory to global variables is managed statically by the compiler.
// So they are allocated to the data segment of the memory.
// Once the program ends their memory is freed.

// Variables may be local to their scope, i.e they may be declared within a function or a loop,
// These variables are accessible in their scope (within the functon/loop) 
// Once code execution leaves the scope, its variables are deleted and their memory is freed.
// These are called automatic variables because the are managed by the compiler
// and they are usually allocated in the stack segment of the memory, which is temporary.
int main()
{
    bool my_flag; // Declaration of a local variable of boolean (bool) type.
    //The scope of this variable is within the main function and it is not accessible anywhere else.

    // There are some rules for naming variables, which can be looked up at cppreference.com
    // Variable names must start with a non-number character, and may contain letters, numbers and 
    // some special characters such as hyphen(-) and underscore(_).
    // Variable names must also not be the same as any of the keywords defined in the language, like int or return.

    // Let us use the defined variables
    a = 7; // The value 7 is assigned to the variable a
    // Note that the assignment (=) operator works from the right to left.
    // i.e. 7 is assigned to a.
    my_flag = false;

    // cout can be used to print the values contained in variables.
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    std::cout << "flag = " << my_flag << std::endl; 
    my_flag = true; 
    std::cout << "flag = " << my_flag << std::endl; // Values in the variables can be changed or re-assigned
    std::cout << "a + b = " << a + b << std::endl; // Variables are useful to carry out operations like addition, etc.
    std::cout << "b - a = " << b - a << std::endl;

    // Lets see what happens if you assign a negative number to an unsigned integer!
    unsigned int positive;
    positive = b-a;
    std::cout << "(unsigned) b - a = " << positive << std::endl;
    // If you execute this part of the code, you will get a huge number.
    // This number is actually the number 2^32 - 2
    // This number is obtained because it is the 2's complement representation
    // of -2 in binary. 
    return 0;
}