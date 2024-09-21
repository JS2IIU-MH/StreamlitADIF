# ADIF utils on Streamlit

Streamlitを使ってADIFユーティリティツールを公開していきます。

## ADIF to CSV

ADIFファイルを読み込ませて、CSVファイル化したものをダウンロードすることができます。**残念ながらファイルサイズ200M制限があります。おそらく7000QSO程度で超えてしまうのではないかと思われます。**大きいファイルへの対応は対応方法を検討中です。

Streamlit Community Cloudにデプロイしております。こちらからアクセスして下さい。

[https://appadif-csv.streamlit.app/](https://appadif-csv.streamlit.app/)

**全体のながれ**

- ユーザーがADIFまたはADIファイルをアップロード。
- ファイルの内容がパースされ、ヘッダーとレコードに分けられた後、各レコードが解析されてDataFrameに変換。
- 変換されたデータがアプリ上に表示され、CSV形式でダウンロード可能。

こちらのブログ記事を参考にして下さい。

- [StreamlitでADIFファイルCSV変換ツールを作成する | アマチュア無線局JS2IIU](https://js2iiu.com/2024/09/21/streamlit-adif-csv/)

