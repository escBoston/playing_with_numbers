FROM python:3.7-alpine
WORKDIR /src/test
COPY test_service.py .
CMD ["python", "test_service.py"]
