FROM python:3.8

WORKDIR /app
COPY build.sh .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x build.sh



COPY . .

RUN  ./build.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]