#! /usr/bin/env python

import graphviz
from yaml import load, CLoader


dot = graphviz.Digraph(comment='Actives')
activos = load(open('activos.yml'), Loader=CLoader)

for activo in activos:
    dot.node(activo['codigo'], activo['nombre'])

for activo in activos:
    if 'dependencias' in activo:
        for dependencia in activo['dependencias']:
            dot.edge(activo['codigo'], dependencia)

dot.render('salida')


