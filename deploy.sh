rm -drf public/ && hugo --theme=custom && cd public && yes|gcloud app deploy --no-promote --version=2
