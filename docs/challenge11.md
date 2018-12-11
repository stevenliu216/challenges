# Challenge 11
Birds of a feather

A new week, more coding! In Part 2 of our Twitter data analysis we challenge you to find out how similar two tweeters
are ...

Challenge
Make a script that receives two command line args: `user1` and `user2`

`$ similar_tweeters.py bbelderbos pybites`

Get the last n tweets of these users. You can use the code from challenge 10. To get the algorithm to perform for this
challenge, use [yanofsky's tweet dumper](https://gist.github.com/yanofsky/5436496) to get 3200 tweets per user, instead
of the 200 we had for the last challenge.

Tokenize the words in the tweets, filtering out stop words, URLs, digits, punctuation, words that only occur once or are
less than 3 characters (and/or other noise ...)

Extract the main subjects the users tweet about. You could use [Gensim](https://radimrehurek.com/gensim/),
an NLP package for Topic Modeling.

Compare the subjects and come up with a similarity score.

### Function prototype
    def similar_tweeters(user1, user2):
        pass


### Example
##### Sample Input
    paugasol
 
##### Sample Output
    jsonmez 0.739746
    Schwarzenegger 0.739746
    tferriss 0.739746
    cine_tv_es 0.631373
    gvanrossum 0.631373

##### Explanation
paugasol is a twitter user. Gensim used Latent Semantic Indexing (LSI) to compare how similar this user's tweets
were to other users. Twitter user jsonmez had the highest similarity score.