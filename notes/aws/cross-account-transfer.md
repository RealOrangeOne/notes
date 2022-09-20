---
title: Cross-account data transfer
tags:
  - AWS
link: https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/
emoji: 🪣
---

To copy bucket contents from bucket in account A to bucket in account B:

1. Create new S3 bucket in account B
2. Create IAM role / user in account B, with access to destination bucket
3. Add IAM inline policy to user:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::<source_bucket>/*",
        "arn:aws:s3:::<source_bucket>"
      ]
    }
  ]
}
```

4. Add policy to source bucket

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<account_id>:user/<user>"
      },
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::<source_bucket>/*", "arn:aws:s3:::<source_bucket>"]
    }
  ]
}
```
