1. 执行 python manage.py migrate 报错  
```python
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    execute_from_command_line(sys.argv)
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\core\management\__init__.py", line 363, in execute_from_command_l
ine
    utility.execute()
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\core\management\__init__.py", line 337, in execute
    django.setup()
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\__init__.py", line 27, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\apps\registry.py", line 85, in populate
    app_config = AppConfig.create(entry)
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\apps\config.py", line 94, in create
    module = import_module(entry)
  File "C:\Python3.7\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\contrib\admin\__init__.py", line 4, in <module>
    from django.contrib.admin.filters import (
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\contrib\admin\filters.py", line 10, in <module>
    from django.contrib.admin.options import IncorrectLookupParameters
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\contrib\admin\options.py", line 12, in <module>
    from django.contrib.admin import helpers, widgets
  File "C:\Users\CZY\PycharmProjects\learning_log\ll_env\lib\site-packages\django\contrib\admin\widgets.py", line 151
    '%s=%s' % (k, v) for k, v in params.items(),
    ^
SyntaxError: Generator expression must be parenthesized

```

提示生成器语法错误，根据提示，找到 '%s=%s' % (k, v) for k, v in params.items(),  这一行，
将最后“,”去掉就好，再重新执行








