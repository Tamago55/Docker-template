FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY . .

# CMD ["python", "./test.py"]
