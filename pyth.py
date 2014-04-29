File_1 = open("sampleData.txt", "rt")


#This function reads the file and takes out the "YES" or "NO" from any line with 'Complete' in it


def get_entries( file ):
    ##open the file and read it
    for line in file:
        if "Complete" in line:
            complete, answer = line.split(':')
            yield answer.strip() 



#Build a list of "YES" or "NO" as they appear
MyList=list(get_entries( file ))


##Pull out names from the file...Not pretty, I am new to python
def get_names( file ):
    for line in file_2:
        if ':', 'Chapter','UserDone' not in line:
            name=line
            yield name.strip()

#Build a list of Names
MyList2=list(get_names( file ))

#Build a dict of Names and the corresponding values of their 'Complete' variables
Database={x: MyList[6*i:6*(i+1)] for i,x in enumerate(MyList2)}


#Final Function takes a student name as input and tells you if they passed
def check_student():
    A=raw_input("Enter student name as it appears in file: ")
    if A not in Database:
        print "Invalid Name"
    if Database[A].count("YES")==6:
        print "This student has passed"
    else:
        print "This student does not pass"


check_student()
    
    
    

    






