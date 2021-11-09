#!/usr/bin/python3
import os
from flask import Blueprint
from flask_autoindex import AutoIndexBlueprint
from flask_login import login_required

autoindex = Blueprint('autoindex', __name__)
file_index = AutoIndexBlueprint(autoindex, browse_root=os.path.curdir+'/flask_app/files', add_url_rules=False)


@autoindex.route('/')
@autoindex.route('/<path:path>')
@login_required
def files(path='.'):
    return file_index.render_autoindex(path, template='autoindex.html', endpoint='.files')
