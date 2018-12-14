# talkshow

[![Build Status](https://travis-ci.com/rochacbruno/talkshow.svg?branch=extended)](https://travis-ci.com/rochacbruno/talkshow)
[![codecov](https://codecov.io/gh/rochacbruno/talkshow/branch/extended/graph/badge.svg)](https://codecov.io/gh/rochacbruno/talkshow)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/rochacbruno/talkshow.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/rochacbruno/talkshow/context:python)

A Call 4 Papers System - A simple base app as example of Flask Architecture

Este é o material do tutorial da Flask Conf 2018 - O evento ocorreu no dia 24/08/2018 - com Patrocinio da SciELO

## Apostila

A Apostila em PDF contém a explicação detalhada dos arquivos deste repositório, é recomendado acompanhar a apostila enquanto desenvolve o projeto e utilizar este repositório apenas como referencia para copy/paste.

Apostila:  https://github.com/rochacbruno/talkshow/blob/master/TutorialFlaskConf2018_BrunoRocha.pdf 

Código para acompanhar a apostila está na branch `master` https://github.com/rochacbruno/talkshow/tree/master

> IMPORTANTE: Alterações e evoluções nesta aplicações serão feitas apenas nesta branch `extended` a branch `master` se manterá em sincronia com a apostila.

## TL:DR;

Não quer acompanhar a apostila e apenas ver o código em execução?

```
git clone https://github.com/rochacbruno/talkshow.git
cd talkshow
git checkout extended
python3.6 -m venv venv
source venv/bin/activate
pip install -e '.[dev]'

#comandos
flask adduser -u admin -p 1234
flask addevent -n "Flask Conf" -d "2018-08-25"
flask routes
flask run
```

Acesse: http://localhost:5000 para ver os eventos cadastrados e submeter propostas

Admin em http://localhost:5000/admin user:admin pass:1234

API em http://localhost:5000/apidocs/


URLS e APIS:

```bash
$ flask routes
Endpoint                   Methods    Rule
-------------------------  ---------  -----------------------------------------
admin.index                GET        /admin/
admin.static               GET        /admin/static/<path:filename>
bootstrap.static           GET        /static/bootstrap/<path:filename>
flasgger.<lambda>          GET        /apidocs/index.html
flasgger.apidocs           GET        /apidocs/
flasgger.apispec_1         GET        /apispec_1.json
flasgger.static            GET        /flasgger_static/<path:filename>
proposalview.action_view   POST       /admin/proposalview/action/
proposalview.ajax_lookup   GET        /admin/proposalview/ajax/lookup/
proposalview.ajax_update   POST       /admin/proposalview/ajax/update/
proposalview.create_view   GET, POST  /admin/proposalview/new/
proposalview.delete_view   POST       /admin/proposalview/delete/
proposalview.details_view  GET        /admin/proposalview/details/
proposalview.edit_view     GET, POST  /admin/proposalview/edit/
proposalview.export        GET        /admin/proposalview/export/<export_type>/
proposalview.index_view    GET        /admin/proposalview/
restapi.event              GET, POST  /api/v1/event/
restapi.eventitem          GET, POST  /api/v1/event/<event_id>
simplelogin.login          GET, POST  /login/
simplelogin.logout         GET        /logout/
static                     GET        /static/<path:filename>
webui.event                GET, POST  /<slug>/
webui.index                GET        /

```

Contribuições são bem vindas na branch `extended`
