class CleaningData:
    """
    Class containing methods for identifying number of NaN values 
    and splitting date entries in separate columns for month, day, and year.
    """
    def __init__(self):
        return
        
    def null_count(self, df):
        """ Check dataframe for NaNs and return the number of missing values. """
    
        x, y = df.shape
        all_count = x*y
        non_null_count = df.count().sum()
    
        return all_count - non_null_count

    def split_dates(self, date_series):
        """
        Method to split dates of format "MM/DD/YYYY" into multiple columns 
        (df['month'], df['day'], df['year']) and then return the 
        same dataframe with those additional columns.
        """

        df = date_series.str.split(pat='/', expand=True)
        df = df.rename(columns={0:'month', 1:'day', 2:'year'})

        return df