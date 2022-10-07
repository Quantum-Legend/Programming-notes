// A simple C++ program to print Hello World!
// The program is small, but I have put what each line means as comments
// in detail, so that it can be read and understood.
// Traditionally, it is the first program written in a programming language.

// As you can see, a comment in C++ is written using // (two forward slashes)
// Comments are pieces of text that are completely ignored by the compiler,
// and are used for readability of the code by humans.
// Comments can also be written using /* to open and */ to close

/* These are multi-line comments
So you can write them in this way.
They are usually used for documentation or well,
to write long comments over multiple lines.
*/

#include <iostream> // In the first line we include the libraries we will use.
// The #include is a preprocessor directive. These statements do not end with a ;
// We are using the iostream library, which is a part of the C++ standard library.
// It contains objects and functions to display text output to the screen,
// and receive text inputs from the keyboard.

// using namespace std; 

//Then we have the main entry point to the program.
//It is a function that is executed by default by the system.
int main()
{
    // The body of a function is a block of code,
    // and it is delimitted by {} (curly braces),
    // symbolising the beginning and the end of the block.
    // You can add indents to the code to make it more readable by a human,
    // but the C++ compiler doesn't require you to do so.

    std::cout << "Hello World!" << std::endl; // The first line of our code block is to print Hello World!
    // cout is an object from the iostream file.
    // It is a member of the standard library, so we use the :: (scope resolution) operator,
    // to represent this membership.
    // cout is character output, which represnts the output window and we must send some text to it.
    // For this, we use the << (insertion) operator to put the text on its right in the cout object on its left (Inserting into).
    // std::endl is another standard library symbol for a new line.
    // Almost every line of code in C++ end with a semicolon, but not all.

    return 0;
    // Since main is a function that returns an integer, we return 0 with the return keyword.
    // A function returns a value to whoever calls it, but since the main function
    // is called by the system, we have no use of it here, other than as a sign of
    // completion of the program (0 traditionally means that no errors came up in the program).

    // You may use a statement at the start of your code after the include statements:
    // using namespace std;
    // to simplify your typing. The cout and endl are members of what is known as the
    // std namespace, so writing that statement at the beginning of the code allows you to
    // omit typing std:: each time and use it by default. Although it may simplify the typing at the basic level,
    // using that statement may also bring some hazards, and so it is considered as bad practice.
}