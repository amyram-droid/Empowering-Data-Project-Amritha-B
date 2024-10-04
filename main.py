
import pandas as pd 
import matplotlib.pyplot as plt
import GWCutilities as util
lwd=pd.read_csv("livwell175.csv")


countryBooleanList = lwd["country_name"] == "South Africa" 
countryData = lwd.loc[countryBooleanList] 
plt. scatter (x = "year", y = "ED_attainment_primary_p", data = countryData, color = "pink")


print("The South African Government considers education to be the highest domestic priority. Education recieves 5% of South Africa's GDP which is the greatest share of the government's spending.\n")
print("However, you may be shocked to discover that there has been a decline in the percentage of women with primary education.\n")

input("Press enter to continue.\n")

print("Our story will take place in a small rural village in South Africa. We will be following Ashanti, who is a bright 10 year old girl who loves going to school.\n")

print("Ashanti wakes up early everyday, excited to go to school. She has a thirst for knowledge, espcially concerning biology. She has dreams of becoming a doctor because she was inspired by a kind woman who runs the local clinic.\n")

input("Press enter to continue.\n")

print("She is surprised to learn that a lot of her friends have stopped coming to school. This worried her, because she dosen't understand why they are not here.\n")

print("When she asks her teacher, Ms.Adama, she gently explains there are many reasons why her friends are unable to come. Ashanti realizes that many of the issues are due to a lack of support.\n")

input("Press enter to continue.\n")

print("Many families in South Africa are unable to send girls to primary school because of poverty. Even in free public schools, there are many hidden costs. Girls from low-income families may be pressured to leave school to help the family. Additionaly, there may be safety concerns if girls have to walk a long distance to school.\n")

input("Press enter to continue.\n")

print("'What is the solution?', you may be wondering\n")

print("I would like to invest research funds into the following question:'To what extent do support programs targeting low-income families in South Africa increase the rate of women getting primary education?'\n")

print("I believe that providing support programs to these families will increase the rate of women getting primary education in South Africa")

input("To see visual proof of the decrease of women with primary education, press enter to continue.\n")

print("Thank you so much for watching my project!")


plt.title("Percent of Women with Primary Education") 
plt. xlabel("Year") 
plt. xlim(1998,2016) 
plt. ylim(0,100)
plt. ylabel("Women with Primary Education (%)") 
plt. show()
