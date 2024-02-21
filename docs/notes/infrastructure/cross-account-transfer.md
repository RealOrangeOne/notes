---
title: Cross-account data transfer
tags:
  - AWS
sources:
  - https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/
  - https://stackoverflow.com/a/63804619
---

To copy bucket contents from a bucket in account A to a bucket in account B:

1. Create new S3 bucket in account B
2. Create IAM role / user in account B, with access to destination bucket
3. Add IAM inline policy to the newly-created user:

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

Now, you can run `aws s3 sync` as the account in account B, and access both buckets.

!!! warning
     Whilst it might seem counter-intuitive, a **pull**-based transfer is significantly simpler than a **push**-based transfer. Notably, it avoids [issues](https://stackoverflow.com/a/63804619) with ownership issues and ACLs.

     These can be solved by overwriting the file's ACLs to enforce the bucket owner owns the file:

     ```
     aws s3 cp --recursive 's3://<destination_bucket>` 's3://<destination_bucket>` --acl bucket-owner-full-control --metadata-directive REPLACE
     ```
