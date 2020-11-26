# AdHocFaresIndexGrouping
This is a toy example of using group and sum within Pandas.  It reads in data from an excel file, shows summary data to the console and outputs the data summed by various sub-categories as a csv file.  It was used in training sessions at ORR.

# Installation
This was written in Visual Studio, so needs VS to open the .sln file.

# Usage
This is used for training and demonstrations.  To change the grouping for other data files. The key line is `groupedsuperfile = rawsuperfile.groupby(['Regulated_Status'],observed=True)['Adjusted Earnings Amount','Operating Journeys'].agg('sum')`
