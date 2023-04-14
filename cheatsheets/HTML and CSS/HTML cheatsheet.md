# Cheatsheet for HTML

## Table of contents
[What is HTML](#what-is-html)

[Tags](#tags)

[Structure](#structure)

[Title Tag](#title-tag)

[Heading Tag](#heading-tag)

[Paragraph Tag](#paragraph-tag)

[Horizontal Rule Tag](#horizontal-rule-tag)

[Break Tag](#break-tag)

[Formatting Elements](#formatting-elements)
* [Bold](#bold)
* [Italic](#italic)
* [Underline](#underline)
* [Strikethrough](#strikethrough)
* [Subscript and Superscript](#subscript-and-superscript)
* [Preserve](#preserve)

[Images](#images)

[Hyperlinks](#hyperlinks)

[Tables](#tables)

## What is HTML?

HTML stands for **H**yper **T**ext **M**arkup **L**anguage.
It is a language used to create webpages (along with CSS and JavaScript)

Consider an analogy: A human body consists of broadly three systems -
the _Skeletal system_, the _nervous system_ and the outer _muscular system_.

* In a webpage, _HTML_ provides the **structure**, similar to how the _skeleton_ provides **structure** to the human body.
* The _nervous system_ is present for the **functionality** of a human body. _JavaScript_ plays that role in a webpage.
* The **outer appearance** of a human body is contributed by the _muscles, skin, hair, etc_. This is done in a webpage using _CSS_,
  which is used for **formatting and styling purposes** for the **general appearance** of a webpage.

---
## Tags

HTML is written using _tags_, which are like the bones in a skeletal system.
A tag is written by typing a keyword within angular brackets (<>).
An opening tag is usually followed by some content, then a closing tag, which is the same tag but with a forward slash (/) in front.


```HTML
<keyword> <!--Opening Tag-->
	content
</keyword> <!--Closing Tag-->
```

> Note: A comment is written in HTML by opening with `<!--` and closing with `-->`

There are also empty tags, which are tags that dont require any content within them, so there's no opening or closing tags, only one tag
which is followed by a / before the >.
```HTML
<link/> <!--An empty tag--> 
```

Tags may also have attributes, which are basically some characteristics that give more description to a tag.
They are written inside the angular brackets of the tag.
Attributes are usually name and value pairs, written as:
```HTML
<tag attributeName = attributeValue>
```

---
## Structure

The general structure of an html file is something like this:

```HTML
<!DOCTYPE html> <!--This tag is used by the browser to understand that the document type is going to be html-->
<html> <!--The html tag encloses the complete html document-->
	<head>
		<!--The title and some other data related to website comes within the head tag-->
		<title>My first website</title>
 	</head>
	<body>
		<!--The body tag contains everything that actually appears on the web page-->
		Hello World!
	</body>
</html>
```

> The landing page of a website is generally index, so we save that file with index.html

The above html code will give us this webpage on a browser:

![My first website image](./Images/My%20first%20website%20screenshot.jpg)

> Note: The right part of this image shows the google developer tools. You can view this by right-clicking on the webpage and clicking on inspect. This can be done on any website and you can see the html code of that website in elements.

---
## Title Tag
This tag comes inside the head tag. It shows the title of the html webpage. In the above example screenshot, you can notice that the title of the webpage is 'My first website' and it appears on the top where the tabs are.

```HTML
<head>
	<title>My first website</title>
</head>
```
> The title is what is usually displayed in the search results so having an appropriate title is important.

---
## Heading Tag
As the name suggests, the heading tag gives the heading to the content in the webpage. It is written within the body tag. It comes in six different sizes.

```HTML
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```
which look like:

![Headings in html image](./Images/Headings%20in%20HTML.jpg)

The h1 tag is the largest and h6 is the smallest.

> Note: HTML headings should be used as headings only. Do not use them to make some random text appear big and bold, because search engines use the headings to index the structure and contents of a webpage.

---
## Paragraph Tag
The paragraph tags are used to show the actual content in the body of a website. Since HTML is whitespace insensitive, if you write content within the body tag without the paragraph tag, you will get them all on the same line regardless of how much space or new lines you have inserted between them in the source. The paragraph tags, as their name suggests, are used for making new paragraphs within the body. They also provide other functionality such as enabling us to style the text.

It is denoted by the `<p>` tag
```HTML
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```

---
## Horizontal Rule Tag
The Horizontal Rule tag `<hr/>` is used to draw a horizontal rule or line on the webpage.

```HTML
<h2>The Big Bang</h2>
<hr/> <!--This will draw a horizontal line between the heading and the paragraph-->
<p>The big bang is the most accepted theory about the beginning of our universe</p>
```

---
## Break Tag
All the lines inside a paragraph tag are shown on the same line on the webpage, even if there is a new line in the html code. To add a break in line, or to show a line on a new line instead of the same line as the previous one, the break tag `<br/>` is used.

```HTML
<h2>The Big Bang</h2>
<hr/>
<p>The big bang is the most accepted theory about the beginning of our universe. <br/> It states the the universe started from just a small point called as singularity and it expanded froom there.</p>

<!--This will show the lines as:
The big bang is the most accepted theory about the beginning of our universe.
It states the the universe started from just a small point called as singularity and it expanded froom there.
on the webpage-->
```

---
## Formatting Elements

### Bold:
Bold tag `<b>` is used to make text bold.

```HTML
<b>This</b> text is bold
```
This will show the text as:
**This** text is bold

### Italic:
Italic tag `<i>` is used to make text italicized.

```HTML
<i>This</i> text is italic
```
This will show the text as:
*This* text is italic

### Underline:
Underline tag `<u>` is used to make text bold.

```HTML
<u>This</u> text is underlined
```
This will show the text as:
<u>This</u> text is underlined

### Strikethrough:
Strikethrough tag `<strike>` is used to strike through the text

```HTML
This costs <strike>$20</strike> $10
```
This will show the text as:
This costs ~~\$20~~ $10

### Subscript and Superscript:
To have subscripts, we use the subscript tag `<sub>`
To have superscripts, we use the superscript tag `<sup>`

```HTML
x<sub>1</sub> = a<sup>2</sup>
```
This will be shown as:
x~1~ = a^2^

### Preserve:
The preserve tag is used to preserve blank or whitespaces in the html code on the webpage. Whatever is within the preserve tag will show up as it is on the webpage.

It is denoted with the `<pre>` tag
```HTML
<pre>Leaving blank spaces            intentionally</pre>
```
Shows up as:
<pre>Leaving blank spaces            intentionally</pre>

## Images
To insert images in the webpage, the `<img src = "image path" alt = "Alternate text"/>` tag is used. The src attribute is used to specify the path of the image to be inserted, and the alt attribute is used for displaying the alternate text to be used in case the image is not found.

It also takes attributes to specify the width and height of the image, or by using the style attribute to do the same.
```HTML
<img src = "Milky Way Galaxy.jpg" alt = "An image of the Milky Way Galaxy" width = "150px" height = "100px"/>
<!--A better way to do whis would be by using the style attribute-->
<img src = "Milky Way Galaxy.jpg" alt = "An image of the Milky Way Galaxy" style = "width:500px; height:250px"/>
```

## Hyperlinks
To insert hyperlinks (text or images that you can click on which takes you to a different part of the webpage or a different webpage entirely), we make use of the anchor tag `<a>`

We give the url of the page or section we want to send to through that link in the href attribute of the anchor tag.
```HTML
<p>For more info about the Milky Way Galaxy,<a href = "https://www.wikiwand.com/en/Milky_Way">click on this wikilink</a></p>
```
Which will show as:
For more info about the Milky Way Galaxy, [click on this wikilink](https://www.wikiwand.com/en/Milky_Way)

You can also link to your other pages, if you have stored them in the same folder. Put the file path of the other html doc in href.
```HTML
<p><a href = "Andromeda.html">Click here for information about the andromeda galaxy</a></p>
```

To create links to navigate in a single webpage, we use the 'id' attribute in the tags which we want to navigate to. The id attribute defines a value which can be used to refer to the tag with that id.

To create a hyperlink to tag in the webpage, the href attribute in the anchor tag uses the id of the referred tag preceded with a hash (#) as the value.
```HTML
<body>
	<h1>Table of contents</h1>
	<p><a href = "#Milky Way">Jump to Milky Way Galaxy</a></p>
	<p><a href = "#Andromeda">Jump to Andromeda Galaxy</a></p>
	<p><a href = "Other Galaxies.html#N1560">Jump to the galaxy N1560</a></p>
	<!--In this way you can also link to an id present in a different html webpage-->

	<h2 id = "Milky Way">Milky way Galaxy</h2>
	<p><!--Some content--></p>

	<h2 id = "Andromeda">Andromeda Galaxy</h2>
	<p><!--Some content--></p>
```

## Tables
We can create tables in HTML using the `<table>` tag.
It uses tags such as `<tr>` which is table row, `<th> ` which is table heading and `<td>` which is table data.

Each row in the table starts with the`<tr>` tag.
If the data in a row has to be specified as a column heading, it is used with the `<th>` tag.
Otherwise for normal data, it is used with the `<td>` tag.

```HTML
<table>
	<caption>Planets and their number of satellites</caption>
	<tr>
		<th>Planets</th>
		<th>No of Satellites</th>
	</tr>
	<tr>
		<td>Mercury</td>
		<td>0</td>
	</tr>
	<tr>
		<td>Venus</td>
		<td>0</td>
	</tr>
	<tr>
		<td>Earth</td>
		<td>1</td>
	</tr>
	<tr>
		<td>Mars</td>
		<td>2</td>
	</tr>
</table>
```

This shows up like this but without any borders:

Planets and their number of satellites
|Planets|No of Satellites|
|-------|----------------|
|Mercury|               0|
|Venus  |               0|
|Earth  |               1|
|Mars   |               2|

Various attributes can be used to customize the table.
* `<table border = "2">` - Gives a border to the table, which has a thickness of 2
* `<table cellpadding = "5">` - Makes space of 5 units between the data and the borders in a cell, i.e. pads the data by 5 units
* `<table cellspacing = "10">` - Makes space of 10 units between each of the cells in the table and also between the cell and border
* `<table width = "500px">` or `<table width = "50%">` - Specifies the width of the table in pixels or as percentage of the webpage.
* `<th colspan = "2">` - Makes the data in this tag occupy space of two columns instead of 1, can also be used with `<td>`
* `<th rowspan = "5">` - Makes the data in this tag occupy space of 5 rows instead of 1, can also be used with `<td>`
