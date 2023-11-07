#format conwersion, liushuotng, SDU
#coding:UTF-8
import re
import pdf2docx
from pdf2docx import Converter
def p2d(str1,str2):
    pdf2docx.Converter(str1,str2)

import docx2pdf
from docx2pdf import convert
def d2p(str1):
    docx2pdf.convert(str1)


import pdf2image
from pdf2image.pdf2image import convert_from_path, convert_from_bytes
def p2m(str1):
    images = convert_from_path(str1)

def main():
    stop = 1
    while(stop == 1):

        print("----------------------------")
        print("----format----conversion----")
        print("----------------------------")
        x = int(input("[1_*.pdf->*.docx\\2_*.pdf->image\\3_*.docx->*.pdf]:"))
        while(x != 1 and x != 2 and x != 3):
            print("Enter Correct Format!")
            x = int(input("[1_*.pdf->*.docx\\2_*.pdf->image\\3_*.pptx->*.docx]:"))
        
        if x == 1:
            print("--------------")
            print("--PDF->WORD---")
            print("--------------")
            pdf_filename = input("pdf_file_name:")
            print("-----------------------")
            re.search(pdf_filename,'.pdf',flags = 0)
            while(re.search(pdf_filename,'.pdf',flags = 0) == None):
                pdf_filename = input("the location must involve \"*.pdf\":")
                print("-----------------------")
                re.search(pdf_filename,'.pdf',flags = 0)
            docx_filename = input("docx_file_name:")
            print("-----------------------")
            re.search('.docx',docx_filename)
            while(re.search('.docx',docx_filename) == None):
                docx_filename = input("the location must involve \"*.docx\"")
                re.search('.docx',docx_filename)
            p2d(pdf_filename,docx_filename)

        if x == 2:
            print("--------------")
            print("--PDF->IMAGE--")
            print("--------------")
            pdf_filename = input("pdf_file_name:")
            re.search('.pdf',pdf_filename)
            print("-----------------------")
            while(re.search('.pdf',pdf_filename) == None):
                pdf_filename = input("the location must involve \"*.pdf\"")
                re.search('.pdf',pdf_filename)
                print("-----------------------")
            p2m(pdf_filename)
        
        if x == 3:
            print("--------------")
            print("--WORD->PDF---")
            print("--------------")
            docx_filename = input("docx_file_name:")
            print("-----------------------")
            re.search('.docx',docx_filename)
            while(re.search('.docx',docx_filename) == None):
                docx_filename = input("the location must involve \"*.docx\"")
                re.search('.docx',docx_filename)
            d2p(docx_filename)

        stop = int(input("END THE SCRIPT[1_N\\0_Y]:"))
    input("Press any key to exit.")

if __name__ == '__main__':
    main()