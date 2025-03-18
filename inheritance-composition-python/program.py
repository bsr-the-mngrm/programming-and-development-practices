# program.py
import hr

def main():
    # Create different types of employees
    salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
    hourly_employee = hr.HourlyEmployee(2, "Jane Doe", 40, 15)
    commission_employee = hr.CommissionEmployee(3, "Kevin Bacon", 1000, 250)

    # Create the payroll system and calculate payroll
    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll(
        [salary_employee, hourly_employee, commission_employee]
    )

if __name__ == "__main__":
    main()
