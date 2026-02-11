#!/bin/sh
set -e


GITHUB_REPO=$1
DOCKER_REPO=$2


if [ -z "$DOCKER_USER" ] || [ -z "$DOCKER_PWD" ]; then
    echo "Error: DOCKER_USER or DOCKER_PWD not set."
    exit 1
fi


echo "$DOCKER_PWD" | docker login -u "$DOCKER_USER" --password-stdin


TEMP_DIR="temp_repo"
echo "Cloning https://github.com/$GITHUB_REPO..."
git clone "https://github.com/$GITHUB_REPO.git" $TEMP_DIR

cd $TEMP_DIR
echo "Building $DOCKER_REPO..."
docker build -t $DOCKER_REPO .

echo "Pushing $DOCKER_REPO..."
docker push $DOCKER_REPO

echo "Done!"