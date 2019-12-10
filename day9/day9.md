A couple of notes on operations you should try to avoid if targeting efficiency (nothing new for who has been following these threads):
* enumerate lists instead of looping with for or while
* use get to retrieve elements from a list (unless you need a default value)
* append spaces for each iteration instead of using the join function