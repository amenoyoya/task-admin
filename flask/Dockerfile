FROM python:3.7-alpine

# uWSGIビルド用ツール
RUN apk add gcc build-base linux-headers

# 作業ディレクトリを変数`project_dir`に格納
ARG project_dir=/var/www/app/

# 必要なファイルをコンテナ内にコピー
COPY requirements.txt $project_dir

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
