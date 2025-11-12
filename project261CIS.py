import sys 
class QuitRequested(Exception):
    """Raised when the user confirms they want to quit using End."""  
    pass 

def prompt_yes_no(prompt):
    while True: 
       ans = input(prompt).strip().lower()
       if ans in ("y", "yes"):
           return True 
       if ans in ("n", "no"):
           return False
       print("Please enter 'y' or 'n'.")

def confirm_end():
    """Ask the user to confirm quitting. Raise QuitRequested if confirmed."""
    if prompt_yes_no("You entered 'End'. Do you want to quit? (y/n): "):
        raise QuitRequested()
    # if user cancels quit, return to caller normally
def check_end_and_confirm(value):
    """If value equals End (case-insensitive), confirm and possibly quit."""
    if isinstance(value, str) and value.strip().lower() == "end":
        confirm_end()
        
def input_with_end(prompt_text):
    """    Read input and treat 'End' (case-insensitive) as a quit request.    Returns the raw string (never None). If the user confirms quit, QuitRequested is raised.    """
    val = input(prompt_text)
    if val.strip().lower() == "end":
        confirm_end()
    return val
def input_name():
    """Prompt for employee name. 'End' will trigger quit confirmation."""
    while True:
        name = input_with_end("Enter employee name (or type End to finish): ").strip()
        if not name:
            print("Name cannot be blank.")
            continue
        return name
def input_total_hours():
    """Prompt for total hours worked. 'End' triggers quit confirmation."""
    while True:
        s = input_with_end("Enter total hours worked: ").strip()
        if not s:
            print("Hours cannot be blank.")
            continue
        try:
            hours = float(s)
        except ValueError:
            print("Please enter a valid number for hours.")
            continue
        if hours < 0:
            print("Hours must be zero or positive.")
            continue
        return hours
def input_hourly_rate():
     """Prompt for hourly rate. 'End' triggers quit confirmation."""
     while True:
         s = input_with_end("Enter hourly rate: ").strip()
         if not s:
             print("Rate cannot be blank.")
             continue
         try:
             rate = float(s)
         except ValueError:
             print("Please enter a valid number for hourly rate.")
             continue
         if rate < 0:
             print("Hourly rate must be zero or positive.")
             continue
         return rate

def input_tax_rate():
    """Prompt for income tax rate as percent. 'End' triggers quit confirmation."""
    while True:
        s = input_with_end("Enter income tax rate (percent, e.g. 15 for 15%): ").strip()
        if not s:
            print("Tax rate cannot be blank.")
            continue
        try:
             pct = float(s)
        except ValueError:
            print("Please enter a valid percentage for tax rate.")
            continue
        if pct < 0 or pct > 100:
            print("Tax rate must be between 0 and 100.")
            continue
        return pct / 100.0

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee(name, hours, rate, tax_rate, gross, tax_amt, net):
    print("-" * 60)
    print(f"Employee Name : {name}")
    print(f"Total Hours   : {hours:.2f}")
    print(f"Hourly Rate   : ${rate:.2f}")
    print(f"Gross Pay     : ${gross:.2f}")
    print(f"Tax Rate      : {tax_rate*100:.2f}%")
    print(f"Income Tax    : ${tax_amt:.2f}")
    print(f"Net Pay       : ${net:.2f}")
    print("-" * 60)
    
def display_totals(count, total_hours, total_gross, total_tax, total_net):
    print("\n" + "=" * 60)
    print("Summary Totals")
    print(f"Total employees processed : {count}")
    print(f"Total hours               : {total_hours:.2f}")
    print(f"Total gross pay           : ${total_gross:.2f}")
    print(f"Total tax                 : ${total_tax:.2f}")
    print(f"Total net pay             : ${total_net:.2f}")
    print("=" * 60)
    
def main():
    print("Simple Payroll Processor (type End to request quit at any prompt)\n")
    total_employees = 0
    total_hours = 0.0
    total_gross = 0.0
    total_tax = 0.0
    total_net = 0.0
    try:
        while True:
            name = input_name()          # 'End' here triggers confirm_end
            # If user supplied "End" and then canceled quit, flow continues.
            if name.strip().lower() == "end":
                # confirm_end already handled quitting; this line is defensive.
                continue
            hours = input_total_hours() # all input_* functions handle 'End'
            rate = input_hourly_rate()
            tax_rate = input_tax_rate()
            gross, tax_amt, net = calculate_pay(hours, rate, tax_rate)
            display_employee(name, hours, rate, tax_rate, gross, tax_amt, net)
            total_employees += 1
            total_hours += hours
            total_gross += gross
            total_tax += tax_amt
            total_net += net
            
    except QuitRequested:
        print("\nQuit confirmed by user. Showing totals so far.")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Showing totals so far.")
    finally:
        display_totals(total_employees, total_hours, total_gross, total_tax, total_net)
        # Exit cleanly
        sys.exit(0)
        
if __name__ == "__main__":
    main()