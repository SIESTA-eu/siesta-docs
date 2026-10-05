# S3 storage

SIESTA provides S3-compatible storage through MinIO deployed in the IFCA cluster. This storage is preconfigured in Onyxia and can be managed directly from the dashboard's [**File Explorer**](https://dashboard.cloud.eosc-siesta.eu/file-explorer) section. Onyxia uses temporary S3 credentials to access compatible storage; see the official Onyxia documentation for its [S3 integration](https://docs.onyxia.sh/admin-doc/readme/data-s3) and [file browser](https://docs.onyxia.sh/docs.onyxia.sh/v9/user-doc/user-guide#file-browser).

S3 storage quotas vary by access group. Your assigned group determines the quota available to your account. See [Roles and permissions](roles.md) for the group definitions and quota table.

## Access storage from a service

Services that support S3 receive the credentials for the user's bucket automatically as environment variables. Depending on the service, these typically include `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_DEFAULT_REGION`, `AWS_S3_ENDPOINT`, and `AWS_BUCKET_NAME`. The exact options and variable names are shown in the service launch form and are controlled by its catalog chart.

Some services also offer an S3-synchronized volume. When this option is enabled before launch, the service can access the bucket through a directory in its file system instead of calling the S3 API directly. Check the service's S3 configuration and launch notes for the mount path.

```{figure} /_static/connect_to_storage.png
:alt: Onyxia service launch form showing temporary S3 credentials and connection settings
:width: 100%

S3 configuration available when launching a compatible service. Secret values remain masked in the interface.
```

```{note}
The temporary S3 credentials expire after six months. Generate fresh credentials when the current set expires, and do not store credentials in source code, notebooks, container images, or shared files.
```

## Connect from an external tool

Open [**My account**](https://dashboard.cloud.eosc-siesta.eu/account) in Onyxia and select **Connect to storage**. This page shows the current S3 credentials and ready-to-use commands for supported clients. Treat the access key, secret key, and session token as sensitive information.

You can also open the [MinIO Console](https://minio-console.cloud.eosc-siesta.eu/login) and authenticate with SIESTA's Keycloak SSO to browse the bucket.

## Browse files in Onyxia

```{figure} /_static/dashboard_storage2.png
:alt: SIESTA dashboard File Explorer showing available storage spaces
:width: 100%

Example of the storage spaces available in the dashboard's **File Explorer** section.
```

```{figure} /_static/dashboard_storage.png
:alt: SIESTA dashboard File Explorer showing folders in a storage space
:width: 100%

Example of folders in the user storage (dashboard view).
```

```{figure} /_static/minio_example.png
:alt: MinIO view of the user storage
:width: 100%

Example of folders in the user storage (MinIO view).
```
