# T5X Sandbox


## Provisioning TPU VM device

```
gcloud alpha compute tpus tpu-vm create jk-v3-8 \
  --zone=us-central1-a \
  --accelerator-type=v3-8 \
  --version=tpu-vm-base \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

## Provisioning TPU VM slice

```
gcloud alpha compute tpus tpu-vm create jk-v2-32 \
  --zone=us-central1-a \
  --accelerator-type=v2-32 \
  --version=tpu-vm-base \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

