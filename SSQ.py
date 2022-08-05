import os , time

print('                       ==============================================================')
print('                       =                  Simple Science Quiz Game                  =')
print('                       ==============================================================')
print('                                                                     By Johny Bhiduri')
print('                                                                     ================')
F1 = input('Do you wanna play the game? : ')
if F1 != "yes"  :
    quit()
'''elif F1 != 'yes':
    quit()
elif F1 != "y":
    quit()
elif F1 != 'Y':
    quit()'''

q1 = input('   Q1. Brass gets discoloured in air because of the presence of which of the following gases in air?\n  a. Oxygen \n  b. Hydrogen sulphide\n  c. Carbon dioxide\n  d. Nitrogen\n   >>> ')

if q1 == 'b' :
    s1 = 1
    print('\n   Correct!\n\n')
elif q1 != "b":
    s1 = 0
    print('   Incorrect!, Right Answer is "b"\n\n')

q2 = input('   Q2. Which of the following is a non metal that remains liquid at room temperature?\n  a. Phosphorous\n  b. Bromine\n  c. Chlorine\n  d. Helium\n   >>> ')

if q2 == 'b' :
    s2 = 1
    print('\n   Correct!\n\n')
elif q2 != "b":
    s2 = 0
    print('   Incorrect!, Right Answer is "b"\n\n')

q3 = input('   Q3. Chlorophyll is a naturally occurring chelate compound in which central metal is\n  a. Iron\n  b.Copper\n  c. Magnesium\n  d. Calcium\n   >>> ')

if q3 == 'c':
    s3 = 1
    print('\n    Correct\n\n')
elif q3 !="c":
    s3 = 0
    print('   Incorrect!, Right Answer is "c"\n\n')

q4 = input('   Q4. Which of the following is used in pencils?\n  a. Graphite\n  b.Silicon\n  c. Charcoal\n  d. Phosphorous\n   >>> ')

if q4 == 'a':
    s4 = 1
    print('\n    Correct\n\n')
elif q4 !="a":
    s4 = 0
    print('   Incorrect!, Right Answer is "a"\n\n')

q5 = input('   Q5. Which of the following metals forms an amalgam with other metals?\n  a. Tin\n  b.Mercury\n  c. Lead\n  d. Zinc\n   >>> ')

if q5 == 'b':
    s5 = 1
    print('\n    Correct\n\n')
elif q5 !="b":
    s5 = 0
    print('   Incorrect!, Right Answer is "b"\n\n')

q6 = input('   Q6. Chemical formula for water is\n  a. NaAlO2\n  b. Al2O3\n  c. H2O\n  d. CaSiO3\n   >>> ')

if q6 == 'c':
    s6 = 1
    print('\n    Correct\n\n')
elif q6 !="c":
    s6 = 0
    print('   Incorrect!, Right Answer is "c"\n\n')

q7 = input('   Q7. The gas usually filled in the electric bulb is\n  a. Nitrogen\n  b. Hydrogen\n  c. Carbon dioxide\n  d. Oxygen\n   >>> ')

if q7 == 'a':
    s7 = 1
    print('\n    Correct\n\n')
elif q7 !="a":
    s7 = 0
    print('   Incorrect!, Right Answer is "a"\n\n')

q8 = input('   Q8. Washing soda is the common name for\n  a. Sodium carbonate\n  b. Calcium bicarbonate\n  c. Sodium bicarbonate\n  d. Calcium carbonate\n   >>> ')

if q8 == 'a':
    s8 = 1
    print('\n    Correct\n\n')
elif q8 !="a":
    s8 = 0
    print('   Incorrect!, Right Answer is "a"\n\n')

q9 = input('   Q9. Which of the gas is not known as green house gas?\n  a. Methane\n  b. Nitrous oxide\n  c. Carbon dioxide\n  d. Hydrogen\n   >>> ')

if q9 == 'd':
    s9 = 1
    print('\n    Correct\n\n')
elif q9 !="d":
    s9 = 0
    print('   Incorrect!, Right Answer is "d"\n\n')

q10 = input('      Q10. Bromine is a\n  a. Black solid\n  b. Red liquid\n  c. Colourless gas\n  d. Highly inflammable gas\n   >>> ')

if q10 == 'b':
    s10 = 1
    print('\n   Correct\n\n')
elif q10 !="b":
    s10 = 0
    print('   Incorrect!, Right Answer is "b"\n\n')

TotalScore = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10
if TotalScore == 10 :
    print(f"\n\n   Your Score is {TotalScore}/10 , Excellent!!")
elif TotalScore > 5 :
    print(f"\n\n   Your Score is {TotalScore}/10 , Keep It Up!")
elif TotalScore < 5 :
    print(f'\n\n   Your Score is {TotalScore}/10 , Need More Practice!')


 
input('\n\n\n\n       ===========================>   Press ENTER to restart! <===========================')
while 1:
    os.system("SSQ.py")
    print("Restarting...")
    time.sleep(0.2)

      
    
