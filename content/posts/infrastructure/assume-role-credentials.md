---
title: Get credentials for an assumed role
tags:
  - AWS
sources:
  - https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/
---

It's often useful to get regular access keys as if you were assumed into another role. This is possible:

```
aws sts assume-role --role-arn arn:aws:iam::<account>:role/<role> --role-session-name <name>
```

This produces JSON output (it's the most readable of the 3 `aws` supports):

```json
{
    "Credentials": {
        "AccessKeyId": "xxxxxxxxxxxxxxx",
        "SecretAccessKey": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "SessionToken": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Expiration": "2022-09-13T17:18:44Z"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "xxxxxxxxxxxxxxxx:<name>",
        "Arn": "arn:aws:sts::<account>:assumed-role/<role>/<name>"
    }
}
```

See also the [`assume-role`](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html) command's docs
