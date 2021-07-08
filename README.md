# Lambdata-IM

Helper functions from LS Unit 3 Sprint 1

What is it?

A class for cleaning tabular data using methods derived from Pandas and Numpy.

Main Features

A method to check a dataframe for NaNs and return the number of missing values.
A method to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) and then return the same dataframe with those additional columns.
A method to remove dataframe rows with outliers > 1.5*IQR
A method to convert a list to series, then add that series as the last column of an existing dataframe. 

Where to get it

The source code is currently hosted on GitHub at https://github.com/ivan-mihailov/Lambdata-IM

License

Apache License, Version 2.0