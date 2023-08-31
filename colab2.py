# -*- coding: utf-8 -*-
"""colabでサクッとStreamlit（最小構成）_のコピー.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DLwvBGoHg4jqoV3XTspvvYp3iWYf5sRY

[Streamlit API reference](https://docs.streamlit.io/library/api-reference)

[Streamlit configuration](https://docs.streamlit.io/library/advanced-features/configuration)
"""

!pip install streamlit

import streamlit as st
st.title("WizWe Planning Team")

import streamlit as st
import numpy as np

# streamlitのメソッドでmarkdown形式で表示
st.write(
    """
    # 案件状況の可視化
    グラフのイメージ-数種類*
    """
    )

# 適当なデータ作成
data = np.arange(0, 10, 0.1)

# streamlitのメソッドでデータを直線グラフに
st.line_chart(data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('案件ごとの進捗率')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.dataframe(chart_data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('NPSのイメージ')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
st.dataframe(chart_data)


import pandas as pd
import matplotlib.pyplot as plt

# Matplotlibの設定を変更

# CSVファイルを読み込む
df = pd.read_csv('word_counts_2.csv', encoding='shift_jis')

df['count'] = df['count'].astype(int)
df['word'] = df['word'].astype(str)

# 出現回数でソートして上位20番目までを取得
top_20 = df.sort_values(by='count', ascending=False).head(20)

df

from google.colab import files
files.view("/content")
files.view("app.py")

!streamlit run app.py & sleep 3 && npx localtunnel --port 8501

from google.colab import drive
drive.mount('/content/drive/')

!streamlit run app.py & sleep 3 && npx localtunnel --port 8501









