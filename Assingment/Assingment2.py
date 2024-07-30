salary = int(input("Your Salary: "))

def calculate_tax(salary):
    tax = 0
    if salary > 418400:
        tax += (salary - 418400) * 0.396
        salary = 418400
    if salary > 416700:
        tax += (salary - 416700) * 0.35
        salary = 416700
    if salary > 191650:
        tax += (salary - 191650) * 0.33
        salary = 191650
    if salary > 91900:
        tax += (salary - 91900) * 0.28
        salary = 91900
    if salary > 37950:
        tax += (salary - 37950) * 0.25
        salary = 37950
    if salary > 9325:
        tax += (salary - 9325) * 0.15
        salary = 9325
    if salary > 0:
        tax += salary * 0.10
    return tax

print(f"Total tax: {calculate_tax(salary):}")
