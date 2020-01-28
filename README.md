Demo Charm
==========

This is a demo charm that I'm using to learn the Operator Framework.
It's new! It's shiny! It's definitely buggy!


Installation
------------

```
sudo snap install juju --classic
sudo snap install microk8s --classic
sudo microk8s.enable dns dashboard registry storage
juju bootstrap microk8s mk8s
juju create-storage-pool operator-storage kubernetes storage-class=microk8s-hostpath
juju add-model demo-charm
juju deploy .
```
