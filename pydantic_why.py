
def insert_patient_data(name, age):

    
    print(name)
    print(age)

    #Demo code say 
    print("Inserted into database")


insert_patient_data("John Doe", "thirty") #now here comes the need for type checking 
#the actual value thirty will be stored as a string in the database 

#one solution (name:str, age:int) also known as type hinting
#but type hinting is not enforced at runtime
#it doesn't raise an error if the type is not correct

#another solution 

#if type(name)== str:
    #insert into database
#else: 
#    raise TypeError("Type doesnt match")

#this is not a good solution because it requires manual checking and is not scalable
#similar case occur for ValueError, some might enter negative age or age as a string
