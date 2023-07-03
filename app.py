from flask import Flask, render_template,jsonify
from datetime import datetime
from markdown import markdown

app = Flask(__name__)

# 禁用模板缓存
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.cache = None

@app.route('/')
def home():
    #return render_template('')
    return 'home'


@app.route('/test', methods=['GET'])
def test():

    with open("./article/test.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown(text, extensions=['extra'])

        return render_template('base.html',title='标题', main=html)
    return 'Error'

@app.route('/article/<path:title>', methods=['GET'])
def article_single():
    return 'single'

@app.route('/echo', methods=['POST'])
def echo():
    return request.get_text()

@app.route('/ping', methods=['GET'])
def ping():
    return datetime.now().isoformat()


@app.template_filter('cat')
def cat(file_path):
    content = '// include: '+file_path
    with open(file_path, 'r') as file:
        content = file.read()
    return content



if __name__ == '__main__':
    app.run(port=5000)
