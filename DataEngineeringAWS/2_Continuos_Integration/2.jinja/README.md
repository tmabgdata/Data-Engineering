# Using GitHub Actions

How to use:
1. Set your AWS credentials within your repository on GitHub.
    
    1. Access the repository and go to settings -> secrets
    
    1. Add the credentials of a user who has sufficient permissions to deploy Cloudformation templates
    
        a. `AWS_ACCESS_KEY_ID`
    
        b. `AWS_DEFAULT_REGION`
    
        c. `AWS_SECRET_ACCESS_KEY`
    
    1. Add required environment variables

        a. `redshiftClusterMasterUsername`
    
        b. `redshiftClusterMasterUserPassword`

## Deploy for staging
1. Create a branch called `2.jinja_staging`
    
    1. `git checkout -b 2.jinja_staging`

2. The file that will control this workflow is in `.github/workflows/2.jinja_staging.yml`
    
    1. Create a commit and push to your remote repository
    
    1. The workflow will be executed when pushing to branch `2.jinja_staging`

3. Watch GitHub deploy your infrastructure within the **Actions** tab


## Deploy to production
1. Create a branch called `2.jinja_production`
     
    1. `git checkout -b 2.jinja_production`

2. The file that will control this workflow is in `.github/workflows/2.jinja_production.yml`

    1. Create a commit and push to your remote repository

    1. The workflow will be executed when pushing to branch `2.jinja_production`

3. Watch GitHub deploy your infrastructure within the **Actions** tab


**Remember to always delete your stacks after class to avoid unexpected charges on your AWS**