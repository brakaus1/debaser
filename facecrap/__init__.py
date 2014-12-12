import urllib
import cStringIO
import base64
from hashlib import md5
import time
import click
from facecrap.single import cager
from facecrap.multiple import switcheroo

def Root(path):
    """Returns the key root for the resource in S3"""
    key = base64.b64encode(md5(path.split('.')[0]).digest(), altchars='!*')[:7]
    return key

@click.command()
@click.option("--picture1", "-p1", required=True, type=str)
@click.option("--picture2", "-p2", type=str)
def handler(picture1, picture2):

    if picture2:
        if 'http' in picture1:
            key = '/tmp/' + Root(picture1)
            with open(key, 'wb') as f:
                f.write(urllib.urlopen(picture1).read())
            picture1 = key
        if 'http' in picture2:
            key = '/tmp/' + Root(picture2)
            with open(key, 'wb') as f:
                f.write(urllib.urlopen(picture2).read())
            picture2 = key
        switcheroo(picture1, picture2)
        switcheroo(picture2, picture1)
    else:
        if 'http' in picture1:
            key = '/tmp/' + Root(picture1)
            with open(key, 'wb') as f:
                f.write(urllib.urlopen(picture1).read())
            picture1 = key
        cager(picture1)
