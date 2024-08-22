import time

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

st.title("My first app")

st.write("プログレスバーの表示")
"Start!!"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done"

st.write("Dataframe")

df = pd.DataFrame(
    {
        "1列目": [1, 2, 3, 4],
        "2列目": [10, 20, 30, 40],
    }
)
st.dataframe(
    df.style.highlight_max(axis=0), width=200, height=200
)  # データフレームを表示 axisは列方向に最大値を探す

st.table(df)  # テーブルを表示

# マークダウンで書くことができる
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```


"""

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# 折れ線グラフ
st.line_chart(df)
# エリアチャート
st.area_chart(df)
# 棒グラフ
st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.randn(100, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
# )
# # 地図の作成
# st.map(df)

st.write("Display Image")

option = st.selectbox("Select Image", ["miyawaki", "sakura", "sakura2"])
if option == "miyawaki":
    col1, col2, col3 = st.columns(3)
    img = Image.open("IMG_5655.jpg")
    with col2:
        st.image(
            img,
            caption="miyawaki",
            width=300,
            # use_column_width=True,
        )
# if st.checkbox("Show Image"):
#     img = Image.open("IMG_5655.jpg")
#     st.image(
#         img,
#         caption="miyawaki",
#         width=300,
#         # use_column_width=True,
#     )

# st.sidebarでサイドバーを作成できる
st.write("Interactive Widgets")
text = st.text_input("あなたの名前は", "miyawaki")
st.write("Your name is", text)

condition = st.slider("Slide me", 1, 100, 50)
st.write("あなたの今の調子は", condition)

exp1 = st.expander("出身地はどこですか")
exp1.write("広島です")
exp2 = st.expander("趣味は何ですか")
exp2.markdown(""":rainbow[温泉]に入ることです""")
