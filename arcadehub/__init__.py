
"""
ArcadeHub package.

En Windows (especialmente con Python 3.13), mysqlclient puede fallar.
Por eso activamos PyMySQL como reemplazo de MySQLdb cuando esté instalado.
"""
try:
    import pymysql  # type: ignore
    pymysql.install_as_MySQLdb()
except Exception:
    pass
