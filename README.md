Demo Charm
==========

It's new! It's shiny! It's definitely buggy!


This is just a charm that I'm using to learn the Operator Framework.


Installation
------------

```
sudo snap install juju --classic
sudo snap install microk8s --classic
sudo microk8s.enable dns dashboard registry storage
sudo usermod -a -G microk8s ubuntu
```

Log out, log back in.

```
juju bootstrap microk8s mk8s
```

Optional: Grab coffee/beer/tea or do a 5k run

```
juju create-storage-pool operator-storage kubernetes storage-class=microk8s-hostpath
juju add-model demo-charm
juju deploy .
```

Developing
----------

We do charm unit testing in this here parts. We're not savages.

```
pip install tox
tox
```

Check out how tests are written in the `test/` dir.
