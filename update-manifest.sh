#!/bin/bash

# Variables
MANIFEST_REPO="git@github.com:your-org/k8s-manifests.git"
DEPLOYMENT_FILE="manifests/deployment.yaml"
DOCKER_IMAGE_BACKEND="your-dockerhub-username/contract-backend:latest"
DOCKER_IMAGE_FRONTEND="your-dockerhub-username/contract-frontend:latest"

# Clone the manifests repository
rm -rf k8s-manifests
git clone $MANIFEST_REPO
cd k8s-manifests

# Update Kubernetes deployment file
sed -i "s|image: .*contract-backend.*|image: $DOCKER_IMAGE_BACKEND|" $DEPLOYMENT_FILE
sed -i "s|image: .*contract-frontend.*|image: $DOCKER_IMAGE_FRONTEND|" $DEPLOYMENT_FILE

# Commit and push changes
git config --global user.email "ci-bot@yourcompany.com"
git config --global user.name "CI/CD Pipeline"
git add $DEPLOYMENT_FILE
git commit -m "Update deployment images to latest version"
git push origin main

echo "Kubernetes manifests updated successfully!"
