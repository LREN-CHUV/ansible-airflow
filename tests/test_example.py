def test_airflow_version(Command):
  assert Command('airflow', 'version').rc == 0
