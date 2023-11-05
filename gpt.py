import openai
import os
import csv
import config
import eligibilities

openai.api_key = config.openaiAPIKEY

def getFeedbackbyID(userID):

    with open('fannieData.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for item in range (userID):
            next(csvreader)
        row_i = next(csvreader)
        grossMonthlyIncome = row_i[1] 
        creditCardPayments = row_i[2]
        carPayments = row_i[3]
        studentLoanPayments = row_i[4]
        appraisedValue = row_i[5]
        downPayment = row_i[6]
        loanAmount = row_i[7]
        monthlyMortgagePayment = row_i[8]
        credit = row_i[9]

    ltv = eligibilities.calculate_ltv_ratio(appraisedValue, loanAmount)
    dti = eligibilities.calculate_dti_ratio(grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, monthlyMortgagePayment)
    fedti = eligibilities.calculate_frontend_dti_ratio(grossMonthlyIncome, monthlyMortgagePayment)
    creditScore = credit

    response = openai.Completion.create(
    model="curie:ft-personal-2023-11-05-03-07-22",
    prompt="Given the following data {" + str(ltv)+ ", " + str(dti) + ", " + str(fedti) + ", " + str(creditScore) + "}, what is the feedback you could give to ?",
    max_tokens=100,
    )
    return response.choices[0].text

print(getFeedbackbyID(1)) 