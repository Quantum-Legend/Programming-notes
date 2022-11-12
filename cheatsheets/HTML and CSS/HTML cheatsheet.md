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
An opening tag is usually followed by some content, then a closing tag, which is
the same tag but with a forward slash (/) in front.

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
All the lines inside a paragraph tag come