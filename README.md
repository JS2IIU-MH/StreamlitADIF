# ADIF utils on Streamlit

![](https://byob.yarr.is/JS2IIU-MH/StreamlitADIF/time)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

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

そのほかの参考記事

- [【Python】Streamlit入門編 | アマチュア無線局JS2IIU](https://js2iiu.com/2024/08/17/pythonstreamlit-basic/)
- [Streamlit応用編 第1回: キャッシュ機能の活用 | アマチュア無線局JS2IIU](https://js2iiu.com/2024/08/28/streamlit-01-cache/)
- [Streamlit応用編 第2回: インタラクティブなウィジェットの応用](https://js2iiu.com/2024/08/29/streamlit-02-widget/)
- [Streamlit応用編 第3回: データのアップロードとダウンロード](https://js2iiu.com/2024/08/29/streamlit-03-download/)
- [Streamlit応用編 第4回: レイアウトのカスタマイズ](https://js2iiu.com/2024/08/30/streamlit-04-layout/)
- [Streamlit応用編 第5回: テーマのカスタマイズ](https://js2iiu.com/2024/08/31/streamlit-05-theme-custom/)
- [Streamlit応用編 第6回: デプロイと共有](https://js2iiu.com/2024/09/01/streamlit-06-deploy/)
- [Streamlit応用編 第7回: 認証とセキュリティ](https://js2iiu.com/2024/09/02/streamlit-07-security/)
- [Streamlit応用編 第8回: データベースとの連携](https://js2iiu.com/2024/09/02/streamlit-08-database/)
- [Streamlit応用編 第9回: 複雑なデータビジュアライゼーション](https://js2iiu.com/2024/09/05/streamlit-09-visualization/)
- [Streamlit応用編 第10回: マルチページアプリの作成](https://js2iiu.com/2024/09/06/streamlit-10-multipage/)
- [Streamlit応用編 第11回: StreamlitでAPIを作成する方法](https://js2iiu.com/2024/09/07/streamlit-11-api/)

## 参考

- [The Independent ADIF Site](https://www.adif.org/)
- [Streamlit • A faster way to build and share data apps](https://streamlit.io/)
- [Streamlit Community Cloud • Streamlit](https://streamlit.io/cloud)