FROM python:3.7-alpine
WORKDIR /src/test
RUN python test_service.py
