from bs4 import BeautifulSoup
import os
import pandas as pd
from tqdm import tqdm
import re

def remove_arabic_diacritics(text):
    arabic_diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    cleaned_text = re.sub(arabic_diacritics, '', text)
    return cleaned_text

path = "poems_html"
html_files = os.listdir(path)

html_contents = [open(f"{path}/{file}").read() for file in tqdm(html_files)]

def extract_poem(soup):
    poem_div = soup.find('div', id='poem_content')
    if len(poem_div.find_all('h3')) > 0:
        poem_lines = [h3.get_text() for h3 in poem_div.find_all('h3')]
    else:
        poem_lines = [h4.get_text() for h4 in poem_div.find_all('h4')]
    poem_text = '\n'.join(poem_lines)
    return poem_text

def extract_tags(soup):
    tips_div = soup.find('div', class_='tips')
    tips_links = tips_div.find_all('a')
    tip_texts = [tip.get_text(strip=True) for tip in tips_links]
    
    return tip_texts    

def extract_poet(soup):
    section_div = soup.find('div', class_='m-section-2')
    a_tags = section_div.find_all('a')
    poet_name = a_tags[2].get_text(strip=True)
    
    return poet_name

data = []

for html_content in tqdm(html_contents):
    soup = BeautifulSoup(html_content, "html.parser")
    poem = extract_poem(soup)
    try:
        poet_name = extract_poet(soup)
    except:
        poet_name = "Unknown"
    tags = extract_tags(soup)
    data.append({"poet": poet_name, "poem": poem, "tags": tags})
    
    
df = pd.DataFrame(data)
df["poem_no_diacritics"] = df["poem"].apply(remove_arabic_diacritics)

assert len(df) == len(html_files)
df["id"] = html_files

df.to_json("poems.jsonl", orient="records", lines=True, force_ascii=False)