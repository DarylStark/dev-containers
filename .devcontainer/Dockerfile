# [Choice] Python version (use -bookworm or -bullseye variants on local arm64/Apple Silicon): 3, 3.11, 3.10, 3.9, 3.8, 3-bookworm, 3.11-bookworm, 3.10-bookworm, 3.9-bookworm, 3.8-bookworm, 3-bullseye, 3.11-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3-buster, 3.11-buster, 3.10-buster, 3.9-buster, 3.8-buster
FROM python:3.11

RUN apt-get update

# Temporary: Upgrade python packages due to https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40897
# They are installed by the base image (python) which does not have the patch.
RUN python3 -m pip install --upgrade setuptools pip

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY src/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

