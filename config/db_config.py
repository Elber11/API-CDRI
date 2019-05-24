params = {
						'dialect' : 'mysql',
						'driver' : 'pymysql',
						'username' : 'root',
						'password' : 'elber',
						'ip' : 'localhost',
						'port' : 3306,
						'database' : 'web_cdri',
						'charset' : 'utf8mb4'
					}

URI = '{dialect}+{d}://{u}:{p}@{ip}:{port}/{db}?charset={charset}&use_unicode=true'.format(dialect=params['dialect'], d=params['driver'], u=params['username'],
													 		   p=params['password'], ip=params['ip'], port=params['port'], db=params['database'],
													 		   charset=params['charset'])