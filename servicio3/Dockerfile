FROM python:3.9-alpine
WORKDIR /servicio3
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5002"]
EXPOSE 5002