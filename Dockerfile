FROM python:3.7-alpine
WORKDIR /src
RUN python test/test_service.py
