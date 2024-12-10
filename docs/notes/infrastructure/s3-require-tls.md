---
title: Enforce TLS for S3
tags:
  - AWS
sources:
  - https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/
---

IAM policies can have a `Condition`, which must pass for the policy to apply. This can be used to require HTTPS and/or the TLS version:


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3::my-bucket/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                 },
                "NumericGreaterThanEquals": {
                    "s3:TlsVersion": [
                        "1.2"
                    ]
                }
            }
        }
    ]
}
```

The above policy allows anyone to access an object, so long as their connection is both secure and using TLS 1.2+.

!!! warning
    When enforcing HTTPS, S3 will **not** perform a redirect. A HTTP connection is just shown as a 403 (since the policy didn't apply).

    If you need a redirect, it's best to handle this using CloudFront.

## ACLs

If the object is made public by an ACL rather than a rule, the policy condition has no effect. Instead, use a Deny rule to block insecure access.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyOutdatedTLS",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "arn:aws:s3::my-bucket/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                },
                "NumericLessThan": {
                    "s3:TlsVersion": [
                        "1.2"
                    ]
                }
            }
        },
        {
            "Sid": "DenyHTTP"
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "arn:aws:s3::my-bucket/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                },
            }
        }
    ]
}
```
