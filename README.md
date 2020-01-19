THREADSWAP

My initial concept was a much more unique concept - I wanted to create a site
in which people can trade their clothes with one another. Unfortunately, this 
wouldn't quite match the brief, as payments wouldn't be involved, so I instead
simplified the concept to a more traditional second hand ecommerce site.

UX

My main focus was keeping the layout simple, as research into other ecommerce
sites showed that it can get quite busy on the screen, so having a clean layout
kept everything in order.

This meant keeping a fresh colour pallette, and making sure the layout was
logical and basic.

FEATURES

Existing Features

Due to the complexity of Django, and not having much time left in the course, I
had to keep the project simple, so there aren't many unique features.

Users can create items to be sold, and can purchase items as well.

Future Features

Due to time constraints, I was unable to hide an item if it was already in the
cart. This would make sure that customers can't purchase the same item twice. I
believe you would need to create a new boolean field in the item model, that would 
confirm if the item is in the cart. This would be updated when adding the cart or
removing from the cart, and would be used to hide items when looping through them
in the items.html page.

I also wanted to implement an in-depth search function, so that if there were
many items, customers would be able to easily navigate the website. I had a very
basic search function, but struggled with the time left to build on this, so I
removed it altogether. I would implement a search function that allows users to
search by item type (jumper, shirt etc.) as well as by size, and price.

TECHNOLOGIES USED

This project was created using:

HTML
CSS
Javascript
JQuery
Bootstrap
Python
Django
Heroku
Stripe
S3

TESTING

This project was tested throughout production, I came across too many issues to
list here.

Most notably, I had many issues with the implementation of Stripe, as it wouldn't
throw out an error message, but the payment would fail every time. This made
solving the issue difficult, as I had to simply use trial-and-error to determine
the issue. It seemed that the issue lied with JQuery being below Stripe, meaning
Stripe wasn't able to use JQuery to function.

I tested each function as it was created, and tested each function after, as an
ongoing theme for this project was functions breaking despite not touching them!
This was always because a new function I'd created would have impacted it in some
way, causing issues with previous ones.

DEPLOYMENT

I used Github for version control, and finally deployed the project using Heroku. 

MEDIA

I created my own logo for this project, as I couldn't find a suitable logo that
fitted the theme.

This was the only media used, in order to keep the interfact clean and simple

ACKNOWLEDGEMENTS

A huge thank you to:

Brian Macharia - My mentor who helped me keep my priorities in order, and really
helped me to understand the fundamentals of Django.

Tutor support - MANY times I turned to them to help me get a head start on 
resolving many of the issues I faced.

Stack Overflow - I would often turn to help from the users at Stack Overflow to 
help further with any concepts I couldn't understand