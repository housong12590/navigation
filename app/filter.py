"""
自定义模版过滤器
"""


def register_template_filter(app):
    @app.template_filter('pwd')
    def pwd(value):
        return '*' * len(value)

    def arr_slice(value, size):
        len(value)
