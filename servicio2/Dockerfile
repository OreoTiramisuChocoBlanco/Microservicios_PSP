FROM python:3.9-alpine
WORKDIR /servicio2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
EXPOSE 5001