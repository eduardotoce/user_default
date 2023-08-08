FROM python:3.11
WORKDIR /usr/src/app
COPY ./* /usr/src/app
COPY src /usr/src/app
COPY data /usr/src/app
COPY models /usr/src/app
RUN pip install -r requirements.txt
ENV PYTHONPATH=/usr/src/app
CMD ["python", "main.py"]