.PHONY: news.ifeng
news.ifeng:
	python scripts/config/old_config.py raw/news.ifeng/results.json raw/news.ifeng/page.yml
	python scripts/config/add_meta.py raw/news.ifeng/page.yml

	python scripts/batch.py  raw/news.ifeng/ cleaned/news.ifeng/ ./scripts/cleaner/clean_cheerio.js HTML_CLEANER_CONFIG=./scripts/cleaner/configs/news.ifeng.json 
	python scripts/batch.py  cleaned/news.ifeng/ markdown/news.ifeng/ scripts/markdown/html2md.js

.PHONY: news.sina
news.sina:
	python scripts/config/old_config.py raw/news.sina/results.json raw/news.sina/page.yml
	python scripts/config/add_meta.py raw/news.sina/page.yml

.PHONY: thepaper.cn
thepaper.cn:
	python scripts/config/new_config.py raw/thepaper.cn/results.json raw/thepaper.cn/page.yml
