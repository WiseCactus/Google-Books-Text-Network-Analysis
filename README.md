# Google-Books-Text-Network-Analysis

I was motivated to make this because I am deeply saddened by how many books are created and don't get to the people that would highly benefit from reading it. We only have so much time to find and read new books, and, as such, this project seeks to gather some insight on any given topic by understanding the context in which it was used in past decades.  In order to do this, I give the user the option to select a word of choice, and a set span of dates that they would like to gain insight from.  I created a web crawler to then go through all of the books that contains the word of choice, and screenshot those pages.  After this, the program will compile the images into a pdf.  The user will then have to extract the text from the images (https://ocrgeek.com/) and then send the returned text file to the program.  Before creating the text network, I will pre-process the text, which will involve getting rid of words that are not associated to the book (i.e. We couldn't make an image for this result. Click to view the whole p appears at the top of the text box), and then go on to get rid of symbols, lower case the words, lemmatize, and spell-check, in that order.  The program will then take this text and generate a uni-gram corpora, then build an adjacency list that composes of all of the words close to the selected word. More details can be found in the ReadME file.

The graph is displayed using the networkX library.

This is a project that is currently active. There is still a lot that I am trying to work out.
My next steps are as follows:
1. Make the text network something that depicts the variance in which the word has been used throughout the decades.
 How can we do this?
  -  Create an x-axis with the set of decades between the chosen decades that depicts the variance in which the word has been used throughout the decades.
  -  Make the default dictonary nested-nested, such that the adjacency list can contain dictionaries with years as their key values; This can then be used
     to create associations.
  -  Put these separate graphs side by side, and find a way to make associations between them, should they contain similar words (this means that the 
     dictionaries have to be able to create edges with one another).  
  - There are also lots of nodes, so I will cut out any that have a weight list that is less than 5.
2.  Refine the text pre-processing segment
What does this mean?
 - Some decades use 'old' language, and sometimes, our current dictionaries fail to account for that.Therefore, it might be good here 
   to find a text file or library that someone may have created that contains all the words in old english.
4.  Make the networks interactable and add hyperlinks to all the nodes, so that viewers can see the sources.
  How can we do this?
  -  Still unclear, but certain libraries like bokeh support networkx, so it might be a matter of finding a way to conjoin the two.
4. Make this available to the public. How this can be done is still unclear.


Given all of that, the final currently looks like this (this is a zoom in of the graph, since its not legible when its zoomed out).
![Screen Shot 2021-12-16 at 9 30 53 PM](https://user-images.githubusercontent.com/76268134/146479265-25131b16-3df0-427c-8e21-084c9e267c5e.png)


