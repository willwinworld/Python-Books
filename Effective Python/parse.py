#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import docx
import zipfile


reload(sys)
sys.setdefaultencoding('utf-8')


class gogogo(object):
    def __init__(self):
        self.count = 0


    def get_dir(self):
        dirs = os.listdir('result')
        # print pdfs
        for d in dirs:
            # os.system('rm result/%s/*.doc'%d)
            # continue
            all_files = os.listdir('result/%s'%d)

            try:
                os.system('mkdir -p txts/%s' %d)
            except Exception,err:
                print err

            for a in all_files:
                print '*'*8,a
                if '.doc' in a:
                    self.readDocx(d,a)
                # if '.zip' in a:
                    # try:
                    #     os.system('unzip -O CP936 result/%s/%s -d result/%s' %(d,a,d))
                    # except Exception,err:
                    #     print err

    def readDocx(self, d,t):
        print d, t

        fullText = []
        try:
            doc = docx.Document('result/%s/%s' % (d,t))
        except Exception,err:
            print err
            return
        paras = doc.paragraphs
        for p in paras:
            fullText.append(p.text)
        content = '\n'.join(fullText)
        with open('txts/%s/%s.txt'% (d,str(t).replace('.doc','')),'w') as file:
            file.write(content)



def run():
    go = gogogo()
    go.get_dir()

if __name__ == '__main__':
    # run(sys.argv[1])
    run()