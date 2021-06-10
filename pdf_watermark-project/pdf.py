import PyPDF2
import sys

# project 1: create a new tilded PDF
# with open('./dummy.pdf','rb') as file:
#     print(file) 
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilted.pdf','wb') as new_file:
#         writer.write(new_file)

# project 2: merge a n. if PDFs passed as arguments
# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         # print(pdf)
#         merger.append(pdf)
#     merger.write('combined.pdf')

# pdf_combiner(inputs)

#project 3: watermark the combined PDF file

# PSEUDO CODE

# create a function that get:
        # create I (data)
            # create a file combined reader     
            # create a file watermark reader

        # create O empty (result)

        # algorithm: loop through each page and add a watermark
            # how to find the num of pages? create a range object -> range(template.getNumPages())
                # for each page 
                # add a watermark page (do the merge)
                # add it to the output
                # create a new pdf to write over
                    # write the file to the otuput


def watermarker():
    template = PyPDF2.PdfFileReader(open('./combined.pdf','rb'))
    watermark = PyPDF2.PdfFileReader(open('./wtr.pdf','rb'))

    output = PyPDF2.PdfFileWriter() 

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('./draft-watermarked.pdf','wb') as file:
            output.write(file)

watermarker()