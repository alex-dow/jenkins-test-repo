# jenkins-test-repo

This is a simple repo to test Jenkins stuff such as Github integration, report publishing and various other features, as well as github workflows.

For this repository, the workflow is:

Assumed Workflow:
1. Master branch is current release
2. New release comes from a merge of the develop branch into master
3. Changes are created in separate branches
4. Pull requests are made from those separate branches into develop
5. Develop is merged into master for next release
6. Jenkins should build everything here

Github Side:
1. Generate a personal access token: https://github.com/settings/tokens
2. Goto repository settings, select webhooks
3. Payload url is [jenkins-url]/github-webhook
4. Select push events

Jenkins Side:
1. Configure job to use git
2. Set branch specifier to blank or **
3. use GitHub hook trigger for build trigger
4. Add build task to set status to pending on Github
5. Add post-build task to set github status (universal)

I got it all working, nice.
