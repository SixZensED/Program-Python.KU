class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, years):
        return self.principal * (1 + self.interest) ** years

    def __str__(self):
        return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest:.2%}"

insert_principal = float(input('Enter your money : '))
insert_interest_rate = float(input('Enter your rate : '))
insert_years = int(input("Enter your years : "))
investment = Investment(insert_principal, insert_interest_rate)

print(f"- {investment}\n- Value after {insert_years} years: ${investment.value_after(insert_years):.2f}")
