#! -*- coding:utf-8 -*-

import csv
import os
import time
import copy
import re
from urllib3.exceptions import ProtocolError
import datetime
import requests
from queue import Queue
import threading
from urllib3.exceptions import MaxRetryError
from bs4 import BeautifulSoup

from selenium import webdriver

import html


driver = webdriver.Chrome()




def use_selenium_headless_getdt(url):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    return html





def list_null(list_content):
    if list_content !=[]:
        result = list_content
    else:
        result = ["null"]
    return result



def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)

def use_bs4_parsehtml(html,tag_name):
    tag_list = []
    soup = BeautifulSoup(html, 'html.parser')
    soup_find_all_tagname = soup.find_all(tag_name)
    tag_len = len(soup_find_all_tagname)
    for item in range(tag_len):
        # remove \n \t
        tag_list.append(" ".join(soup_find_all_tagname[item].get_text().split()))
    big_string = " ".join(tag_list)
    final_list= [big_string]
    return final_list



def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)




if __name__=="__main__":
    type = "大手資産運用会社"
    for page in range(50):
        url =""




        html = use_selenium_headless_getdt(url)
        div_tag = use_bs4_parsehtml(html,"div")
        writeintoTSV_file('reruit_{0}.tsv'.format(type), div_tag)











