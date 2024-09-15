# -*- coding: utf-8 -*-
"""UNDERDOGS.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t2qG6MnRDTPUa6SUTUkyuO5IUuh79PS5
"""

!pip install huggingface
!pip install sentence-transformers
!pip install torch
!pip install -q -U google-generativeai

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from google.colab import userdata
import PIL.Image

GOOGLE_API_KEY=userdata.get('gemini_api_key')

genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


img = PIL.Image.open('/content/drive/MyDrive/Prescriptions/medicine prescription - Google Search 3.png')

model = genai.GenerativeModel('gemini-pro-vision')


response = model.generate_content(["Please analyse the provided image accurately and explain the data present in the image", img], stream=True)
response.resolve()
print('medicine present:', response.text)

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import pickle
from sentence_transformers import util

df = pd.read_csv("/content/drive/MyDrive/MEDICIE DATA/medicinedataset.csv")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Get embeddings for all medicines
with open('/content/drive/MyDrive/medicine-embeddings.pkl', "rb") as fIn:
    embeddings = pickle.load(fIn)
    print(f"Shape of one embedding{embeddings[0].shape}")

# Perform Semantic Search for substitutes
def find_substitutes(prompt, df, model, embeddings):
    # Get embedding for the prompt
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)

    # Perform semantic search
    hits = util.semantic_search(prompt_embedding, embeddings, top_k=5)

    # Extract substitute medicines
    substitute_indices = [hit['corpus_id'] for hit in hits[0]]
    substitute = df.iloc[substitute_indices[0]]['substitutes']

    return substitute


prompts = [
    'albendazol 40mg',
    'syrup ofloxacin 250 mg',
    'ranitidine 150 mg',
    'levocetirizine 5 mg'
]

prescription_image_texts = prompts



alternatives = {}
for medicine in prescription_image_texts:
    alternatives[medicine] = find_substitutes(medicine, df, model, embeddings)
    print(f"Alternatives for {medicine}: {alternatives[medicine]}")

import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle
from sentence_transformers import util

class MedicineSubstitutes:
    def __init__(self):
        self.df = pd.read_csv("/content/drive/MyDrive/MEDICIE DATA/medicinedataset.csv")
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        # Get embeddings for all medicines
        with open('/content/drive/MyDrive/medicine-embeddings.pkl', "rb") as fIn:
            self.embeddings = pickle.load(fIn)
            print(f"Shape of one embedding: {self.embeddings[0].shape}")

    def find_substitutes(self, prompt, top_k=1):
        # Get embedding for the prompt
        prompt_embedding = self.model.encode(prompt, convert_to_tensor=True)

        # Perform semantic search
        hits = util.semantic_search(prompt_embedding, self.embeddings, top_k=top_k)

        # Extract substitute medicines
        substitute_indices = [hit['corpus_id'] for hit in hits[0]]
        substitutes = self.df.iloc[substitute_indices[0]]['substitutes']

        return substitutes

    def find_substitutes_for_prompt(self, prompt):
        substitutes = self.find_substitutes(prompt)
        print(f"Substitutes for {prompt}: {substitutes}")

    def run(self):
        while True:
            prompt = input("Enter the medicine name and dosage: ")
            if prompt.lower() == 'exit':
                print("Exiting program...")
                break
            self.find_substitutes_for_prompt(prompt)

# Instantiate the class and run the program
medicine_substitutes = MedicineSubstitutes()
medicine_substitutes.run()
