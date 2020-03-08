#!/usr/bin/python3

import argparse
import os
import pathlib
import shutil


def download(video_id: str, tmp_dir: str):
    os.system('annie -p -o {tmp_dir} {video_id}'.format(tmp_dir=tmp_dir, video_id=video_id))


def transcode(tmp_dir: str):
    for index, file in enumerate(os.listdir(tmp_dir), start=1):
        source_filepath = os.path.join(tmp_dir, file)
        new_filepath = os.path.join(tmp_dir, '{}_ep{}{}'.format(
            video_id.lower(), str(index).zfill(3), pathlib.Path(file).suffix))
        output_filepath = os.path.join(tmp_dir, '{}_ep{}.mp4'.format(video_id.lower(), str(index).zfill(3)))
        os.rename(source_filepath, new_filepath)
        os.system('ffmpeg -y -i {input} -c copy {output}'.format(input=new_filepath, output=output_filepath))
        os.remove(new_filepath)


def upload(tmp_dir: str, bucket: str, prefix: str):
    os.system('aws s3 cp {tmp_dir} s3://{bucket}/{prefix} --recursive'.format(
        tmp_dir=tmp_dir, bucket=bucket, prefix=prefix,
    ))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bucket', help='S3 Bucket')
    parser.add_argument('-p', '--prefix', help='S3 Object Prefix')
    parser.add_argument('id', help='Bilibili Video ID')
    args = parser.parse_args()
    video_id = args.id
    bucket = args.bucket
    if args.prefix:
        prefix = '{}/{}/'.format(args.prefix, video_id)
    else:
        prefix = video_id + '/'

    tmp_dir = os.path.abspath(os.path.join('/tmp/{}'.format(video_id)))

    # print(video_id)
    # print(bucket, prefix)
    # print(tmp_dir)

    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)

    download(video_id, tmp_dir)
    transcode(tmp_dir)
    upload(tmp_dir=tmp_dir, bucket=bucket, prefix=prefix)
    shutil.rmtree(tmp_dir)
