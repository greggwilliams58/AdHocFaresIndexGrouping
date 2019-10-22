from sharedfunctions import exportfile
import pandas as pd


def main():
     # Testing to commit
    #additional test
    #test change to demonstrate github functionality
    #variables holding the location and name of the superfile, as well as the location where the result is sent to 
    superfilelocation = 'C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\FaresIndexSourceData\\advanced_and_non_advanced_output\\'
    superfilename = 'superfile without regulated steps_20190430_14-18.csv'
    outputto = 'C:\\Users\\gwilliams\\Desktop\\Python Experiments\\work projects\\FaresIndexSourceData\\advanced_and_non_advanced_output\\adv_non_advanced_and_superfile\\'
   
    #reading in the data from the csv file and converting into appropriate datatypes
    print("getting superfile for weights")
    rawsuperfile = pd.read_csv(superfilelocation + superfilename,
                               dtype={'Carrier TOC / Third Party Code':'category','Origin Code':'category','Destination Code':'category','Route Code':'category', 'Regulated_Status':'category',
                                      'Product Code':'category','Product Primary Code':'category','class':'category','sector':'category','ticket_type':'category','Category':'category'}
                               )



    #filtering the data by the field "Category" and the criteria category == season
    #print("now filtering the data\n")
    #superfilefiltered = rawsuperfile[rawsuperfile['Category']=='season']

    #printing out generic information about the filtered superfile
    print("information about the data\n")
    print(type(rawsuperfile))
    print(rawsuperfile.head(5))
    print(rawsuperfile.info())

    # the full superfile is being grouped by the fields sector and carrier TOC, with the fields Earings and journeys being summed
    print("now grouping and summing the data")
    
    #example grouping
    #['Carrier TOC / Third Party Code','Product Code','class','Regulated_Status','Category','sector']
    groupedsuperfile = rawsuperfile.groupby(['Regulated_Status'],observed=True)['Adjusted Earnings Amount','Operating Journeys'].agg('sum')
    
    #remove aggregations where earnings/journeys are null
    nonagroupedsuperfile = groupedsuperfile.dropna()

    #the filtered, grouped and summed data is then exported as a csv file using the imported module sharedfunctions
    exportfile(nonagroupedsuperfile,outputto, "Aggregated_Fares_Index_Superfile")


#standard boilerplate to point compiler to start point of program.
if __name__ == '__main__':
    main()