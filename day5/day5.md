The solutions are very similar, so I leave just a couple of notes here:
if you are targeting efficiency over readability or maintainability, try to avoid functions that require you to go over the full list many times, like the min()
Indexing a dictionary with brackets ([]) looks faster than using the .get method
If you are looping through a dictionary, it looks faster to use the .keys() method - write "for key in dict.keys()" instead of "for tuple in dict" (although both work fine)