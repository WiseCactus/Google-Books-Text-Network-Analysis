# Google-Books-Text-Network-Analysis

I was motivated to make this program because as a former social science student, I found that since there is so much information nowadays, researching about a topic was often an over-convoluted and inefficient process. It also made me sad because many (older) books (that are usually in archives) tend to get lost and not to the people who may benefit from reading it.

I am hoping that my program can help researchers or any curious individuals understand the type of discourse that surrounded a particular topic in a particular time period by providing a visual text network that would display the various nouns, adjectives/adverbs, and verbs associated with it. The program will also provide a list of all of the associated words along with the title and links of the books that contain those associations. The hope is to make this accessible to anyone by deploying the program through Heroku.

To start, the program gives the user the option to select a word of choice, and a set span of dates that they would like to gain insight from.
The user also must enter an interval to set the various time periods that they would like to visually display (for example in the screeshot demo, the interval of 10 when start date is 1800 and end date is 1930 would produce 13 graphs, former with words pertaining to associations in books that were created from 1810-1820, etc., but the same start and end date with interval of 30 wouldd produce one graph with associations from books created in 1800-1830).
The user must also provide a number that the the program will use to determine the number of books that it goes through. A number over 10 is recommended because higher number will create a more holistic graph, but is not necessary.

The user is also provided with several options to specialize their search. First, they are able to enter keyword(s) that may help contextualize the search a bit more (i.e. in the screenshot the user's word is mold; if we wants to understand how it was understood scienfitically, they may add 'botany' and/or 'science' (If both are added, keywords must be separated by spaces). And second, they have the option to search through only books, magazines, or newspapers (in default the program will search through any one of these); they must enter m for magazines, b for books, and n for newspapers in the analysis type box.


![Screen Shot 2022-01-22 at 6 44 58 PM](https://user-images.githubusercontent.com/76268134/150659070-cc73a6c7-feae-4485-a02f-71d48c6855d5.png)



I created a web crawler to then go through all of the books that contains the word of choice, and screenshot those pages. 

Here is a little demo of how the scraper operates. The scraper zooms in so that the text is more legible, and before scrolling down, screenshots the text.

All these images are saved in png format and subsequently compiled and saved into a pdf, then deleted to not overload storage :) 

The program will then leverage to Google Drive API to convert the pdf files  into google docs, which has an in-built automatic OCR conversion. The program will then  convert the google doc(s) to (separate) text file(s) and feed it back to the program for text pre-processing.

https://user-images.githubusercontent.com/76268134/146480531-96044276-2212-476b-b7e6-69eb1fa918a2.mp4


The program will then pre-process the lines in the text file(s), which will involve getting rid of words that are not associated to the book (i.e. "Page 4", which you can see appears with the book pages), and then go on to get rid of symbols, lower case the words, lemmatize, spell-check, in that order.  The program will then take this text and generate an adjacency list that composes of all of the words close to the selected word.


Given all of that, the final output will produce a weighted graph and a list. The way that the graph is weighted is that the program finds the words that is to be contextualized and assigns the following numerical values to words beside it; directly to the right or left of the word gets 5 points, 1 word away gets 4 points, up until 4 words away gets 1 point. Therefore, the numerical value is not merely the number of times the word has been seen associated with the chosen word. The words will also be visually displayed in the syntatic category that they are associated to, with nouns at the top left, adjectives and adverbs at the top right, verbs at the bottom right, and everything else at the bottom left. The size of the node will also increase with a heigher weighting to make the strongest associations obvious to the reader.

These networks are meant to provide the user with more insight and direction about the various topics/words that are associated with their word. That being said, users should exercise caution in coming to immediate conclusions with the results, and should take it upon themselves to read the sources cited in the hyperlinks to see how the other words in the network are associated to the selected word. For example, a user can type a word 'plant' and include the keyword 'love', but these words can show up with high weightings because they are next to each other in the title of a book or chapter, or be next to each other in a book's glossary. Users can observe the weights associated to each associaton to gauge how often a topic is tied to the selected word.

With that being said, a good precautionary measure to take in light of this situation is to gauge if a word is associated with many different books in the graph; Since the writers of books are independent of one another, this will give a good sense of whether the topic was more or less associated with another topic in a particular time period.

It should also be noted that the networks generated in later years are more likely to be insightful than that of earlier years, since the OCR segment of preprocessing the text is not as adept at recognizing words in older texts, as well as because many old & middle english words would not be found in the dictionary we use to cross-check the validity of a given word.


The output of this program will look like the following (to look at (an updated) output in full, check out the attached notebooks file):

![bifurcat](https://user-images.githubusercontent.com/76268134/149076115-713b1919-40af-45b9-bc42-d1b2e0382245.png)

![Screen Shot 2022-01-12 at 1 33 55 AM](https://user-images.githubusercontent.com/76268134/149076285-3ba47900-2182-4344-9902-515b3fd068ee.png)


Current updates focus on trying to product outputs that provide more context to the user, rather than mere associations of words.


Thank you!
