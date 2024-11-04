.PHONY: news.ifeng
news.ifeng:
	python scripts/config/old_config.py news.ifeng/results.json news.ifeng/page.yml
	python scripts/config/add_meta.py news.ifeng/page.yml

.PHONY: news.sina
news.sina:
	python scripts/config/old_config.py news.sina/results.json news.sina/page.yml
	python scripts/config/add_meta.py news.sina/page.yml

.PHONY: thepaper.cn
thepaper.cn:
	python scripts/config/new_config.py thepaper.cn/results.json thepaper.cn/page.yml
