FROM gcr.io/deeplearning-platform-release/base-cpu

WORKDIR /llm

RUN conda create -n t5x python=3.9

RUN git clone --branch=main https://github.com/google-research/t5x
RUN /opt/conda/envs/t5x/bin/pip install --upgrade pip

RUN /opt/conda/envs/t5x/bin/pip install -e 't5x[tpu]' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

RUN /opt/conda/envs/t5x/bin/pip uninstall seqio seqio-nightly -y
RUN /opt/conda/envs/t5x/bin/pip install seqio-nightly

ADD test.py ./