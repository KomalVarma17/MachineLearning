# -*- coding: utf-8 -*-
"""userinterface.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10aYAaGnl4XzMjYhcFPCx37EEGFNwDIkc
"""

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