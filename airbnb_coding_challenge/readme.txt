
Airbnb Coding Challenge: Find cheap places to stay

IMPORTANT: THE BEST APPROACH TO THIS TASK IS TO BUILD A SIMPLE WORKING SOLUTION, AND THEN TO WRITE A THOUGHTFUL ANALYSIS OF HOW IT COULD BE IMPROVED.  

You will be provided with availability and pricing data for a set of rental properties.  Your program will determine the cheapest properties for a given date range in a specific geographic area.

INPUT:
You will be provided with three CSV files of data, with columns as described below:

properties.csv 
property_id - an integer
lat - a float
lng - a float
nightly_price - the standard nightly price; an integer

calendar.csv - This file specifies dates when properties are unavailable, or when the nightly pricing differs from the standard nightly price.  If not specified here, the property is available at the standard nightly price. 
date - a date in the format YYYY-MM-DD
availability - 0 if the property is unavailable, 1 if the property is available
price - price for the night

searches.csv - each row is a separate search. 
search_id - an identifier for this search; an integer
lat - 
lng - 
checkin - a date in the format YYYY-MM-DD
checkout - a date in the format YYYY-MM-DD

OUTPUT:
Your program should return the 10 cheapest, nearby properties for that date range (There may be fewer/no results).  For the geographic filter, use a bounding box that is 2 degrees square in total (ie, +/- 1.0 degrees from each coordinate).  If a property is unavailable for any date during the range, it is not a valid result.  If a property has a variable price specified during the range, that variable price overrides the base nightly price.  The total price is the sum of the nightly prices for the entire stay.  The program should return the cheapest available properties, in order, up to a max of 10.  

Note that properties do not need to be available on the checkout date itself, just on the day before.

Your program should produce a file called search_results.csv.  Each row is a result for one of the given searches.  A search with 10 valid results corresponds to 10 rows.
search_id - integer
rank - integer
property_id
total_price - the total price for the stay

EVALUATION:
Correctness - the program should generate the correct output, and you MUST include this output file in your email submission
Efficiency - is the implementation efficient?  will it scale to large data sets and to large numbers of searches?
Clarity - is the code well-organized and clear?
Prioritization - if the program is incomplete, did you prioritize appropriately?
NOTES AND ANALYSIS - you should include an analysis of the problem and your approach.  What other approaches did you consider?   What parts of your program are inefficient?  What changes could you make to have a better solution?  How does the optimal solution depend on the distribution of the data?

RECOMMENDED APPROACH:

IMPORTANT: The best approach is to get some sort of working solution, even if it is a simple and brute force approach.  This can be accompanied by a thoughtful written analysis.  Do not make the mistake of trying to build a complex system, and then leaving it incomplete.

Your program should first process the input files and store the property and calendar data in memory, using data structures that will be useful for performing the searches.  Then perform each search and write the results to file.

You may use any language you like.  Using a high-level scripting language will probably allow the most rapid progress.  You will not be judged on the raw speed of the program (ie no need to use raw C), but rather on the efficiency of the approach and the elegance of the implementation. 

You should not use a database or any kind of search engine.  You may make use of existing code, whether written by you or someone else. For example, you can use snippets of code that implement basic searching or sorting algorithms. However this is not necessary, and if you do so then indicate as such.

You have 3 hours to provide a response.  Please take at least a half hour to think through the problem and to write up an analysis of your solution.  

AGAIN, THE BEST APPROACH TO THIS TASK IS TO BUILD A SIMPLE WORKING SOLUTION, AND THEN TO WRITE A THOUGHTFUL ANALYSIS OF HOW IT COULD BE IMPROVED.  


