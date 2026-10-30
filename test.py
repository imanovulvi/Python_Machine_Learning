import numpy as np
import pandas as pd

data = [
    {"sual": "Salam", "cavab": "Salam"},
    {"sual": "Necəsən?", "cavab": "Yaxşıyam"},
    {"sual": "Sabahın xeyir", "cavab": "Sabahın xeyir"},
    {"sual": "Sənin adın nədir?", "cavab": "Mənim adım Robotdur"},
    {"sual": "Sən kimsən?", "cavab": "Mən süni intellektəm"},
    {"sual": "Sağ ol", "cavab": "Dəyməz"},
    {"sual": "Təşəkkür edirəm", "cavab": "Buyur"},
    {"sual": "Hələlik", "cavab": "Görüşənədək"}
]
df=pd.DataFrame(data)
print(df)

