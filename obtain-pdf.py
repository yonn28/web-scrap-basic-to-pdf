from xhtml2pdf import pisa


for i in list(range(30,32)):
    output_filename = f'output{i}.pdf'
    # to obtain pdf
    dataHtml = open(f'output{i}.html',"r")
    result_file = open(output_filename, "w+b")
    pisa_status = pisa.CreatePDF( dataHtml, dest=result_file ) 