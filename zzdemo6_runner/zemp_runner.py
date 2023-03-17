from demo4_employee.employee_module import Employee


emp1=Employee()

emp1.set_company_code_p=45

print(emp1.get_company_code_p)


emp1.set_company_code(500)
print(emp1.get_company_code())