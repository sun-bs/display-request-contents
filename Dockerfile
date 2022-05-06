FROM python:alpine

WORKDIR /app
COPY ./index.py /app/index.py
RUN pip install Flask
CMD ["python", "index.py"]