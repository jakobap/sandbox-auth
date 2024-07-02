# GCP Custom LLM App Auth

This repo is showcasing how to setup authentication on GCP without Service Account keys for a simple custom LLM application.

## Getting Started
1. Fill out variables in `.env`
2. [Create Docker repository in GCP Artifact Registry](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create)
3. Make sure that the Service Account used by Cloud Run (usually default compute SA) has [Vertex AI User](https://cloud.google.com/vertex-ai/docs/general/access-control) permissions.
4. Get started using:
```bash
# Make command to build and deploy Flask LLM app
make all
```