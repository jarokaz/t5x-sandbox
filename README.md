# T5X on Vertex AI

This repository compiles prescriptive guidance and code samples demonstrating how to operationalize Google Research T5X framework on Vertex AI.


## T5X Overview

### Configuring T5X jobs using Gin

### Configuring T5X tasks and mixtures with SeqIO

#### Developing custom SeqIO tasks

### Defining data and model partitioning

## Running Vertex AI T5X jobs

### Building Vertex AI custom training container

From the repo's root folder run the following command:

```
PROJECT_ID=jk-mlops-dev
IMAGE_NAME=gcr.io/$PROJECT_ID/t5x_base
docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
```

### Defining Vertex AI Training T5X jobs

### Using Vertex AI Experiments to track and analyze T5X jobs

#### Creating Vertex AI Tensorboard instance

```
PROJECT_ID=jk-mlops-dev
REGION=us-central1
TENSORBOARD_INSTANCE_NAME=t5x-experiments

gcloud ai tensorboards create \
--display-name=$TENSORBOARD_INSTANCE_NAME \
--region=$REGION \
--project=$PROJECT_ID
```

## Repository structure

## Contributing

## Getting help

## Disclaimer

## Feedback
