SQUA_RATE = 13.00
SWIM_RATE = 12.00
GYM_RATE = 11.00
WEI_RATE = 8.00

def amount_due(facility_code, hours):
    if facility_code == "squa":
        return SQUA_RATE * hours
    elif facility_code == "swim":
        return SWIM_RATE * hours
    elif facility_code == "gym":
        return GYM_RATE * hours
    elif facility_code == "wei":
        return WEI_RATE * hours
    else:
        print("please provide facility code and hours")

def Final_amount_due(amount):
    return amount* 1.14

def display(name, final_amount):
    print("Customer Name: ", name)
    print(f"Final Amount: R{final_amount:.2f}")

def process_payment():
    Name = input("Enter customer Name: ")
    Code = input("Enter customer Facility Code: ")
    Hours = float(input("Enter Number of hours: "))
    
    Amount_Due = amount_due(Code, Hours)
    Final_Amount = Final_amount_due(Amount_Due)
    display(Name, Final_Amount)
    
process_payment()  
    
