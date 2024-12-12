#!/usr/bin/env python
import json
from dataclasses import dataclass
import requests
import pandas as pd


@dataclass
class ApiData():
    url: str
    out_file: str = "outfile.json"
    
    def get_response(self):
        response = requests.get(self.url)
        return response
        
    def write_response(self):
        try:
            r = self.get_response()
            with open(self.out_file, 'w') as f:
                f.write(r.text)
            print(f"Wrote response to {self.out_file}")
        except Exception as e:
            print(f"Error occured when writing file: {e}")


@dataclass
class JsonData:
    in_file: str
    response_key: str
    out_file: str = 'normalized.csv'
    
    def load_file(self):
        with open(self.in_file, "r") as file:
            json_data = json.load(file)
        return json_data
    
    def normalize_array(self):
        df = pd.json_normalize(self.load_file())
        series = df[self.response_key]
        print('Check type: ', type(series))
        exploded = series.explode()
        normalized_df = pd.json_normalize(exploded)
        return normalized_df
    
    def write_dataframe(self, df):
        try:
            df.to_csv(self.out_file, index = False)
        except Exception as e:
            print(f"Error occured when writing file: {e}")

