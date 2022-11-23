# Google-Books-Text-Network-Analysis
I was motivated to make this because I am deeply saddened by how many books are created and don't get to the people that would highly benefit from reading it. We only have so much time to find and read new books, and, as such, this project seeks to gather some insight on any given topic by understanding the context in which it was used in past decades.  In order to do this, I give the user the option to select a word of choice, and a set span of dates that they would like to gain insight from.  

I created a web crawler to then go through all of the books that contains the word of choice, and screenshot those pages. 

Here is a little demo of how the scraper operates. The scraper zooms in so that the text is more legible, and before scrolling down, screenshots the text.

All these images are saved in png format and subsequently compiled and saved into a pdf, then deleted to not overload storage :) 

https://user-images.githubusercontent.com/76268134/146480531-96044276-2212-476b-b7e6-69eb1fa918a2.mp4



The user will then have to extract the text from the pdf using the following site (https://ocrgeek.com/) and then send the returned text file as input to the text generator segment of the program.  Before creating the text network, I will pre-process the text, which will involve getting rid of words that are not associated to the book (i.e. "Page 4", which you can see appears with the book pages), and then go on to get rid of symbols, lower case the words, lemmatize, spell-check, in that order.  The program will then take this text and generate a uni-gram corpora, then build an adjacency list that composes of all of the words close to the selected word.




The graph is displayed using the networkX library.

This is a project that is currently active. There is still a lot that I am trying to work out.
My next steps are as follows:
1. Make the text network something that depicts the varied contexts in which the word has been used throughout the decades, which may involve potentially incorporating bigrams or trigrams. This would involve;
  -  Create an x-axis with the set of decades between the chosen decades that depicts the variance in which the word has been used throughout the decades. Join
     together the various text networks by making the adjacency list a default dictonary that is double nested-, such that the adjacency list can contain     dictionaries with years as their key values (i.e. adjacencyList[chosen_word][1800][associated_word], in this case chosen_word is the word the user selected,1800 is the decade that we are looking at it from, and associated_word is the word that we found to be next to our chosen word that we are adding an edge to)
  -  Put these separate graphs side by side, and find a way to make associations between them, should they contain similar words (this means that the 
     dictionaries have to be able to create edges with one another).  
  - There are also lots of nodes, so I will cut out any that have a weight list that is less than 5.
2.  Refine the text pre-processing segment. 
4.  Make the text network more informative and insightful. This would involve;
  - Making the networks interactable and add hyperlinks to all the nodes, so that viewers can see the sources by using libraries like bokeh that support networkx, so it might be a matter of finding a way to conjoin the two.
  - Incorportating topic modelling to extract similar themes over the given decades.
4. We have yet to develop a front-end to all of this. Ideally, it can be made into a software, or can be made available to the public at some point, but it definetly still needs fine-tuning :)

Given all of that, the final currently looks like this (this is a zoom in of the graph, since its not legible when its zoomed out).
![Screen Shot 2021-12-16 at 9 30 53 PM](https://user-images.githubusercontent.com/76268134/146479265-25131b16-3df0-427c-8e21-084c9e267c5e.png)

Thank you!
