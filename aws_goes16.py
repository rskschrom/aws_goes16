import boto3
from numpy import array, argmin, abs
from datetime import datetime
import os

# set up access to aws server
s3 = boto3.resource('s3')
bucket = s3.Bucket('noaa-goes16')

# set date range
now = datetime.utcnow()
yyyy = now.year
mm = now.month
dd = now.day
hh = now.hour
doy = datetime(yyyy, mm, dd).timetuple().tm_yday

# filter data
product = 'ABI-L2-CMIPF'
fstr = 'OR_ABI-L2-CMIPF-M3C16'
prefix = '{}/{:04d}/{:03d}/{:02d}/{}'.format(product, yyyy, doy, hh, fstr)

objs = bucket.objects.filter(Prefix=prefix)
keys = [o.key for o in objs]
fnames = [k.split('/')[-1] for k in keys]

dkey = keys[-1]
dfile = fnames[-1]
print dfile, dkey

# download data
s3_client = boto3.client('s3')
s3_client.download_file('noaa-goes16', dkey, dfile)
