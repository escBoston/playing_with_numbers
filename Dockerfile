FROM python:3.7-alpine
WORKDIR /src/test
COPY *.py ./
CMD ["python", "test_service.py"]
