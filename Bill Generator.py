import os
from fpdf import FPDF
from fpdf.enums import XPos
from fpdf.enums import YPos

def text_to_pdf(li,title,tcost,dto):
    try:
        custom=(130,400)
        pdf=FPDF(unit='mm',format=custom)
        pdf.set_auto_page_break(auto=True, margin=20)
        pdf.add_page()
        pdf.set_font("Helvetica", 'B', 18)
        pdf.cell(w=0,h=8,text=title,border=0,align='C',new_x=XPos.LMARGIN, new_y=YPos.NEXT )
        pdf.ln(8)
        pdf.set_font("Helvetica", 'B', 15)
        a="BILL DETAILS"
        wide=pdf.w - pdf.l_margin - pdf.r_margin
        pdf.set_dash_pattern(1,1)
        x=pdf.get_x()
        y=pdf.get_y()
        pdf.line(x,y,x+wide,y)
        pdf.ln(1)
        pdf.set_font("Helvetica", size=15)
        pdf.cell(w=0,h=7,text=a,border=0,align='C',new_x=XPos.LMARGIN, new_y=YPos.NEXT )
        pdf.ln(1)
        x=pdf.get_x()
        y=pdf.get_y()
        pdf.line(x,y,x+wide,y)
        pdf.ln(4)
        pdf.set_dash_pattern()
        pdf.set_line_width(0.3)
        pdf.set_font("Helvetica", size=12)
        pdf.cell(40, 5, "Product Name", border=1)
        pdf.cell(20, 5, "Price", border=1)
        pdf.cell(20, 5, "Quantity", border=1)
        pdf.cell(30, 5, "Total Price", border=1)
        pdf.ln()
        for i in li:
            pdf.cell(40, 5, i['Product Name'], border=1)
            pdf.cell(20, 5, str(i['Price']), border=1)
            pdf.cell(20, 5, str(i['Quantity']), border=1)
            pdf.cell(30, 5, str(i['Total Price']), border=1)
            pdf.ln()
        pdf.ln(5)
        
        pdf.cell(w=0,h=8,text=tcost,border=0,align='R',new_x=XPos.LMARGIN, new_y=YPos.NEXT )
        pdf.ln()
        pdf.output(dto)
        print("[SUCCESS]BILL is successfully created",dto)
    except Exception as e:
        print("ERROR ,Check the details filled",e)


def basic(dto,title):
    wide=75
    a="Bill Details".center(wide)
    bill=("-"*wide)+"\n"+a+"\n"+("-"*wide)
    print("Enter your bill details")
    li=[]
    c=0
    while True:
        a=str(input("ADD items press Y \nDont want to add items press R \nEnter :")).upper()
        if a=='Y':
            try:
                p=str(input("Product Name :"))
                pri=float(input("Price in Rs. :"))
                q=int(input("Quantity :"))
                item={'Product Name':p,
                     'Price':pri,
                     'Quantity':q,
                     'Total Price':pri*q}
                li.append(item)
            except ValueError:
                print("Give valid input")
                continue
        elif a=='R':
            print(bill)
            break
        
        else:
            print("Give valid input")
            break
    for k in li:
        b=k['Total Price']
        c+=b
        print(k)
        bill+="\n"
        bill+=str(k)
    print("Total Cost: ",c)
    tcost=f"Total Cost: {c}"
    text_to_pdf(li,title,tcost,dto) 
    

dto="Bill.pdf"
title=str(input("Enter Store Name: \n"))
basic(dto,title)
