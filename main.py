import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text('Iteration' +str(i+1))
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!'
left_column,right_culumn=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラム')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2内容を書く')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ3内容を書く')
# text = st.text_input('あなたの趣味を教えてください。')
# condition=st.slider('あなたの調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション：',condition
# option = st.selectbox(
#     'あなたの好きな数字を教えてください。',
#     list(range(1,11))
# )
#'あなたの好き数字は',option,'です。'
# if st.checkbox('show image'):
#     img=Image.open('bokeh_plot.png')
#     st.image(img,caption='stock',use_column_width=True)
