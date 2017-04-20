[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/LREN-CHUV/ansible-airflow/blob/master/LICENSE) [![CircleCI](https://circleci.com/gh/LREN-CHUV/ansible-airflow.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/ansible-airflow) [![wercker status](https://app.wercker.com/status/9bab59ff38cd2dbf9f5ef1949fa75692/s/master "wercker status")](https://app.wercker.com/project/byKey/9bab59ff38cd2dbf9f5ef1949fa75692)

# ansible-airflow

Installs Airflow using Ansible.

This Ansible role also supports starting Ansible using Marathon. In this case, specify with the variable `marathon_version` the version of Marathon used.

Supported systems:

* Ubuntu 16.04
* RedHat/Centos 7.2
## Continuous integration

This project uses two different continuous integration services to test different aspects of the project.

CircleCI: [![CircleCI](https://circleci.com/gh/LREN-CHUV/ansible-airflow.svg?style=svg)](https://circleci.com/gh/LREN-CHUV/ansible-airflow)

CircleCI to validate the syntax of Ansible scripts using ansible-lint.

[![wercker status](https://app.wercker.com/status/9bab59ff38cd2dbf9f5ef1949fa75692/m/master "wercker status")](https://app.wercker.com/project/byKey/9bab59ff38cd2dbf9f5ef1949fa75692)

Werker to validate the installation of Airflow.
