FROM python:3.9 

WORKDIR /
RUN git clone --branch=main https://github.com/google-research/t5x
WORKDIR t5x

RUN pip install -e '.[tpu]' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
RUN pip uninstall seqio seqio-nightly -y
RUN pip install seqio-nightly

RUN apt-get install apt-transport-https ca-certificates gnupg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-cli -y

ENTRYPOINT ["python", "./t5x/main.py"]