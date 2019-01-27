#Aayush Ghimire
#This program does the Sentiment Analysis
#it goves option for user to do different operation
#it also does a little bit of machine learning

#this is the concise summary of the program
#it calls the function and stores the return of the function
#it writes positive and negative word in the txt file
def main():
    file_final_value = (get_file())
    option = introduction()
    new_file = text_no_character(file_final_value)
    digit_count, senti_values = variable_count(file_final_value)
    final_value =values(digit_count,senti_values)
    write_positive = open("positives.txt","w")
    write_negative = open("negatives.txt","w")
    operation(option,final_value,digit_count,senti_values,
              write_positive,write_negative)

#this ask the user for the file final_value
#it prints out the five different option for the user
#it ask the user to chose one from the five option
#params:option is the parameter
#       final_value is the dictionary of the score / frequency
#       digit_count is the dictionary of frequency of the 
#       word in the txt file 
#       senti_values is the dictionary of score of the word in
#       the txt file
#       write_positive and write_negative writes the output to the txt file
#it gives four different option and performs accordingly
def operation(option,final_value,digit_count,senti_values,
              write_positive,write_negative):
    while option != "5":
        if option == "1":
            first_optn_operator(final_value)
            
        if option == "2":
            second_optn_operator(final_value,digit_count,senti_values)
            
        if option == "3":
            third_optn_operator(final_value,digit_count,senti_values)
            
        if option == "4":
            postive_list(final_value,write_positive,write_negative)

        print()    
        option = introduction()

#introduction part of the program
#return:the option is returned
def introduction():

    print("What would you like to do?")
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file")
    print("3: Find the highest / lowest scoring words in a file")
    print("4: Sort the words in a file into positive.txt and negative.txt")
    print("5: Exit the program")
    option = (input("Enter a number 1-5: "))
    return option


#prompts the user for the file final_value
#open the file and read each individual line
#return: the each individual file final_value
def get_file():
    file_final_value = input("Learning data file name? ")
    name = open(file_final_value)
    file_final_value = name.readlines()
    print()
    return file_final_value

#this creates the text file without any special character
#ord function is used to check the range of characters
#return:the new txt file without punctutation is created
#prams:the file is read and passed as a parameter
def text_no_character(file_final_value):
    for i in range(len(file_final_value)):
        text = ""
        words = file_final_value[i].lower()
        for j in range(0, len(words)):
            if( ord("a") <= ord(words[j]) <= ord("z") or words[j] == " " or
            words[j] == "\t" or words[j] == "\n" or
                ord("0") <= ord(words[j]) <= ord("9")):
                text += words[j]
        file_final_value[i] = text
        file_final_value[i] = file_final_value[i].split()
    return file_final_value
           
#this function counts the frequency of the words and stores in dictionary
#it also calculates the sentiment scores and stores in seperate dicitionary
#params:new file is the file without punctuation passed as a parameter
#return:two dictionaries digit_count and senti_count are returned
def variable_count(new_file):
    digit_count = {}
    senti_dict = {}
    for i in range(len(new_file)):
        for j in range(1,len(new_file[i])):
            if new_file[i][j] in digit_count:
                digit_count[new_file[i][j]] += 1
                senti_dict[new_file[i][j]] += int(new_file[i][0])
                
            else:
                digit_count[new_file[i][j]] = 1
                senti_dict[new_file[i][j]] = int(new_file[i][0])
    return digit_count, senti_dict


#calculates the final score
#gets the value from two dictionaries and gets the score divide by count
#params:digit_count is the dictionary passed
#       senti_dict is the dictionary passed
#return:the final value is the final value dictionary returned
def values(digit_count,senti_dict):
    final_value = {}
    for key_first,value_first  in digit_count.items():
        
        for key_second,value_second in senti_dict.items():
            
            if (key_first == key_second):
                result = (value_second) / (value_first)
                final_value[key_first] = float(result)
    return final_value

#this function prompts the new file from the user
#params:final_value, digit_count and senti_values are three dictionary passed
#lis is the new empty list created
#retruns:lis is the list of the words in the file and dictionaries
#        that is returned
#        the file is opened, read and returned 
def file_operation(final_value,digit_count,senti_values):
    file_Ask = input("file name? ")
    file = open(file_Ask).read()
    file_ask = text_no_character([file])
    lis = []
    for word in file_ask:
        for letter in word:
            if letter in final_value:
                lis.append(letter)
    return  lis, file

#this function is called when user prompt for the first option
#prams:final_Value dictionaries is passed as a parameter
def first_optn_operator(final_value):
    word_ask = input("Which word? ")
    if word_ask in final_value:
        print("score =",round(final_value[word_ask],2))
        if (final_value[word_ask]) > 2.01:
            print(word_ask, "is positive")
        elif (final_value[word_ask]) < 1.99:
            print(word_ask, "is negative")
        else:
            print(word_ask,"is neutral")

#this function is called when user prompts for second option
#prams:final_value, digit_count and senti_values are dictionary passed
#      passed as a parameter
def second_optn_operator(final_value,digit_count,senti_values):
    lis,file = file_operation(final_value,digit_count,senti_values)
    suma = 0
    for i in range(len(lis)):
        suma += final_value[lis[i]]
    average = suma
    if len(lis) > 0:
        average = suma / len(lis)
    
    print("score =",round(average,2))
    file = file.strip()
    print(file)       
    if average > 2.01:
        print(" is positive")
    elif average < 1.99:
        print(" is negative")
    else:
        print(" is neutral")
    right_wrong = input("Am I right (yes/no)? ")
    if right_wrong == "no":
        correct_score = int(input("What score should this sentence have "
                                   "(0 - 4 where 4 is the most positive)? "))
#       this for loop is used to update the value in the dictionary
        for i in range(len(lis)):
            digit_count[lis[i]] += 1
            senti_values[lis[i]] += correct_score
            final_value[lis[i]] = senti_values[lis[i]]/digit_count[lis[i]]

#this fucntion is called when user choose option 3
#prams:final_value,digit_count,senti_values are the ditionary
#      passed as a parameter 
def third_optn_operator(final_value,digit_count,senti_values):
    lis, file = file_operation(final_value,digit_count,senti_values)
    maxi = final_value[lis[0]]
    mini = final_value[lis[0]]
    maxstr = ""
    minstr = ""

    for i in range(len(lis)):
        if maxi < (final_value[lis[i]]):
            maxi = float(final_value[lis[i]])
            maxstr = lis[i]
        if mini > final_value[lis[i]]:
            mini = float(final_value[lis[i]])
            minstr = lis[i]
        
    print("Maximum score is",maxi,"for",maxstr)
    
    print("Minimum score is",mini,"for",minstr)

#this function determines whether the word is positive or not
#it writes to the two different files fo positive and negative
#params:final_value is the dictionary ppassed
#       write_positive is the fucntion which helps positive words
#       to write in file called postive.txt
#       write_negative is the fucntion which helps negative words
#       to write in file called negative.txt
def postive_list(final_value,write_positive,write_negative):
    for key,values in final_value.items():
        if values > 2.01:
            write_positive.write(key+"\n")
        elif values < 1.99:
            write_negative.write(key+"\n")





main()
