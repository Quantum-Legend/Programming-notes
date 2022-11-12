# Markdown Cheatsheet

<!-- Comments -->
Check the raw or open the file in a text editor (like VS code) to see the full text.

The Auto-Open Markdown Preview extension for VS code can help write markdown

<!-- Headings -->
> * Headings are made using # symbol
```Markdown
# Heading 1 (H1) 
## Heading 2 (H2) 
### Heading 3 (H3)
#### Heading 4 (H4)
##### Heading 5 (H5)
###### Heading 6 (H6)
```
# Heading 1 (H1) 
## Heading 2 (H2) 
### Heading 3 (H3)
#### Heading 4 (H4)
##### Heading 5 (H5)
###### Heading 6 (H6)

---
<!-- Italics -->
> * Italics are done by wrapping the text in asterik (*) or underscore (_):

*This text* is italic using *asterik* (*)

_This text_ is italic using _underscore_ (_)

---
<!-- Bold -->
> * Bold is done by wrapping the text in double asterik (**) or double underscore(__):

**This text** is bold using **double asterik** (**) 

__This text__ is bold using __double underscore__ (__)

---
<!-- Strikethrough -->
> * Strikethrough is done by wrapping the text in:

~~This text~~ is strikethrough using tildae (~)

---
<!-- Horizontal Rule -->
> * Horizontal Rule is made using --- or ___

---
___

> * Asteriks, Underscores can be actually displayed using escape sequence (\\) 

\*Hi\* \_This will show\_ the \*\*Characters\*\*
```Markdown
 For double symbols you have to do \*\* Characters \*\* as shown above
```

---
<!-- Blockquote -->
> * To make a blockquote we use the > sign

> * This is a quote. We have used quotes in this md file for the description of the syntax.

---
<!-- Links -->
> * For links we wrap the text to be shown in [] and then type the url in () after it.

```Markdown
[<Text to be shown>](<url>)
```
[My Github Repo](https://github.com/Quantum-Legend/Programming-notes)

> * To have a title to be shown on hovering over it put a space after the url and type the title within ""

```Markdown
[Text to be shown](<url> "<Text to be shown when hovered>")
```
[My Github Repo](https://github.com/Quantum-Legend/Programming-notes "The github repository for this md file")

---
<!-- Unordered Lists/Bullet points -->
> * To create unordered lists (bullet points), use a asterisk (\*) followed by space for each item.
For nested items, indent with tabs.

* Item 1
* Item 2
    * Sub item 2A
        * Nested Sub item 2A (i)
    * Sub item 2B
        * Nested Sub item 2B (i)

---
<!-- Ordered Lists/Numbered points -->
> * To create ordered lists (numbered points), use the syntax 1. followed by space for each item.
For nested items, indent with tabs.

1. Item 1
1. Item 2
    1. Item 2 option 1
1. Item 3
    1. Item 3 option 1
    1. Item 3 option 2

---
<!-- Inline Code Blocks -->
> * To create inline code blocks, we enclose within backticks (`).

`<p>This is a paragraph<\p>`

---
<!-- Images -->
> * Inserting images is similar to links but we put an ! before the []

```Markdown
![Markdown Logo](https://markdown-here.com/img/icon256.png)
```
![Markdown Logo](https://markdown-here.com/img/icon256.png)

---
<!-- Github markdown -->
## For github flavour of markdown:

---
<!-- Code Blocks -->
> * For showing codeblocks, enclose within triple backticks (```)

```
    git add <file name>
    git commit -m "message"
```

> * You can specify syntax specific codeblocks by specifying it in front of the opening triple backticks (Eg: ```javascript)

### Python codeblock:
```python
print("Hello World!")
def something():
    for i in range(10):
        i+=1
    return i
```

### Javascript codeblock:
```Javascript
function add(num1, num2) {
    return num1 + num2;
}
```

---
<!-- Tables -->
> * To insert tables we use | as column seperator then horizontal rule (---) on second line

```Markdown
| Item        | ID |
|-------------|----|
| Box         | 2  |
| Matchsticks | 3  |
```
| Item        | ID |
|-------------|----|
| Box         | 2  |
| Matchsticks | 3  |

---
<!-- Task Lists -->
> * Task lists are like checkboxes on github.
Write them like unordered lists (with asteriks) followed by [x] for checked or [] for unchecked

```Markdown
* [x] task 1
* [x] task 2
* [ ] task 3
```
* [x] task 1
* [x] task 2
* [ ] task 3

