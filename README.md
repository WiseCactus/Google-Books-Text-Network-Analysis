# Google-Books-Text-Network-Analysis

I was motivated to make this because I am deeply saddened by how many books are created and don't get to the people that would highly benefit from reading it. After all, we only have so much time to find and read new books. 
I am hoping that my program can help researchers or any curious individuals understand the type of discourse that surrounded a particular topic in a particular time period by providing a visual text network that would display the various nouns, adjectives/adverbs, and verbs associated with it. The program will also provide a list of all of the associated words along with references to the links of the books that contain those associations. The hope is to make this accessible to anyone by deploying the program through Heroku.

To start, the program gives the user the option to select a word of choice, and a set span of dates that they would like to gain insight from.
The user also must enter an interval to set the various time periods that they would like to visually display (for example in the screeshot demo, the interval of 10 when start date is 1800 and end date is 1830 would produce 3 graphs, former with words pertaining to associations in books that were created from 1810-1820, etc., but the same start and end date with interval of 30 wouldd produce one graph with associations from books created in 1800-1830).
The user must also provide a number that the the program will use to determine the number of books that it goes through. A number over 10 is recommended because higher number will create a more holistic graph, but is not necessary.

The user is also provided with several options to specialize their search. First, they are able to enter keyword(s) that may help contextualize the search a bit more (i.e. in the screenshot the user's word is mold; if we wants to understand how it was understood scienfitically, he may add botany and/or science can be added into the keywords). These keywords must be separated by spaces. And second, they have the option to search through only books, magazines, or newspapers (in default the program will search through any one of these); they must enter m for magazines, b for books, and n for newspapers in the analysis type box.


![Screen Shot 2022-01-22 at 6 44 58 PM](https://user-images.githubusercontent.com/76268134/150659070-cc73a6c7-feae-4485-a02f-71d48c6855d5.png)






I created a web crawler to then go through all of the books that contains the word of choice, and screenshot those pages. 

Here is a little demo of how the scraper operates. The scraper zooms in so that the text is more legible, and before scrolling down, screenshots the text.

All these images are saved in png format and subsequently compiled and saved into a pdf, then deleted to not overload storage :) 

The program will then leverage to Google Drive API to convert the pdf files  into google docs, which has an in-built automatic OCR conversion. The program will then  convert the google doc(s) to (separate) text file(s) and feed it back to the program for text pre-processing.

https://user-images.githubusercontent.com/76268134/146480531-96044276-2212-476b-b7e6-69eb1fa918a2.mp4


The program will then pre-process the lines in the text file(s), which will involve getting rid of words that are not associated to the book (i.e. "Page 4", which you can see appears with the book pages), and then go on to get rid of symbols, lower case the words, lemmatize, spell-check, in that order.  The program will then take this text and generate an adjacency list that composes of all of the words close to the selected word.


Given all of that, the final output will produce a weighted graph and a list. The way that the graph is weighted is that the program finds the words that is to be contextualized and assigns the following numerical values to words beside it; directly to the right or left of the word gets 5 points, 1 word away gets 4 points, up until 4 words away gets 1 point. Therefore, the numerical value is not merely the number of times the word has been seen associated with the chosen word. The words will also be visually displayed in the syntatic category that they are associated to, with nouns at the top left, adjectives and adverbs at the top right, verbs at the bottom right, and everything else at the bottom left.

The aforementioned output look like the following (to look at the output in full, check out the attached notebooks file):

![bifurcat](https://user-images.githubusercontent.com/76268134/149076115-713b1919-40af-45b9-bc42-d1b2e0382245.png)

![Screen Shot 2022-01-12 at 1 33 55 AM](https://user-images.githubusercontent.com/76268134/149076285-3ba47900-2182-4344-9902-515b3fd068ee.png)





Thank you!
