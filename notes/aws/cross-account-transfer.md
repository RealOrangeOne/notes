---
title: Cross-account data transfer
tags:
  - AWS
link: https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/
emoji: 🪣
---

1. Create S3 bucket in account A
2. Create IAM role / user in account B
3. Add IAM inline policy to user:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "arn:aws:s3:::<bucket>/*"

        }
    ]
}
```

4. Add policy to bucket

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account_id>:user/<user>"
            },
            "Action": "*",
            "Resource": [
                "arn:aws:s3:::<bucket>/*"
            ]
        }
    ]
}
```
