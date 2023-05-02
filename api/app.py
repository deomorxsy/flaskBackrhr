from flask import Flask, jsonify, request
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

    @app.route('/books', methods=['GET', 'POST'])
    def all_books():
        #response object, first item status
        rsp_obj = {'status': 'success'}

        if (request.method == 'POST'):
            post_data = request.get_json()
            # Since dict has no attribute 'append',
            # you just have to search for a list/array
            # -like structure that can be appended. It
            # would be ["books"].
            my_dict['books'].append({
                    'title': post_data.get('title'),
                    'author': post_data.get('author'),
                    'read': post_data.get('read')
            })
            rsp_obj['message'] = 'you just added a book.'
        else:
            # if the request is any other different from post,
            #rsp_obj['books'] = my_dict
            rsp_obj = my_dict
        return jsonify(rsp_obj)
            # done using the leftmost key because doing so I
            # do not need to change neither the code key
            # variable nor the JSON file.

    return app



def main():
    runAppRun = create_app()
    runAppRun.run(debug=True)

if __name__ == '__main__':
    main()
