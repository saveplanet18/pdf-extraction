import os 
from pdf2image import convert_from_path


def convert_pdf_to_jpg(pdf_path):
    for root,dirs,files in os.walk(pdf_path):
        for filename in files:
            basename,extension=os.path.splitext(filename)
            if extension ==".pdf":
                path=root+'//'+basename+extension 
                pdf_list=[]     
                pdf_list.append(path)
                for files in pdf_list:
                      images=convert_from_path(files,500)
                      for i in images:
                        img=basename+'.jpg'
                        i.save(img,"JPEG")




def Directory():
    
    pdf_path=r'pdffile'
    pdf = convert_pdf_to_jpg(pdf_path)
    return pdf
    


if __name__=="__main__":
    Directory()








