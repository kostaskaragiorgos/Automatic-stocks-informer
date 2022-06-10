from fpdf import FPDF
import csv

class PDF(FPDF):
    def set_title(self, name):
        self.set_font('Arial', 'B',size=15)
        self.cell(w=0,h=0,txt=name,align='C')
        self.ln(10)
    
    def add_text(self, text):
        self.set_font('Arial',size=10)
        self.write(5,text)
        self.ln(10)
    
    def add_image(self, image_name):
        self.image(image_name)
        self.ln(10)
    