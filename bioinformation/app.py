import streamlit as st
import yfinance as yf
import altair as alt
from PIL import Image
import pandas as pd

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width = True)


st.write("""
## DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***

""")


tickerSymbol = 'GOOGL'

st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nAAAAAAAAAAAAffjhfjhdcmjBBchgnJFVFJHTDGGGGCGKMJAAAKFGGGGGKHHNHVHDtttGGGGGttttBBBBBtttttttttBBBBttttttBBBBttttttttttttttttttttttttttttyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\nGJTFCHTCHCCCCCGKFUTDGHGGGGGGGCHGDCJGRSXYMKHDGCHMFSXJVJGMXFJGGXCJHGCHGCJHVFJYKFKHTDGFJGFUJKHGFCBJHF"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ' .'.join(sequence)
st.write('''
***
''')
## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT(DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('B', seq.count('B')),
        ('G', seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X
#Print text
st.subheader('2. Print text')

st.write('there are' + str(X['A']) + 'adeline(A)')
st.write('there are' + str(X['B']) + 'adeline(B)')
st.write('there are' + str(X['G']) + 'adeline(G)')
st.write('there are' + str(X['A']) + 'adeline(A)')

###3. Display Dataframe
st.subheader('Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns=  {'index': 'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair

st.subheader('4. Display bar Altair')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width = alt.Step(100)
)
st.write(p)
