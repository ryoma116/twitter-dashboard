# Django個別アプリ初期セットアップコマンド
startapp:
	mkdir -p src/${name}
	django-admin startapp ${name} ./src/${name}

