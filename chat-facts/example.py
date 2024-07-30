import streamlit as st
import numpy as np
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")


def rand_table(col_range = 5):
    df = pd.DataFrame(
    np.random.randn(10, col_range),
    columns=('col %d' % (i + 1) for i in range(col_range))
    )
    return st.dataframe(df.style.highlight_max(axis=0))


def draw_chart():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    return st.line_chart(chart_data)


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option