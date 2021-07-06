
#!/bin/bash
set -euxo pipefail
CHARTS_FOLDER=charts/kubemq-test-drive
MAIN_BRANCH=remotes/origin/main

# renovate: datasource=github-releases depName=kubeval lookupName=instrumenta/kubeval
KUBEVAL_VERSION=v0.16.1

CHART_DIRS="$(git diff --find-renames --name-only "$(git rev-parse --abbrev-ref HEAD)" ${MAIN_BRANCH} -- ${CHARTS_FOLDER} | grep '[cC]hart.yaml' | sed -e 's#/[Cc]hart.yaml##g')"
SCHEMA_LOCATION="https://raw.githubusercontent.com/instrumenta/kubernetes-json-schema/master/"

# install kubeval
curl --silent --show-error --fail --location --output /tmp/kubeval.tar.gz https://github.com/instrumenta/kubeval/releases/download/"${KUBEVAL_VERSION}"/kubeval-linux-amd64.tar.gz
tar -xf /tmp/kubeval.tar.gz kubeval

# add helm repos
helm repo add bitnami https://charts.bitnami.com/bitnami

# validate charts
for CHART_DIR in ${CHART_DIRS}; do
  (cd ${CHART_DIR}; helm dependency build) # This may not be necesary
  # Add variablres for the tag of images
  helm template --values "${CHART_DIR}"/ci/ci-values.yaml "${CHART_DIR}" | ./kubeval --strict --ignore-missing-schemas --kubernetes-version "${KUBERNETES_VERSION#v}" --schema-location "${SCHEMA_LOCATION}"
done
