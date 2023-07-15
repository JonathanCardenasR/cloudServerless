FROM --platform=linux/amd64 python:3.9
ADD funSacar.py .
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "./funSacar.py"]