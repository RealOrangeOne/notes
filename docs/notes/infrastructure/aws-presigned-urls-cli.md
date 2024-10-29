---
title: Create presigned URLs using AWS CLI
tags:
  - AWS
sources:
  - https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html
---

Sometimes, you only have access to the `aws` CLI, and need to generate presigned URLs to S3 objects.

The `aws s3 presign` command will do this, creating URLs signed as the currently-authenticated user.

```bash
export AWS_ACCESS_KEY_ID=xxx AWS_SECRET_ACCESS_KEY=xxx
aws s3 presign --expires-in 3600 s3://my-bucket/file.txt
```

!!! note
    URLs are signed with a region of `us-east-1`. Pass `--region` or set `$AWS_REGION` to override. URLs with the wrong region are not valid.
