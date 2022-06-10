from fpdf import FPDF
import csv

class PDF(FPDF):
    def set_title(self, name):
        self.set_font('Arial', 'B',size=15)
        self.cell(w=0,h=0,txt=name,align='C')
        self.ln(10)