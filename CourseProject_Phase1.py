#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetHoursWorked():
    hours = float(input('hours: '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input('hourlyrate: '))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input('taxrate: '))
    return taxrate




def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    print("hourlyrate: ", f"{hourlyrate:,.2f}")
    print("grosspay: ", f"{grosspay:,.2f}")
    print("taxrate: ", f"{taxrate:,.2f}%")
    print("incometax: ", f"{incometax:,.2f}")
    print("netpay: ", f"{netpay:,.2f}")
    
    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):   
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"TotGrossPay: {TotGrossPay:,.2f}")
    print(f"TotTax; {TotTax:,.2f}")
    print(f"TotNetPay: {TotNetPay:,.2f}")


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked() 
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)

