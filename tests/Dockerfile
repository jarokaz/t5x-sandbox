FROM python:3.8

WORKDIR /llm
RUN git clone --branch=main https://github.com/google-research/t5x

RUN pip install --upgrade pip
RUN pip install "jax[tpu]>=0.2.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

WORKDIR /llm/t5x
RUN python -m pip install -e '.[tpu]' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
