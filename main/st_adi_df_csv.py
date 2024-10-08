''' st_adi_df_csv.py: convert adif file to csv on Streamlit demo '''

import re

import pandas as pd
import streamlit as st

def parse_adif_record(record):
    ''' returns parsed one QSO record as dict '''
    # Find all fields in the format <FIELD:LENGTH>value
    fields = re.findall(r'<(.*?):(\d+)>([^<]*)', record)
    return {field[0].upper(): field[2] for field in fields}

def adif_to_dataframe(file_content):
    ''' returns pd.DataFrame with all records in adif file '''
    lines = file_content.decode("utf-8").splitlines()

    # Find the line where the header ends
    start_line = 0
    for i, line in enumerate(lines):
        if "<EOH>" in line:
            start_line = i + 1
            break

    # Process records after the header
    records = []
    adif_data = ''.join(lines[start_line:]).split("<EOR>")

    for record in adif_data:
        if record.strip():
            records.append(parse_adif_record(record))

    # Convert to DataFrame
    adif_df = pd.DataFrame(records)
    return adif_df

# Streamlit App
st.set_page_config(
    page_title="ADIF/ADIファイル変換",
)

st.title("ADIF/ADIファイル変換")

st.write("本ツールによる損害等には責任を持ちません。ADIFファイルはバックアップした状態でご利用ください。サーバ側にADIFデータは残しません。")

# ファイルアップローダー (ADIFとADIファイルに対応)
uploaded_file = st.file_uploader("ADIFまたはADIファイルをアップロードしてください", type=["adif", "adi"])

# ファイルがアップロードされたら処理
if uploaded_file is not None:
    df = adif_to_dataframe(uploaded_file.read())
    st.write("ADIF/ADIファイルの内容:")
    st.dataframe(df)

    # DataFrameをCSVに変換
    csv = df.to_csv(index=False)

    # CSVダウンロードボタン
    st.download_button(
        label="CSVをダウンロード",
        data=csv,
        file_name="adif_data.csv",
        mime="text/csv"
    )
