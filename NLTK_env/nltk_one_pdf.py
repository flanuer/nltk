#This is just to open one pdf for NLTK reader

import nltk
import PyPDF2
import textblob as TextBlob
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


mypdf = open("/home/scott/projects/RedTideResearch/dataHarvests/COHH-impleplan_31823.pdf", mode="rb")
mypdf2 = open("/home/scott/projects/RedTideResearch/dataHarvests/Blasco-1977-Limnology_and_Oceanography.pdf", mode="rb")

pdf_document = PyPDF2.PdfFileReader(mypdf)
pdf_document2 = PyPDF2.PdfFileReader(mypdf2)

first_page = pdf_document.getPage(4)
first_page2 = pdf_document2.getPage(0)

print(first_page.extractText())
print("-----------------second pdf --------------------------------------")
print(first_page2.extractText())

print("++++++++++++++++ sent tokenize +++++++++++++++++++++++++++++++++++")

print(sent_tokenize(pdf_document2))