from flask import Flask, render_template,jsonify
from datetime import datetime
from markdown import markdown

from .py import config
from .py import fl
from pathlib import Path
import os


app = Flask(__name__)

# 禁用模板缓存
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.cache = None

@app.route('/')
def home():
    return fl.render(main='<h1>Index of /</h1>')


@app.route('/archive')
def archive():
    return fl.render(main='<h1>Index of /archive</h1>')



@app.route('/test', methods=['GET'])
def test():

    with open("./archive/test.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown(text, extensions=['extra'])

        return render_template(
                'post.html',
                title='标题',
                main=html,
                env='dev',
                render_time=datetime.now().isoformat(),
                **vars(config),
                #css=':root{--bg_h: 0;--bg_s: 50%;--bg_l: 50%;}'

        )
    return 'Error'

@app.route('/article/<path:title>', methods=['GET'])
def article_single():
    return 'single'

# 浏览项目文件
@app.route('/browse/', defaults={'path': '.'})
@app.route('/browse/<path:path>')
def browse_files(path):
    root='/browse'
    path = path or '.'
    if not os.path.exists(path):
        return f'Path does not exist. "{path}"'

    # 访问文件
    data = get_file_info(path)
    if os.path.isfile(path):
        return render_template('file.html', file=data, root=root)

    # 访问目录
    content = []
    with os.scandir(path) as entries:
        for entry in entries:
            item = get_file_info(entry.path)

            content.append(item)

    data['content'] = content

    return render_template('file.html', file=data, root=root)

# 测试用路由
@app.route('/echo', methods=['POST'])
def echo():
    return request.get_text()

@app.route('/ping', methods=['GET'])
def ping():
    return datetime.now().isoformat()




# 在模板中读取文件
@app.template_filter('cat')
def cat(file_path):
    content = '// include: '+file_path
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def get_file_info(path):
    path = Path(path)
    cwd = os.getcwd()
    parent = str(path.parent.resolve())
    parent = parent[len(cwd):] #or '/'


    file_info = {
        'name': path.name,
        'parent': parent,
        'type': path.is_dir() and 'dir' or 'file',
        'size': path.stat().st_size,
        'mtime': path.stat().st_mtime
    }

    return file_info


if __name__ == '__main__':
    app.run(port=5000)
