# Roles and permissions

Access to SIESTA catalogs and S3 storage is managed by group. Your group membership determines which catalogs you can access and the quota assigned to your S3 bucket.

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

## Group administration

SIESTA's Keycloak deployment uses the [RCIAM group-management plugin](https://rciam.github.io/rciam-docs/docs/manager/group-management/). A **group admin** is an administrative designation, not a role inside the group. Users designated as group admins can manage the groups for which they have been granted that permission.

```{figure} /_static/keycloak_group_management.png
:alt: RCIAM Group Management page listing the groups administered by the signed-in user
:width: 100%

The **Group Management** page lists the groups that the signed-in group admin can manage.
```

### Invite users to a group

A group admin can create and share an enrollment link:

1. Sign in to the [SIESTA Keycloak Account Console](https://aai.cloud.eosc-siesta.eu/realms/siesta/account/) and open **Group Management**.
2. Find the group and open its actions menu.
3. Select **Enrolment Discovery Page Link**.
4. Share the link with the intended users. After signing in, each user can submit a request to join the group.

An enrollment configuration determines which roles are available and whether an administrator must approve each request. See the RCIAM instructions for [adding group members by enrollment request](https://rciam.github.io/rciam-docs/docs/manager/group-management/#by-enrollment-request).

```{figure} /_static/keycloak_group_enrollment_link.png
:alt: RCIAM group details showing the enrollment discovery link and group roles
:width: 100%

The group details page provides the enrollment discovery link and controls for managing group-specific roles.
```

### Review participation requests

When an enrollment requires approval, group admins receive a notification and can review it from **Group Management** > **Review Enrollment Requests**. Open the pending request, verify the user, requested group and roles, and then approve or reject it. RCIAM documents the complete [enrollment-request review flow](https://rciam.github.io/rciam-docs/docs/manager/group-management/#review-enrollment-request).

```{figure} /_static/keycloak_enrollment_requests.png
:alt: RCIAM Review Enrollment Requests page showing a request pending approval
:width: 100%

The **Review Enrollment Requests** page lists requests that require a group admin's decision.
```

### Create group-specific roles

Group admins can create roles from the group's details page and assign them to group members or make them available through an enrollment configuration. The resulting entitlement values are included in the user's Keycloak tokens under the `eduperson_entitlement` claim. 

```{important}
These roles can only be used by an application that authenticates its users and reads the `eduperson_entitlement` claim from their token. Merely launching an application as an Onyxia service does not make the application enforce these roles. The application must include a user login flow and map the entitlement values to its own authorization rules.
```

## S3 quota by group

| Group | S3 storage quota |
|---|---:|
| `access:ap-u` | Unlimited |
| `access:ap-d` | 10 GiB |
| `access:ap-b` | 5 GiB |
| `access:ap-a1` | 250 MiB |
| `access:ap-a` | 250 MiB |
| `access:ap-0` | 250 MiB |

The quotas come from the SIESTA deployment's [MinIO bucket-quota configuration](https://gitlab.ifca.es/eosc-siesta/siesta-deployment/-/blob/main/clusters/siesta-cluster/apps/minio-bucket-quota.yaml?ref_type=heads). Accounts without one of the explicitly matched access roles receive the default quota of 250 MiB. If an account has multiple matching roles, the deployment applies the first match in this order: `ap-u`, `ap-b`, `ap-d`, `ap-a1`, and `ap-a`. Quotas are reconciled hourly, so a role change may not be reflected immediately.
