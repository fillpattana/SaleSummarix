import fitz


doc = fitz.open('/Users/r13_2014/Desktop/SaleSummarix/SPF2303037509_e_Tax_Invoice_by_Shopee/TIV_SPF2303037509.pdf')

for page in doc:
  text = page.get_text()
  print(text)