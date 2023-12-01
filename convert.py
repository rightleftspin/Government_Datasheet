from pypdf import PdfReader
import sys
from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
import io

food_calories = read_pdf('./officeholder_2023.pdf', pages = [5, 6, 7])
print(food_calories)
