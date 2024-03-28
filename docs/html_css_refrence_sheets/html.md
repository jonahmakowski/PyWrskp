## Tags and Attributes

## Structure
A webpage is made up of three basic tags: html, head, body.

Glitch makes this for you, you just need to know where to put your tags.
```
<html>
  <head>
    <title>My Webpage</title>

    <!-- information about the webpage goes here -->
  </head>

  <body>
    <!-- Put all your tags to show on the page here -->
  </body>
</html>
```
## Headings
This makes the largest heading
```
<h1>Heading Goes Here</h1>
```
You can use these tags to make smaller headings, the bigger the number the smaller it is.

- h2
- h3
- h4
- h5
- h6
## Text
Use `p` to add text to a page.
```
<p>My text goes here</p>
```
## Images
Include an image with the img tag. Use a src attribute to use an image from a url.
```
<img src="https://media.giphy.com/media/JOGDMviQHZvC2QGWeg/giphy.gif">
```
## Links
Make a link to another page with a. The link will go to the url you put in the href attribute.

### Example of an External Link:
See how the 'href' link goes to another website:
```
<a href="https://media.giphy.com/media/JOGDMviQHZvC2QGWeg/giphy.gif">External Link</a>
```
### Example of a Relative/Internal Link:
See how the 'href' link goes to a different page on our webpage and it ends with '.html':
```
<a href="contact_info.html">Relative Link</a>
```
## Lists
Make a list by using a list tag, ul. Wrap each item in the list with li tags.
```
<ul>
  <li>Dog</li>
  <li>Cat</li>
  <li>Bird</li>
</ul>
```
li means list item. ul means unordered list. Use ol, ordered list, if you want the list to be numbered.
```
<ol>
  <li>Dog</li>
  <li>Cat</li>
  <li>Bird</li>
</ol>
```
## Divs
These tags have a lot of power! You can use them by themselves to create things on the page.
```
<div>Some text goes here</div>
```
You can use divs to group other tags together. Later on we'll learn how to style groups of tags with divs.
```
<div>
  <p>My paragraph</p>
  <a href="http://link.com">my link</a>
</div>
```
## Fun Tags
You don't need to know any of these, but they can be fun to spice up a page.

Scrolling text from right to left
```
<marquee>This text will scroll from right to left</marquee>
```
Scrolling text from bottom to top

```
<marquee direction="up">This text will scroll from bottom to top</marquee>
```
Bounce around in a box. Change the width and height to change the size. Try using an image instead of text!
```
<marquee direction="down" width="250" height="200" behavior="alternate" style="border:solid">
  <marquee behavior="alternate">
    This text will bounce
  </marquee>
</marquee>
```
## Blink text
```
<blink>Blinking text</blink>
```
Line break, make text go to the next line.
```
Some text here<br>This will go on the new line
```
Quotes
```
<blockquote cite="https://www.huxley.net/bnw/four.html">
    <p>Words can be like X-rays, if you use them properly—they’ll go through anything. You read and you’re pierced.</p>
</blockquote>
```
## Order of Specificity
<ol>
  <li><strong>id</strong> is the most specific</li>
  <li><strong>class</strong> is the 2nd most specific </li>
  <li><strong>element</strong> is the 3rd most specific </li>
</ol>