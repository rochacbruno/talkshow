# talkshow

[![Build Status](https://travis-ci.com/rochacbruno/talkshow.svg?branch=extended)](https://travis-ci.com/rochacbruno/talkshow)

A Call 4 Papers System - A simple base app as example of Flask Architecture

Este é o material do tutorial da Flask Conf 2018 - O evento ocorreu no dia 24/08/2018 - com Patrocinio da SciELO

## Apostila

A Apostila em PDF contém a explicação detalhada dos arquivos deste repositório, é recomendado acompanhar a apostila enquanto desenvolve o projeto e utilizar este repositório apenas como referencia para copy/paste.

Apostila:  https://github.com/rochacbruno/talkshow/blob/master/TutorialFlaskConf2018_BrunoRocha.pdf 

## TL:DR;

Não quer acompanhar a apostila e apenas ver o código em execução?

```
git clone https://github.com/rochacbruno/talkshow.git
cd talkshow
python3.6 -m venv venv
source venv/bin/activate
pip install -e .
pip install -e .[dev]

#comandos
flask adduser -u admin -p 1234
flask addevent -n "Flask Conf" -d "2018-08-25"
flask routes
flask run
```

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

Uma versão `evoluida` deste projeto está sendo desenvolvido na branch `extended` https://github.com/rochacbruno/talkshow/tree/extended
