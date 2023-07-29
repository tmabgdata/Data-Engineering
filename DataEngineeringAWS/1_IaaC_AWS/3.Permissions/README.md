# Managing access and permissions with IAM

Deploy:
1. Navigate to the Cloudformation page on your AWS console
2. Click on create stack -> with new resources
3. Upload the file and follow the instructions to deploy

To test:
1. With admin access, create a user and add him to the `iam-group-data-engineer` group
2. Log into your AWS dashboard with the credentials of this new user that was added to the group.
3. Click on your username in the top right menu
4. Click Switch Roles
5. Fill in the fields:
   1. Account: your AWS account number (12 digits)
   1. Role: `role-production-data-engineer`
   1. Display Name: Name of your choice eg `Data Engineer`
    
This user has now assumed the `role-production-data-engineer` role and only has the permissions described within the `IamPolicyDataEngineer` policy.

Use this to separate permissions for different groups of users: Analysts, Developers, Data Scientists, Admins, etc.