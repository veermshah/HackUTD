import csv

def getCreditscore(csv_file, target_id):
    # Initialize variables to store relevant information
    credit_score = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                credit_score = int(row['CreditScore'])
                break

    # Check if the target ID was found
    if credit_score is not None:
        return credit_score
    else:
        return None

#method to calculate ltv ratio and return true if the value is less than 80% and false if not
def calculate_ltv_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    appraised_value = None
    down_payment = None
    loan_amount = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                appraised_value = float(row['AppraisedValue'])
                down_payment = float(row['DownPayment'])
                loan_amount = float(row['LoanAmount'])
                break

    # Check if the target ID was found
    if appraised_value is not None and down_payment is not None and loan_amount is not None:
        # Calculate the LTV ratio
        ltv_ratio = (loan_amount / appraised_value) * 100
        return ltv_ratio
    else:
        return None

def calculate_ltv_ratio(appraised_value, down_payment, loan_amount):
    # Calculate the LTV ratio
    ltv_ratio = (loan_amount / appraised_value) * 100
    return ltv_ratio


#method to calculate dti ratio using fannieData.csv, return a floating point value
def calculate_dti_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    credit_card_payment = None
    car_payment = None
    student_loan_payments = None
    MonthlyMortgagePayment = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                gross_monthly_income = float(row['GrossMonthlyIncome'])
                credit_card_payment = float(row['CreditCardPayment'])
                car_payment = float(row['CarPayment'])
                student_loan_payments = float(row['StudentLoanPayments'])
                MonthlyMortgagePayment = float(row['MonthlyMortgagePayment'])
                break

    # Check if the target ID was found
    if gross_monthly_income is not None and credit_card_payment is not None and car_payment is not None and student_loan_payments is not None:
        # Calculate the total monthly debt payments
        total_debt = credit_card_payment + car_payment + student_loan_payments+MonthlyMortgagePayment
        
        # Calculate the DTI ratio
        dti_ratio = (total_debt / gross_monthly_income) * 100
        return dti_ratio
    else:
        return None

def calculate_dti_ratio(gross_monthly_income, credit_card_payment, car_payment, student_loan_payments, MonthlyMortgagePayment):
    # Calculate the total monthly debt payments
    total_debt = credit_card_payment + car_payment + student_loan_payments+MonthlyMortgagePayment
        
    # Calculate the DTI ratio
    dti_ratio = (total_debt / gross_monthly_income) * 100
    return dti_ratio

# method to calculate FEDTI ratio returns true if less than or equal to 28%, false otherwise
def calculate_frontend_dti_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    monthly_mortgage_payment = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                gross_monthly_income = float(row['GrossMonthlyIncome'])
                monthly_mortgage_payment = float(row['MonthlyMortgagePayment'])
                break

    # Check if the target ID was found
    if gross_monthly_income is not None and monthly_mortgage_payment is not None:
        # Calculate the front-end DTI ratio
        front_end_dti_ratio = (monthly_mortgage_payment / gross_monthly_income) * 100
        return front_end_dti_ratio <= 28
    else:
        return None

import csv

def calculate_frontend_dti_ratio(gross_monthly_income, monthly_mortgage_payment):
    # Calculate the front-end DTI ratio
    front_end_dti_ratio = (monthly_mortgage_payment / gross_monthly_income) * 100
    return front_end_dti_ratio <= 28

def calculate_high_low_pmi_with_credit_score(csv_file, target_id):
    # Initialize variables to track the high and low PMI values
    high_pmi = float('-inf')  # Initialize with negative infinity as the minimum
    low_pmi = float('inf')  # Initialize with positive infinity as the maximum

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                # Extract the relevant data from the CSV row
                loan_amount = float(row['LoanAmount'])
                appraised_value = float(row['AppraisedValue'])
                down_payment = float(row['DownPayment'])
                credit_score = int(row['CreditScore'])

                # Calculate the Loan-to-Value (LTV) ratio
                ltv = (loan_amount / appraised_value) * 100

                # Determine the PMI rate based on credit score
                if credit_score >= 740:
                    pmi_rate = 0.005  # Example: Excellent credit score
                else:
                    pmi_rate = 0.02  # Example: Bad credit score

                # Calculate PMI
                pmi = (ltv - 80) / 100 * (loan_amount * pmi_rate / 12)
                
                # Update the high and low PMI values if necessary
                high_pmi = max(high_pmi, pmi)
                low_pmi = min(low_pmi, pmi)

    # Return the high and low PMI values
    return high_pmi, low_pmi

def calculate_high_low_pmi_with_credit_score(loan_amount, appraised_value, down_payment, credit_score):
    # Calculate the Loan-to-Value (LTV) ratio
    ltv = (loan_amount / appraised_value) * 100

    # Determine the PMI rate based on credit score
    if credit_score >= 740:
        pmi_rate = 0.005  # Example: Excellent credit score
    else:
        pmi_rate = 0.02  # Example: Bad credit score

    # Calculate PMI
    pmi = (ltv - 80) / 100 * (loan_amount * pmi_rate / 12)

    # Return the PMI value
    return pmi

def possibleAppraisedHousePrice(csv_file, target_id):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ID']) == target_id:
                down_payment = float(row['DownPayment'])
                return down_payment*5
            return None
            
def possibleAppraisedHousePrice(down_payment):
    return down_payment*5
            


def meetsCriteria(csv_file, target_id):
    # Get the credit score
    credit = getCreditscore(csv_file, target_id)

    # Calculate the LTV ratio
    ltv_ratio = calculate_ltv_ratio(csv_file, target_id)

    # Calculate the DTI ratio
    dti_ratio = calculate_dti_ratio(csv_file, target_id)

    # Calculate the front-end DTI ratio
    frontend_dti_ratio = calculate_frontend_dti_ratio(csv_file, target_id)

    # Check if the credit score is greater than or equal to 640
    if credit >= 640:
        # Check if the LTV ratio is less than or equal to 80%
        if ltv_ratio <= 80:
            # Check if the DTI ratio is less than or equal to 43%
            if dti_ratio <= 43:
                # Check if the front-end DTI ratio is less than or equal to 28%
                if frontend_dti_ratio <= 28:
                    # Return True if all criteria are met
                    return True
                else:
                    # Return False if the front-end DTI ratio is greater than 28%
                    return False
            else:
                # Return False if the DTI ratio is greater than 36%
                return False
        else:

            # Return False if the LTV ratio is greater than 80%
            return False
    else:
        # Do not show new listing, ONLY give recommendations/feedback to improve their credit score/other factors
        return False

# Example usage of pmi_calclulator: (PMI calculator is only to be used if LTV ratio is >80%)
csv_file = 'fannieData.csv'
high_pmi, low_pmi = calculate_high_low_pmi_with_credit_score(csv_file)

# Print the high and low PMI values
print(f"High PMI: ${high_pmi:.2f}")
print(f"Low PMI: ${low_pmi:.2f}")


# Example usage of calculate_frontend_dti_ratio:
csv_file = 'fannieData.csv'
target_id = 1  # Replace with the desired ID
frontend_dti_result = calculate_frontend_dti_ratio(csv_file, target_id)

if frontend_dti_result is not None:
    if frontend_dti_result:
        print(f"Front-end DTI Ratio for ID {target_id} is True (<= 28%).")
    else:
        print(f"Front-end DTI Ratio for ID {target_id} is False (> 28%).")
else:
    print(f"ID {target_id} not found in the CSV file.")



# Example usage of calculate dti ratio:
csv_file = 'fannieData.csv'
target_id = 1  # Replace with the desired ID
dti_result = calculate_dti_ratio(csv_file, target_id)

if dti_result is not None:
    print(f"DTI Ratio for ID {target_id}: {dti_result:.2f}%")
else:
    print(f"ID {target_id} not found in the CSV file.")

# Example usage of ltv_ratio:
csv_file = 'fannieData.csv'
target_id = 1  # Replace with the desired ID
ltv_result = calculate_ltv_ratio(csv_file, target_id)

if ltv_result is not None:
    print(f"LTV Ratio for ID {target_id}: {ltv_result:.2f}%")
else:
    print(f"ID {target_id} not found in the CSV file.")
