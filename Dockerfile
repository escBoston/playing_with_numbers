FROM python:3.7-alpine
COPY src/ ./src/
WORKDIR /src/test
CMD ["python", "test_service.py"]
