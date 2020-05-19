# Project 0

Web Programming with Python and JavaScript

My web site is created to record homeowners association fees payments, consult payments already done, and update users information such as name, house number and email.

The App has four html pages
.- index.html (Home)
.- insert.html (insert payments)
.- list.html (list payments already done)
.- update.html (update user information)

You can get from any page of the site to any other page using the nav menu in the bottom of the page

The web site has an image at home page (index.html file), has a table in list.html file and has an unordered list in update.html file; list items are:
.- House number
.- First name
.- Last name
.- Email

The list uses list-group bootstrap component to eliminate bullets and the flex-column class,  to make it responsive.

The web site uses a stylesheet file called mystyle.css in order to set  table style and nav menu style. 

It also uses media queries with the purpose of change  background color and font size when screen size changes from desktop size to tablet size or smaller.

Stylesheet mystyle.css use some CSS properties such as border, padding, text-align,  background-color, margin, and different types of CSS selectors: h1, nav, footer, .image, #pago, body among others.

The app uses bootstrap nav component (for nav menu at the bottom of each page). Also the app uses list group component in the update.html file

In the insert.html file the content for input data was designed with two responsive columns when screen is  desktop size and just one column for smaller sizes, in both cases bootstrap columns grid model was used.

In mystyle.scss file there are some variables such as
$smallbgcolor: #ccffcc; 
to define backgrond color for screen smaller size

$minwidth:992px; 
$maxwidth:991px;
to define which sizes activate the smaller screen style

Styling id #pagos is used to style the table. There are a nesting SCSS because td and th selectors are table selector's children

Id #pagos also uses inheritance because there is a generic pattern called %pattern-basic that set common properties for th and td selectors.
