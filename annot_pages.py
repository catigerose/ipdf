#!/usr/bin/env python
# coding: utf-8


import fitz
import sys
import os


def get_anot_pages(fn):
    doc = fitz.open("./raw_pdf/"+fn)
    dels = []
    # elif page.first_annot.type[-1]!="Ink": 备用
    for i in range(doc.page_count):
        # print(i)
        if (doc[i].first_annot == None):
            dels.append(i)

    print("文件名：{0};   总页数：{1} ;  删除页数：{2};  保留页数：{3}".format(
        fn, doc.page_count, len(dels), doc.page_count-len(dels)))

    doc.delete_pages(dels)

    doc.save("./anot_pages/"+fn[:-4]+"_anot_pages"+fn[-4:])

    doc.close()


pdf_names = next(os.walk("./raw_pdf/"))[-1]
for pdf_name in pdf_names:
    print(pdf_name)
    try:
        get_anot_pages(pdf_name)
    except Exception as e:
        print(pdf_name, e)
        continue
