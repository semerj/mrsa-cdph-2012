from itertools import groupby
import pandas as pd
import re
import os


def mrsa(doc):
    pages = []
    with open(doc, 'r') as inputfile:
	  fx = lambda x: re.search(r'Go Back To Table of Contents Page', x)
	  for k, g in groupby(inputfile, key=fx):
	      if not k:
	          pages.append(list(g))
    
    data = pd.DataFrame()
    measure = []
    for p in pages:
        df = pd.DataFrame([re.split(r'\s{2,}|\, (?=\d)', d.strip()) for d in p if re.findall(r'[A-Z]{5}', d)])
        matched = re.findall(r'Table \d\. ([^]]*)\*', " ".join(p[0:3]).replace('\n', ''))
        if matched:
            measure.append(matched[0])
            df['measure'], df['facility'] = matched[0].split(' Reported by California ')
            data = data.append(df)
    
    data.columns = ['hosp', 'count', 'ptDays', 'sir', 'ciLow', 'ciHigh', 'comp', 'facility', 'measure']
    data.loc[data.sir.str.contains('[A-z]', na=False), 'comp'] = data.loc[data.sir.str.contains('[A-z]', na=False), 'sir']
    data.loc[data.sir.str.contains('N', na=False), 'sir'] = None
    data['ciLow'] = data['ciLow'].str.replace('[()]', '')
    data['ciHigh'] = data['ciHigh'].str.replace('[()]', '')
    data.drop_duplicates(inplace=True)
    data.to_csv('mrsa2012.csv', index=False)


if __name__ == "__main__":
    mrsa('out-2012-MRSA-BSI-T1-T4.txt')
