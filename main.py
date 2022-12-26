import webbrowser

from fpdf import FPDF
"""
This App takes in input of an amount which is bill for a particular period of time.
By taking into account the duration each of the flatmates have stayed in the flat in that particular time period,
the portion of the bill flatmate has to pay is calculated
Also generates a pdf report of the flatmates name and share he has to pay
"""

class Bill:
    """
    This class deals with details of the bill like amount in the bill and
    period of time to which bill amount is associated
    """
    def __init__(self,amount,period):
        self.period = period
        self.amount = amount
        
class Flatmate:
    """
    This class deals with the details of the flatmate. Flatmate is identified by the name and
    days he have spent in the flat
    """
    def __init__(self,name,days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    """
    Logic- no of days / sum of number of days of both flatmates gives a coefficient
    Multiply the amount by the coefficient
    eg- 120 is the amount to be split
    John stays in flat for 20 days and James stays for 25 days
    John has to pay =>
    -> 20/20+25  =  0.44 which is the coefficiant
    -> 120 * 0.44 = 52.8 is the amount John has to pay 
    """
    def pays(self,bill,flatmate2):
        weight= self.days_in_flat/(self.days_in_flat+ flatmate2.days_in_flat)
        to_pay=bill.amount*weight
        return to_pay

class PDFReport:
    """
    This class deals with generation of PDF report of amount each flatmate has to pay
    """

    def __init__(self,filename):
        self.filename = filename

    def generate(self, flatmate1,flatmate2,bill):

        flatmate1_pays=str(round(flatmate1.pays(bill=bill,flatmate2=flatmate2),2))
        flatmate2_pays=str(round(flatmate2.pays(bill=bill,flatmate2=flatmate1),2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Heading
        pdf.set_font(family='Times', size=24, style='B')
        pdf.image("house.jpg",w=30,h=30)
        pdf.cell(w=0, h=80, txt="Flatmates Bill Report", border=1, align='C', ln=2)

        # Add Period of the bill
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0,ln=1)

        pdf.set_font(family='Times', size=18, style='B')
        # Add amount of flatmate 1
        pdf.cell(w=100, h=30, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=30, txt=flatmate1_pays, border=0,ln=1)

        # Add amount of flatmate 2
        pdf.cell(w=100, h=30, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=30, txt=flatmate2_pays, border=0)


        pdf.output(name=self.filename)
        webbrowser.open(self.filename)



amount= float(input("Enter the bill amount: "))
period= input("Enter the period of the bill: ")
flatmate1= input("Enter the name of flatmate 1: ")
days_in_flat_1= float(input(f"Enter the days {flatmate1} spent in flat: "))
flatmate2= input("Enter the name of flatmate 2: ")
days_in_flat_2= float(input(f"Enter the days {flatmate2} spent in flat: "))
bill= Bill(amount=amount,period=period)
f1=Flatmate(name=flatmate1,days_in_flat=days_in_flat_1)
f2=Flatmate(name=flatmate2,days_in_flat=days_in_flat_2)
print(f"{flatmate1} pays : {f1.pays(bill=bill,flatmate2=f2)}")
print(f"{flatmate2} pays: {f2.pays(bill=bill,flatmate2=f1)}")

pdf=PDFReport(f"Flat Bill {period}.pdf")
pdf.generate(f1,f2,bill)


        
        
        