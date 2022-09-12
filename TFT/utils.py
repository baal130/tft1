from storages.backends.s3boto3 import S3Boto3Storage
import datetime 
import os
import random
import string

from django.utils import timezone
from django.utils.text import slugify

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media')