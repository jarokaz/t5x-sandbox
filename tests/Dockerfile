FROM python:3.8

WORKDIR /llm

RUN git clone --branch=main https://github.com/google-research/t5x
RUN pip install --upgrade pip

RUN python -m pip install -e 't5x[tpu]' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
