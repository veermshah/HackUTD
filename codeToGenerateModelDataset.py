import csv

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



#method to calculate dti ratio using fannieData.csv, return a floating point value
def calculate_dti_ratio(csv_file, target_id):
    # Initialize variables to store relevant information
    gross_monthly_income = None
    credit_card_payment = None
    car_payment = None
    student_loan_payments = None

    # Open the CSV file and search for the target ID
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
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
        return front_end_dti_ratio
    else:
        return None

def calculate_high_low_pmi_with_credit_score(csv_file):
    # Initialize variables to track the high and low PMI values
    high_pmi = float('-inf')  # Initialize with negative infinity as the minimum
    low_pmi = float('inf')  # Initialize with positive infinity as the maximum

    # Read the CSV file
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
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

input_file = 'fannieData.csv'
output_file = 'data.csv'
data = []

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.writer(outfile, delimiter=',')
    #writer.writeheader()
    next(reader) # Skip the first line of the CSV file cuz its bogus
    
    for row in reader:
        #data = []
        ltv = calculate_ltv_ratio(input_file, int(row['ID']))
        dti = calculate_dti_ratio(input_file, int(row['ID']))
        fedti = calculate_frontend_dti_ratio(input_file, int(row['ID']))
        
        if ltv < 80 and dti < 43 and fedti < 28:
            isTrue = 1
        else:
            isTrue = 0
            
        data = [ltv, dti, fedti, isTrue]
        writer.writerow(data)