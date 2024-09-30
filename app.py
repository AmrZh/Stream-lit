import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from transformers import pipeline

# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)

# import streamlit as st

# st.title("This is a title")
# st.title("_Streamlit_ is :blue[cool] :sunglasses:")

pipe = pipeline("image-classifiction", model="julien-c/hotdog-not-hotdog")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    img = image.open(uploaded_file)
    st.image(img)
    predictions = pipe(imge)
    st.write(predictions)

img = Image.open(uploaded_file)

predictions = pipe(img)
