import csv

#method to calculate ltv ratio and return true if the value is less than 80% and false if not
def calculate_ltv_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    appraised_value = None
    down_payment = None
    loan_amount = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            if int(row['ID']) == target_id:
                gross_monthly_income = float(row['GrossMonthlyIncome'])
                appraised_value = float(row['AppraisedValue'])
                down_payment = float(row['DownPayment'])
                loan_amount = float(row['LoanAmount'])
                break

    # Check if the target ID was found
    if gross_monthly_income is not None and appraised_value is not None and down_payment is not None and loan_amount is not None:
        # Calculate the LTV ratio
        ltv_ratio = (loan_amount / appraised_value) * 100
        return ltv_ratio <= 80
    else:
        return None

#method to calculate dti ratio using fannieData.csv, return a floating point value
def calculate_dti_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    credit_card_payment = None
    car_payment = None
    student_loan_payments = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            if int(row['ID']) == target_id:
                gross_monthly_income = float(row['GrossMonthlyIncome'])
                credit_card_payment = float(row['CreditCardPayment'])
                car_payment = float(row['CarPayment'])
                student_loan_payments = float(row['StudentLoanPayments'])
                break

    # Check if the target ID was found
    if gross_monthly_income is not None and credit_card_payment is not None and car_payment is not None and student_loan_payments is not None:
        # Calculate the total monthly debt payments
        total_debt = credit_card_payment + car_payment + student_loan_payments
        
        # Calculate the DTI ratio
        dti_ratio = (total_debt / gross_monthly_income) * 100
        return dti_ratio
    else:
        return None

# method to calculate FEDTI ratio returns true if less than or equal to 28%, false otherwise
def calculate_frontend_dti_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    monthly_mortgage_payment = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
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
csv_file = 'your_csv_file.csv'
target_id = 1  # Replace with the desired ID
dti_result = calculate_dti_ratio(csv_file, target_id)

if dti_result is not None:
    print(f"DTI Ratio for ID {target_id}: {dti_result:.2f}%")
else:
    print(f"ID {target_id} not found in the CSV file.")


# Example usage of calculate_ltv_ratio:
csv_file = 'your_csv_file.csv'
target_id = 1  # Replace with the desired ID
ltv_result = calculate_ltv_ratio(csv_file, target_id)

if ltv_result is not None:
    if ltv_result:
        print(f"LTV Ratio for ID {target_id} is False (<= 80%).")
    else:
        print(f"LTV Ratio for ID {target_id} is True (> 80%).")
else:
    print(f"ID {target_id} not found in the CSV file.")
