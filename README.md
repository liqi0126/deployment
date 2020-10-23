# simplebbs-unnitest
Simplebbs用于单元测试作业的版本，基于flask / python3.8


### migrate

```text
# 初始化数据库，创建一个migrations文件夹，并且在数据库中生成一个alembic_version表
python manager.py database init

# 创建迁移历史
python manager.py database migrate

# 更新数据库
python manager.py database upgrade
```

### run for dev

```bash
cp config_example.yaml config.yaml
vim config.yaml # 编辑配置
python manage.py runserver
```

### run with gunicorn

```bash
gunicorn -w4 -b 0.0.0.0:5000 --log-level=debug --access-logfile error.log manage:app
```

