FROM python:3.7-alpine
WORKDIR /base
ENV FAST_API=main.py
ENV FAST_API_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5100
COPY . .
CMD ["uvicorn", "main:app", "--reload"]
