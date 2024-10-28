---
title: Using the AWS CLI without installing it
tags:
  - AWS
sources:
  - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
---

The official AWS CLI installation steps require downloading and running a script to install the CLI. This download contains the CLI itself, and the install script simply copies it to the right places.

However, especially for one-off uses, it's quite convenient to not run it at all, and run it as-is:

1\. Download the CLI:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
```

2\. Make the CLI itself executable:

```bash
chmod +x ./aws/dist/aws
```

3\. Run the CLI:

```bash
./aws/dist/aws help
```
