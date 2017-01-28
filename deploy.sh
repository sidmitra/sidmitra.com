rm -drf public/ && hugo --theme=custom && cd public && yes|gcloud app deploy --version=2
