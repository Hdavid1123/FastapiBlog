FROM python:3.10
ENV PYTHONUNBUFFERED=true

ADD requirements.txt .
RUN apt install g++
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app

RUN apt-get clean && apt-get update && apt-get install -y locales

CMD ["uvicorn", "app.users:app", "--host=0.0.0.0", "--port", "8000", "--reload"]
