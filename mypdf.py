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
    
    def add_csvfile(self, csv_file_name):
        page_width = self.w - 2 * pdf.l_margin
        col_width = page_width/4
        th = 14
        with open(csv_file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                for i in range(len(row)):
                    self.cell(col_width, th, row[i], border=1)
                self.ln(th)
            self.ln(10)