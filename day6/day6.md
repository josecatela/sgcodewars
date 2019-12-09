This is a very difficult one to analyze due to the fact that it has 2 input parameters. It has a great impact whether you have lots of customers or lots of checkout tills or both. Many combinations of parameters should be tested before getting a reliable result, this is what is called a linear optimization problem.
Almost everyone took the approach of adding the next customer in the queue to the smallest checkout line, so most of the results revolve around the same values.
A couple of notes on operations that increased the running time:
looping over a list more than once
removing elements from a list with "pop(0)"
adding/appending elements to a list
there is a contradiction between something I indicated before as being a bad approach for performance and the fastest solution. Can you see which and why it changes in this case?