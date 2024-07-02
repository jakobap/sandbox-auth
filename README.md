# GCP Custom LLM App Auth

This repo is showcasing how to setup authentication on GCP without Service Account keys for a simple custom LLM application.

## Getting Started
1. Fill out variables in `.env`
2. [Create Docker repository in GCP Artifact Registry](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create)
2. Get started using:
```bash
# Make command to build and deploy Flask LLM app
make all
```