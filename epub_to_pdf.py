import fitz
import sys
import os


def epub_to_pdf(fn,equb_dir="./epub/",pdf_dir="./pdf/"):    
    #equb_dir = code_path+equb_dir
    #pdf_dir = code_path+pdf_dir
    doc = fitz.open(equb_dir+fn)


    b = doc.convert_to_pdf()  # convert to pdf
    pdf = fitz.open("pdf", b)  # open as pdf

    toc= doc.get_toc()   # table of contents of input
    pdf.set_toc(toc)  # simply set it for output
    meta = doc.metadata  # read and set metadata
    if not meta["producer"]:
        meta["producer"] = "PyMuPDF v" + fitz.VersionBind

    if not meta["creator"]:
        meta["creator"] = "PyMuPDF PDF converter"
    meta["modDate"] = fitz.get_pdf_now()
    meta["creationDate"] = meta["modDate"]
    pdf.set_metadata(meta)

    # now process the links
    link_cnti = 0
    link_skip = 0
    for pinput in doc:  # iterate through input pages
        links = pinput.get_links()  # get list of links
        link_cnti += len(links)  # count how many
        pout = pdf[pinput.number]  # read corresp. output page
        for l in links:  # iterate though the links
            if l["kind"] == fitz.LINK_NAMED:  # we do not handle named links
                #print("named link page", pinput.number, l)
                link_skip += 1  # count them
                continue
            pout.insert_link(l)  # simply output the others

    # save the conversion result
    pdf.save(pdf_dir+fn[:-5] + ".pdf", garbage=4, deflate=True)
    # say how many named links we skipped
    #if link_cnti > 0:
        #print("Skipped %i named links of a total of %i in input." % (link_skip, link_cnti))
epub_names = next(os.walk("./epub/"))[-1]
for epub_name in epub_names:
    try:
        epub_to_pdf(epub_name)  
    except Exception as e:
        print(epub_name,e)
        continue