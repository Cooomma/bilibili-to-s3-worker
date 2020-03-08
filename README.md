# bilibili-to-s3-worker
Download Video from Bilibili, Change video container, and Upload to S3

## Prerequisites
* FFmpeg
* [Annie](https://github.com/iawia002/annie)

## Docker

Build docker image:

```bash
docker build . -t bilibili-to-s3-worker 
```

Use image:

```bash
docker run --rm --interactive \
    -e AWS_ACCESS_KEY_ID=${YOUR_AWS_ACCESS_KEY_ID} \
    -e AWS_SECRET_ACCESS_KEY=${YOUR_AWS_SECRET_ACCESS_KEY} \
    bilibili-to-s3-worker worker ${BILIBILI_VIDEO_ID} ${S3_BUCKET} ${S3_PREFIX}
```
