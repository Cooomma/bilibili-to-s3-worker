## Build Annie
FROM golang:1.14.0-buster as annie_builder
WORKDIR /builder
RUN git clone https://github.com/iawia002/annie.git && \
    cd annie && \
    go build . 

FROM python:3.8.2-slim-buster
RUN apt update && apt install -y --no-install-recommends ffmpeg awscli
COPY --from=annie_builder /builder/annie/annie /usr/bin/annie
COPY ./worker.py /usr/bin/worker
RUN chmod 755 /usr/bin/worker
CMD [ "/usr/bin/worker" ]