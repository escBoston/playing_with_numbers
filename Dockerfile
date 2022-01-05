FROM python:3.7-alpine
COPY src/ ./src/
WORKDIR /src/test
#COPY *.py ./
CMD ["python", "test_service.py"]
