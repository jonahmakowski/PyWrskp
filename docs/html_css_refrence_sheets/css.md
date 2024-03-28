
# CSS Glossary

* [List of every possible CSS rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) 

* [List of web colors](https://www.w3schools.com/tags/ref_colornames.asp)

* [List of web fonts](https://web.mit.edu/jmorzins/www/fonts.html)
  
# Selectors
Tag selectors are just the name of the tag you want to add styles to and look like this in CSS.

```
main {

}
```
And like this in the HTML

```
<main>
  Some content
</main>
```
## Class selectors (multiple elements)
In CSS create a class and add style rules

```
.my-class {
  background-color: #ff00ff;
  font-size: 12px;
}
```
Add your class to HTML
```
<div class="my-class">Div 1</div>
<div class="my-class">Div 2</div>
```
## ID selectors (one element)
Similar pattern to classes, but IDs are generally used for one specific element, while classes are for a group of elements.

In CSS:
```
#my-id {
  background-color: red;
  border-radius: 2px
}
```
Add your id to HTML
```
<div id="my-id">Stuff goes here</div>
```
## Properties + Values


| Properties  | Values  
| :------------ |:---------------:
| `background-color`, `color`      | <ul><li>predefined names (`aqua`, `green`, `teal`, `maroon`, `purple`, `black`... <a href="https://www.w3school.com/colors/color_names.asp" targer="_blank">see the full list here</a>.)<li>or use <a href="https://htmlcolorcoders.com/color-picker/" targer="_blank">a color</a></li></ul>
|  `padding`, `margin`, `width`, `height`     | <ul><li>pixels (`2px`)</li><li>percentage (`50%`)</li></ul>       
| `text-align` | `left` (default), `center`, `right`       

Some other properties that you can change are:
```
border
border-radius
font-size
font-family
font-weight
text-align
list-style
```