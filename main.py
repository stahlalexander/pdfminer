# PDF Miner import as "pdf"
import pdfminer.high_level as pdf


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #insert location of pdf file to extract text from
    pdf_filepath = ""
    text = pdf.extract_text(pdf_filepath)
    #print pdf text
    print(text)

