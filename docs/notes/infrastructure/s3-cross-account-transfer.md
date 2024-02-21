---
title: Cross-account data transfer in S3
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

## ACLs

Whilst it might seem counter-intuitive, a **pull**-based transfer is significantly simpler than a **push**-based transfer. Notably, it avoids [issues](https://stackoverflow.com/a/63804619) with ownership issues and ACLs. Bucket policies don't seem to apply if the object is owned by a different account, which is the case when ACLs are enabled and the object is written by a user not in the organisation (hence pull-based being best).

These can be solved by overwriting the file's ACLs to enforce the bucket owner owns the file:

```
aws s3 cp --recursive 's3://<destination_bucket>` 's3://<destination_bucket>` --acl bucket-owner-full-control --metadata-directive REPLACE
```

It's then good practice to make sure the ACLs are as you expect (eg [`./manage.py fix_document_acls`](https://github.com/torchbox/wagtail-storages?tab=readme-ov-file#django-admin-fix_document_acls)).
