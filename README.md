# T5X Sandbox


## Build a T5X container

```

PROJECT_ID=jk-mlops-dev
IMAGE_NAME="gcr.io/$PROJECT_ID/t5x_base"

docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
```


## Provisioning TPU VM device

```
gcloud alpha compute tpus tpu-vm create jk-v3-8 \
  --zone=us-central1-a \
  --accelerator-type=v3-8 \
  --version=tpu-vm-base \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

```
gcloud alpha compute tpus tpu-vm ssh jk-v3-8 \
  --zone us-central1-a \
  --command="pip install ipython 'jax[tpu]>=0.2.16' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html"
```

## Provisioning TPU VM slice

```
gcloud alpha compute tpus tpu-vm create jk-v2-32 \
  --zone=us-central1-a \
  --accelerator-type=v2-32 \
  --version=tpu-vm-base \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

## Installing JAX
```
gcloud alpha compute tpus tpu-vm ssh jk-v2-32 \
  --zone us-central1-a \
  --worker=all \
  --command="pip install ipython 'jax[tpu]>=0.2.16' -f https://storage.googleapis.com/jax-releases/libtpu_releases.html"
```
