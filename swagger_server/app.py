#!/usr/bin/env python3

import connexion
#  from encoder import JSONEncoder

app = connexion.App(__name__, specification_dir='./swagger/')
#  app.app.json_encoder = JSONEncoder

app.add_api('swagger.yaml', arguments={'title': 'Composite interface to the Neotoma and PBDB databases'})

application = app.app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8008)
