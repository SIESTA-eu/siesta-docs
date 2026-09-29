# Roles and permissions

Access to SIESTA catalogs and S3 storage is managed by group. Your group membership determines which catalogs you can access.

## Access levels and group membership

The access-level definitions follow the [AI4EOSC access-level reference](https://docs.ai4eosc.eu/en/latest/reference/user-access-levels.html). The following groups are available:

### Basic access (`ap-0`)

Granted to any registered user, for example users registered via [GitHub](https://github.com/), [Google](https://accounts.google.com/), [IFCA SSO](https://sso.ifca.es/), or [ORCID](https://orcid.org/).

### EduGAIN access groups

- **`ap-a`**: any person with EduGAIN credentials.
- **`ap-a1`**: any person with EduGAIN credentials who is employed by an organization. This is a more specific category within `ap-a`.
- **`ap-b`**: any person with EduGAIN credentials who is employed as a researcher. This is a more specific category within `ap-a1`.

### Full access groups

- **`ap-u`**: members of the project.
- **`ap-d`**: developers.

## S3 quota by group

| Group | S3 storage quota |
|---|---:|
| `access:ap-u` |  |
| `access:ap-d` |  |
| `access:ap-a` |  |
| `access:ap-a1` |  |
| `access:ap-b` |  |
| `access:ap-0` |  |
