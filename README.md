# africana-web-crawler
A web crawler for the Africana project that sifts through sites searching for reputable primary and secondary sources.


###Basic Layout
The basic functionality of this crawler is as follows: 

(1) take user input for an initial url

(2) search through the source code for other urls, recursively

(3) return a registry containing all the urls found

###Reader Component
In addition to the basic funcitons above the crawler will be paired with a reader that will operate in the following five step process:

(1) Parse a text as input for reading (either through a search of its own or a manual user input).

(2) Parse the text appropriately

(3) Identify points of interest

(4) Summarize the text appropriately

(5) Store summary/analysis in a contextually appropriate manner
