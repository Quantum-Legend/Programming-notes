# This is Vim!

* :q - quit vim
* :w - write changes
* :wq - write changes and quit vim
* :q! - dont save changes and quit vim 

You start vim in normal mode (where you cannot insert text). Press:

* i - enter insert mode
* ESC - return to normal mode
* I - go to beginning of line and enter insert mode
* a - enter insert mode placing cursor to the right of the letter
* A - enter insert mode placing the cursor to end of the line

## Navigation
* h - same as left arrow key
* j - same as down arrow key
* k - same as up arrow key
* l - same as right arrow key
* w - jump to the next word
* b - jump to previous word
* W - jumps to next word seperated by spaces
* B - jumps to previous word seperated by spaces
Example: "Hello_World.exe" 
* gg - move to beginning of the page
* G - move to end of page
pressing w will jump from beginning to the point(.), pressing W will jump the whole thing

## Normal mode
* r - replace a letter
* R - Replace mode
* cw - change word
* ciw - change inner word
* yw - yank word
* yiw - yank inner word
* yy or Y - yank line


## Using numbers
You can use numbers in the different commands to use them for that specific number of times. Examples:
* 12k - Equivalent to pressing the k key 12 times (which means the cursor will move up 12 lines)
* 5w - Jump ahead 5 words
* c3w - change 3 words
* y7w - yank 7 words
