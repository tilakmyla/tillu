
# Apache ZooKeeper Ansible role [![Build Status](https://travis-ci.org/idealista/zookeeper-role.png)](https://travis-ci.org/idealista/zookeeper-role)

This ansible role installs an Apache ZooKeeper service in a debian environment.

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an Apache ZooKeeper server.

### Prerequisities

Ansible 2.4.0.0 version installed.
Inventory destination should be a Debian environment.

Notice that automatically java is installed as dependency.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.zookeeper-role
  version: 1.0.0
  name: zookeeper
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: zookeeper
      }
```

## Usage

To set multiple versions

```
zookeeper_hosts:
  - host: zookeeper1
    id: 1
  - host: zookeeper2
    id: 2
  - host: zookeeper3
    id: 3
```

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.
