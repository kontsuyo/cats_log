FROM python:3.11-slim

# pycファイル(および__pycache__)の生成を行わないようにする
# 本番環境では削除
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
# 本番環境では削除
ENV PYTHONUNBUFFERED=1

# パッケージのインストール
RUN apt-get update -qq &&\
   apt-get install -y --no-install-recommends \
   tzdata \
   sudo \
   less \
   locales \
   python3-dev \
   default-libmysqlclient-dev \
   pkg-config \
   build-essential
RUN rm -rf /var/lib/apt/lists/*

# 日本語のロケールとタイムゾーンの設定
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ="Asia/Tokyo"


# pythonモジュールのインストール
WORKDIR /tmp/work
COPY ./app/requirements.txt ${PWD}
RUN pip install -r requirements.txt \
    django-debug-toolbar \
    django-environ \
    pytest \
    pytest-django


# 環境変数の定義
ENV USER user1

# 一般権限のユーザーを追加
RUN useradd -m ${USER} -u 1000
RUN usermod -aG sudo ${USER}
RUN echo "${USER}:password" | chpasswd

# pathの設定
ENV PATH /root/.local/bin:$PATH

# ユーザーの切替
USER ${USERNAME}
