import openai
import os
import csv
import login

openai.api_key = "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"

def getFeedbackbyID(userID):

    with open('fannieData.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for item in range (userID-1):
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

    response = openai.Completion.create(
    model="curie:ft-personal-2023-11-05-03-07-22",
    prompt="My gross monthly income is " + grossMonthlyIncome + ". My credit card payments are " + creditCardPayments + ". My car payments are " + carPayments + ". My student loan payments are " + studentLoanPayments + ". The appraised value of the home is " + appraisedValue + ". The down payment is " + downPayment + ". The loan amount is " + loanAmount + ". The monthly mortgage payment is " + monthlyMortgagePayment + ". My credit score is " + credit + ". Which of these values is too high/low and how can I be a better candidate for a loan?",
    max_tokens=200,
    )

    return response.choices[0].text