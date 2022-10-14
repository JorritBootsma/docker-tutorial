# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip3 install -v -r requirements.txt

COPY . .

EXPOSE 8501

# For Streamlit:
CMD ["streamlit", "run", "streamlit_app.py"]