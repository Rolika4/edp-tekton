# edp-tekton

![Version: 0.1.0-SNAPSHOT](https://img.shields.io/badge/Version-0.1.0--SNAPSHOT-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0-SNAPSHOT](https://img.shields.io/badge/AppVersion-0.1.0--SNAPSHOT-informational?style=flat-square)

A Helm chart for EDP Tekton Pipelines

**Homepage:** <https://epam.github.io/edp-install/>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| epmd-edp | <SupportEPMD-EDP@epam.com> | <https://solutionshub.epam.com/solution/epam-delivery-platform> |
| sergk |  | <https://github.com/SergK> |

## Source Code

* <https://github.com/epam/edp-tekton>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| fullnameOverride | string | `""` |  |
| gerrit.enabled | bool | `true` | Deploy Gerrit related components. Default: true |
| gerrit.sshPort | int | `30003` | Gerrit port |
| github.accountName | string | `"GitHub Account Name"` |  |
| github.enabled | bool | `false` |  |
| github.repositoryName | string | `"GitHub Repository Name"` |  |
| github.webhookSecret.secretString | string | `"random-string-data"` |  |
| github.webhookSecret.token | string | `"123"` |  |
| gitlab.enabled | bool | `false` |  |
| gitlab.host | string | `"git.epam.com"` | The GitLab host, adjust this if you run a GitLab enterprise. Default: gitlab.com |
| gitlab.repositoryName | string | `"epmd-edp/temp/tekton-petclinic"` |  |
| gitlab.webhookSecret.secretString | string | `"random-string-data-123"` | Generated on Tekton side and populated in GitLab for each Project in section: PROJECT_NAME > Settings > Webhooks > Secret Token |
| gitlab.webhookSecret.token | string | `"generated_on_gitlab_side"` | Generated on GitLab side in section: (User Settings) or (Project Settings) or (Group Settings) > Access Token |
| global.dnsWildCard | string | `"eks-sandbox.aws.main.edp.projects.epam.com"` | a cluster DNS wildcard name |
| kaniko.roleArn | string | `"arn:aws:iam::093899590031:role/AWSIRSACoreSandboxEdpDeliveryKaniko"` | AWS IAM role to be used for kaniko pod service account (IRSA). Format: arn:aws:iam::<AWS_ACCOUNT_ID>:role/<AWS_IAM_ROLE_NAME> |
| kaniko.serviceAccount.create | bool | `false` | Specifies whether a service account should be created |
| nameOverride | string | `""` |  |
| tekton.pruner.create | bool | `true` | Specifies whether a cronjob should be created |
| tekton.pruner.keep | int | `1` | Maximum number of resources to keep while deleting removing |
| tekton.pruner.resources | string | `"pipelinerun,taskrun"` | Supported resources for auto prune are 'taskrun' and 'pipelinerun' |
| tekton.pruner.schedule | string | `"0 18 * * *"` | How often to clean up resources |