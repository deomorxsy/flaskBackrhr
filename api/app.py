from flask import Flask, jsonify
from flask_cors import CORS

import json

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    # enable CORS
    CORS(app, resources={r'/*': {'origins' : '*'}})

    # import the dict
    with open('../data.json') as f:
        my_dict = json.load(f)
        #f.close()

    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong o/')

    @app.route('/books', methods=['GET'])
    def all_books():
        return jsonify({
            'status': 'success',
            'books': my_dict['books']
            # done using the leftmost key because doing so I
            # do not need to change neither the code key
            # variable nor the JSON file.
        })

    return app



def main():
    runAppRun = create_app()
    runAppRun.run(debug=True)

if __name__ == '__main__':
    main()
