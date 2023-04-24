# 使用方法

### 1. OpenAI

- OpenAI アカウントを作成
- OpenAI API キーを取得

  <br/>

### 2. Python

```
# git clone
git clone https://github.com/tukky-14/python_chatgpt_line.git
cd python_chatgpt_line

# line-bot-sdk
pip install line-bot-sdk -t .

# openai
pip install open -t .
```

<br/>

### 3. AWS

- Lambda の作成
  - AWS で python の Lambda 関数を作成
  - Zip 圧縮したこのソースをアップロード
  - 一般設定（任意）
    - メモリ　　　：1024MB
    - タイムアウト：30 秒
  - 環境変数
    - 1.の OpenAI API キー
    - 4.の「チャネルアクセストークン」
- API Gateway の作成
  - API Gateway で REST API を作成
  - リソースを作成
  - POST メソッドを作成し、上記で作成した Lambda 関数を設定
  - API を公開

<br/>

### 4. LINE Developers

- Messaging API の作成
- 「チャネルアクセストークン」を取得
- Webhook の設定を有効にし、2.で公開した API エンドポイントを設定
  ※[API エンドポイント + リソース名]で設定することに注意

<br/>
