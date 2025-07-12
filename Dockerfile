FROM python:3.14-rc-bookworm AS builder
WORKDIR /opt/sex_mans
COPY Requirements.txt ./
RUN pip3 install --no-cache-dir -r Requirements.txt

FROM python:3.14-rc-slim-bookworm
WORKDIR /opt/sex_mans
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY main.py .
COPY .env .
CMD ["python", "main.py"]
