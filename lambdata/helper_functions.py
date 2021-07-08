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
    
    def rm_outlier(self, df):
        """ Method to remove dataframe rows with outliers > 1.5*IQR """
        
        iqr = pd.np.quantile(df, 0.75) - pd.np.quantile(df, 0.25)
        
        # Create new DF with Bool values where True values are any outlier
        # values in original DF (larger than 1.5*IQR)
        df1 = df.iloc[:, :].gt(1.5*iqr)

        for i in range(0, len(df1)):
            # Loop through new DF and drop any rows from original DF
            # where there is True value on the same row number in new DF
            if df1.iloc[i,:].any() == True:
                df.drop(i, axis = 0, inplace=True)
        
        return df

    def list_2_series(self, list_2_series, df):
        """
        Convert a list to series, then add that series as the last column
        of an existing dataframe.
        """
        s1 = pd.Series(data=list_2_series)

        df.insert(len(df.columns), 'list', s1) # Add series as DF last column

        return df
