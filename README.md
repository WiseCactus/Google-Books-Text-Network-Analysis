# Google-Books-Text-Network-Analysis

I was motivated to make this because I am deeply saddened by how many books are created and don't get to the people that would highly benefit from reading it. After all, we only have so much time to find and read new books. 
I am hoping that my program can help researchers or any curious individuals understand the type of discourse that surrounded a particular topic in a particular time period by providing a visual text network that would display the various nouns, adjectives/adverbs, and verbs associated with it. The program will also provide a list of all of the associated words along with references to the links of the books that contain those associations.

To start, the program gives the user the option to select a word of choice, and a set span of dates that they would like to gain insight from.
The user also must enter an interval to set the various time periods that they would like to visually display (i.e. interval of 10 when start date is 1820 and end date is 1840 would produce 2 graphs, former with words pertaining to associations in books that were created from 1820-1830, latter from 1830-1840, same start and end date with interval of 20 wouldd produce one graph with 1820-1840).
The user is also provided the option to enter keyword(s) that may help contextualize the search a bit more (i.e. if they are interested in understanding what scientific progressions were made in botany, botany would be the word of choice, and botany and/or science can be added into the keywords). These keywords must be separated by spaces.

![Screen Shot 2022-01-12 at 1 09 51 AM](https://user-images.githubusercontent.com/76268134/149073512-f31a3b5e-6a2b-4d70-b95f-6f9cdf14216e.png)


I created a web crawler to then go through all of the books that contains the word of choice, and screenshot those pages. 

Here is a little demo of how the scraper operates. The scraper zooms in so that the text is more legible, and before scrolling down, screenshots the text.

All these images are saved in png format and subsequently compiled and saved into a pdf, then deleted to not overload storage :) 

The program will then leverage to Google Drive API to convert the pdf files  into google docs, which has an in-built automatic OCR conversion. The program will then  convert the google docs to text files and feed it back to the program for text pre-processing.

https://user-images.githubusercontent.com/76268134/146480531-96044276-2212-476b-b7e6-69eb1fa918a2.mp4



The user will then have to extract the text from the pdf using the following site (https://ocrgeek.com/) and then send the returned text file as input to the text generator segment of the program.  Before creating the text network, I will pre-process the text, which will involve getting rid of words that are not associated to the book (i.e. "Page 4", which you can see appears with the book pages), and then go on to get rid of symbols, lower case the words, lemmatize, spell-check, in that order.  The program will then take this text and generate a uni-gram corpora, then build an adjacency list that composes of all of the words close to the selected word.


The

Given all of that, the final currently looks like this (this is a zoom in of the graph, since its not legible when its zoomed out).
![Screen Shot 2021-12-16 at 9 30 53 PM](https://user-images.githubusercontent.com/76268134/146479265-25131b16-3df0-427c-8e21-084c9e267c5e.png)

Thank you!
