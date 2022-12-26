from fpdf import FPDF
pdf=FPDF(orientation='P',unit='pt',format='A4')
pdf.add_page()

#Add contents
pdf.set_font(family='Times',size=24,style='B')
pdf.cell(w=0,h=80,txt="Flatmates Bill Report",border=1,align='C', ln=2)
pdf.cell(w=100,h=40,txt="Period: ",border=0)
pdf.cell(w=200,h=40,txt="December 2022",border=1)
pdf.output(name="Bill Report.pdf")