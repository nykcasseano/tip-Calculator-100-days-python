#If the Bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60
print("Seja bem vindo ao programa: Calculadora de gorjeta!")

bill = float(input("Qual é o valor total da conta? $"))

#Porcentagem de preferência de gorjeta 10, 12 ou 15%
tip = int(input("Quanto deseja dar de gorjeta? 10, 12, ou 15? "))
people = int(input("Quantas pessoas vão dividir a conta?"))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")