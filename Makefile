.PHONY: news.ifeng
news.ifeng:
	python scripts/config/old_config.py raw/news.ifeng/results.json raw/news.ifeng/page.yml
	python scripts/config/add_meta.py raw/news.ifeng/page.yml

.PHONY: news.sina
news.sina:
	python scripts/config/old_config.py raw/news.sina/results.json raw/news.sina/page.yml
	python scripts/config/add_meta.py raw/news.sina/page.yml

.PHONY: thepaper.cn
thepaper.cn:
	python scripts/config/new_config.py raw/thepaper.cn/results.json raw/thepaper.cn/page.yml
