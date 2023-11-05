import openai
import os
import csv

openai.api_key = "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"

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

    #ltv = eligibilities.calculate_ltv_ratio(appraisedValue, loanAmount)
    #dti = eligibilities.calculate_dti_ratio(grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, monthlyMortgagePayment)
    #fedti = eligibilities.calculate_frontend_dti_ratio(grossMonthlyIncome, monthlyMortgagePayment)
    #creditScore = credit

    response = openai.Completion.create(
    model="curie:ft-personal-2023-11-05-03-07-22",
    prompt="My gross monthly income is " + grossMonthlyIncome + ". My credit card payments are " + creditCardPayments + ". My car payments are " + carPayments + ". My student loan payments are " + studentLoanPayments + ". The appraised value of the home is " + appraisedValue + ". The down payment is " + downPayment + ". The loan amount is " + loanAmount + ". The monthly mortgage payment is " + monthlyMortgagePayment + ". My credit score is " + credit + ". Which of these values is too high/low and how can I be a better candidate for a loan?",
    max_tokens=200,
    )
    
    return response.choices[0].text