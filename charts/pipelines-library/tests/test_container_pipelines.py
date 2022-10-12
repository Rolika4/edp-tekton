import os
import sys

from .helpers import helm_template


def test_container_pipelines_gerrit():
    config = """
gerrit:
  enabled: true
    """

    r = helm_template(config)

    assert "gerrit-kaniko-docker-lib-review" in r["pipeline"]
    assert "gerrit-kaniko-docker-lib-build-default" in r["pipeline"]
    assert "gerrit-kaniko-docker-lib-build-edp" in r["pipeline"]

    # ensure pipelines have proper steps
    for buildtool in ['kaniko']:
        for framework in ['docker']:

            gerrit_review_pipeline = f"gerrit-{buildtool}-{framework}-lib-review"
            gerrit_build_pipeline_def = f"gerrit-{buildtool}-{framework}-lib-build-default"
            gerrit_build_pipeline_edp = f"gerrit-{buildtool}-{framework}-lib-build-edp"

            rt = r["pipeline"][gerrit_review_pipeline]["spec"]["tasks"]
            assert "fetch-repository" in rt[0]["name"]
            assert "gerrit-notify" in rt[1]["name"]
            assert "init-values" in rt[2]["name"]
            assert "fetch-target-branch" in rt[3]["name"]
            assert "dockerfile-lint" in rt[4]["name"]
            assert "dockerbuild-verify" in rt[5]["name"]
            assert "gerrit-vote-success" in r["pipeline"][gerrit_review_pipeline]["spec"]["finally"][0]["name"]
            assert "gerrit-vote-failure" in r["pipeline"][gerrit_review_pipeline]["spec"]["finally"][1]["name"]

            # build with default versioning
            btd = r["pipeline"][gerrit_build_pipeline_def]["spec"]["tasks"]
            assert "fetch-repository" in btd[0]["name"]
            assert "gerrit-notify" in btd[1]["name"]
            assert "init-values" in btd[2]["name"]
            assert "get-version" in btd[3]["name"]
            assert f"get-version-{buildtool}-default" == btd[3]["taskRef"]["name"]
            assert "dockerfile-lint" in btd[4]["name"]
            assert "create-ecr-repository" in btd[5]["name"]
            # ensure we have default versioning
            assert "kaniko-build" in btd[6]["name"]
            assert buildtool == btd[6]["taskRef"]["name"]
            assert "git-tag" in btd[7]["name"]
            assert "update-cbis" in btd[8]["name"]

            # build with edp versioning
            btedp = r["pipeline"][gerrit_build_pipeline_edp]["spec"]["tasks"]
            assert "fetch-repository" in btedp[0]["name"]
            assert "gerrit-notify" in btedp[1]["name"]
            assert "init-values" in btedp[2]["name"]
            assert "get-version" in btedp[3]["name"]
            assert "get-version-edp" == btedp[3]["taskRef"]["name"]
            assert "dockerfile-lint" in btedp[4]["name"]
            assert "create-ecr-repository" in btedp[5]["name"]
            assert "kaniko-build" in btedp[6]["name"]
            assert "git-tag" in btedp[7]["name"]
            assert "update-cbis" in btedp[8]["name"]