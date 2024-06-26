# A CSS reference for what we've used in this section

Font and sizes

- font-family
  - Changes the font used. Takes in one or more (commaseparated) font names.
- font-size
- Changes the size of the font in this container. Often, we use the rem unit to set font sizes, although between 16-18px is common as a root font size.
- font-weight
- Changes the boldness of the font. Use a value between 100 (very light) to 900 (very bold). Also, use keywords like normal or bold.
- text-decoration
- Changes any decoration of text like underline or strikethrough .
- line-height
- Changes the amount of space given to each line of text. I usually set this as a percentage, and I like giving my paragraphs between $135 \%$ and $150 \%$.

Spacing

- display: inline
- Sets the element to be inline (taking only the amount of horizontal space its content need). Setting to block instead makes it take $100 \%$ of the horizontal space.
- margin
- Sets the element's margin in the CSS box model. That's the separation from other elements.
- Can be given 4 values (e.g. 10px 5px 15px 20px), and that will set 10px for margin-top, $5 \mathrm{px}$ for margin-right, $15 \mathrm{px}$ for margin-bottom, and 20px for margin-left. Note it goes clockwise starting from margin-top.
- Can be given 2 values, the first one is margin top and bottom, and the second is margin right and left. Note it's also clockwise.
- Can be given 1 value, applied to all 4 sides.
- Alternatively you can use margin-top, margin-bottom, margin-right, and margin-left to control each side individually.

- padding
- As above, but for padding in the CSS box model.
- max-width
- Makes sure an element can't be wider than the value given.
- width
- Makes sure an element is exactly as wide as the value given.
- box-sizing
- Usually set to border-box for all elements. See the lecture on the CSS Box Model for information on what this is.
- border
- Lets us add a visible border to an element. As an example, border: 1px solid black;
- border-radius
- Rounds the border corners of an element. Value usually set in pixels, such as border-radius: 8px;

Color

- color
- Sets the foreground (text) color of the element.
- background-color
- Sets the background color of the element.

Flexbox

- display: flex
- Sets the display mode to flex (as opposed to inline or block). This allows us to use the new CSS flex mode for layout. See https://css-tricks.com/snippets/css/a-guide-toflexbox/ for a guide on how CSS containers and contained elements behave.
- flex-direction
- Changes the direction of elements inside a flex container. Usually, either row or column.
- flex-grow
- Splits the available space in a flex container between elements that have flex-grow. So if two elements have flexgrow: 1 , then they will split the space evenly. If one element has a value of 2 and the other of 1 , the first will try to take twice as much space as the second. However, all elements will still have enough space for their content.
