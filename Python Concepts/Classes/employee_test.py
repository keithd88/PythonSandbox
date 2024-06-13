from employee import Employee

def create_employee():
    print("Employee is starting their job...")
    employee1 = Employee()
    employee1.name = "Blake"
    employee1.working(employee1.name)
    employee1.is_on_vacation = False

    return employee1

employee = create_employee()

print(f"Employee vacation: {employee.is_on_vacation}")