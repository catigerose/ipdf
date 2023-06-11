#!/usr/bin/env python
# coding: utf-8

import fitz
import os


# gap 注释之间的间隔
def refresh_cursor(cursor, h, gap=2):
    return fitz.Rect(0, cursor.y1+gap, page.rect.x1, cursor.y1+h+gap)


pdf_names = next(os.walk("./raw_pdf/"))[-1]
for pdf_name in pdf_names:
    # print(pdf_path)

    fn = "./raw_pdf/"+pdf_name

    doc = fitz.open(fn)  # 打开笔记文件
    clips = fitz.open()  # 创建一个空的document对象， 用于插入注释剪切横条

    # 初始化一个新页面和初始化游标
    page = doc[0]
    page_width = page.rect.width
    page_height = page.rect.height

    # 创建一个新页面
    new_page = clips.new_page(-1,
                              width=page_width,
                              height=page_height)

    cursor = initial_cursor = fitz.Rect(
        0, 0, page.rect.x1, 0)  # 页面插入注释的游标rect，初始位置为页面顶部的横线

    for i in range(doc.page_count):
        # print(i)
        page = doc[i]  # 加载一个页面
        page_width = page.rect.width
        page_height = page.rect.height
        annots = list(page.annots())  # 获取该页面所有注释

        for j in range(len(annots)):
            annot = annots[j]  # 获取一个注释
            rect = annot.rect  # 获取该注释坐标
            # 将注释坐标拉到页面宽度:x0=0,x1=page.rect.x1
            annot_wide_rect = fitz.Rect(0, rect.y0, page.rect.x1, rect.y1)
            h = annot_wide_rect.height  # 注释的高度

            cursor = refresh_cursor(cursor, h)  # 更新页面插入注释的游标rect
            # 判断是否超出页面底部，如果超出，新建一个页面；初始化游标，然后更新游标
            if cursor.y1 > page_height:
                # 创建新页面
                new_page = clips.new_page(-1,
                                          width=page_width,
                                          height=page_height)

                cursor = refresh_cursor(initial_cursor, h)  # 初始化游标，然后更新游标

            # 新页面插入剪切横条
            new_page.show_pdf_page(
                cursor,  # fill all new page with the image
                doc,  # input document
                i,  # input page number
                clip=annot_wide_rect,  # which part to use of input page
            )

    clips.save("./clips/"+"clip_"+pdf_name,
               garbage=3,  # eliminate duplicate objects
               deflate=True,  # compress stuff where possible
               )
    doc.close()
    clips.close()
