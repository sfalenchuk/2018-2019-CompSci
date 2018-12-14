# Partner 1:
# Partner 2:
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''

if grade == "A":
	print("good work")

''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
 
 if yards < 17:
 	yards = yards*2

 
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''

  if success == True:
  	print("Congrats!")
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''

 if word[1] == "f":
 	print("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''

if celsius == True:
   temp = 1.8*temp + 32
else:
   temp = temp

 
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
   
if numItems == 0:
   print("No items here, sir!")
 
else:
   averageCost = totalCost/numItems
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condpption eo
'''

if pollution < cutoff:
   print("You are safe.")
else:
   print("It's not safe out there!")


''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
 
if score < 60:
   grade = 'F'
elif 60 <= score <= 69:
   grade = 'D'
elif 70 <= score <= 79:
   grade = 'C'
elif 80 <= score <= 89:
   grade = 'B'
elif 90 <= score <= 100:
   grade = 'A'
 
''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
 
if letter > 0 or letter < 10
   print ("number")
elif letter isupper():
   print("Uppercase")
elif letter islower():
   print("Lowercase")
else:
   print("symbol")

''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
if neighbors == 0:
   print("You live in the middle of nowhere!")
if 1 >= neighbors > 25:
   print("You live in a rural area!")
if 25 >= neighbors > 50:
   print("You live in the suburbs!")
if neighbors >= 50:
   print("You live in the city!")
 
 
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't.
'''

if doesSignificantWork == True && if makesBreakthrough == True:
   nobelPrizeCandidate == True
else:
   nobelPrizeCandidate == False
 
 
 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''

if tax == True:
   taxrate = .0635
   price = price*taxRate
else:
   price = price
 
 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
 
if word[-2,-1] == ["l","y"]:
   type = adverb

elif word[-3,-2,-1] == ["i","n","g"]:
   type = gerund

elif word[-1] == ["s"]:
   type = plural
else:
   print("error")
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
if currentNumber%2 == 1:
   currentNumber = (3*currentNumber)+1
elif currentNumber%2 == 0:
   currentNumber = currentNumber//2
 
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''

if year%4 == 0:
   leapYear == True
else:
   leapYear == False
 
 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
 
 l = [a,b,c]

for i in l:
    if i < [a,b,c]:
        x = i

 
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
 
 if x%5 == 0 and x > -100 and x < 100:
   x = True
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
 
if letter == a or letter == e or letter == o or letter == u or letter == i:
   letter = 1
if letter == y:
   letter = -1
else:
   lette = 0
 
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
 
 if dayOfWeek == "saturday" or dayOfWeek == "sunday"
   dayOfWeek = True
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
 if month == [0,2,4,6,7, 9, 11]:
   numDays = 31
if month == [3,5,8,10]:
   numDays = 30
else:
   numDays = 28

 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
 if angle1 == True and angle2 == True and angle3 == True:
   validTriangle = True
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
 
   if units == 50:
      units = units*.5
   elif units <= 100:
      units = units*.75
   elif units <= 250:
      units = units*1.2
   else:
      units = units*1.5
      units=units*1.2
 
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
   if language == English:
      print("hello")
   if language == French:
      print("Bonjour")
 
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
   if choice == 5:
      PRINT("5"+noun+"s")

''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
 if userInput == "bacon":
   print("WHY DID YOU TYPE BACON?? WHYYYYYY!")
else:
   print("OH BOY!!! I loooooooove bacon!")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.