FROM python:3.7-alpine
COPY src/ ./src/
RUN pip install pytest
WORKDIR /src/test
CMD ["python", "test_service.py"]
