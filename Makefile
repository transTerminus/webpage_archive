.PHONY: news.ifeng
news.ifeng:
	python scripts/config/old_config.py raw/ifeng.com/results.json raw/ifeng.com/page.yml
	python scripts/config/add_meta.py raw/ifeng.com/page.yml

	python scripts/batch.py  raw/ifeng.com cleaned/news.ifeng/ ./scripts/cleaner/clean_cheerio.js HTML_CLEANER_CONFIG=./scripts/cleaner/configs/news.ifeng.json 
	python scripts/batch.py  cleaned/ifeng.com/ markdown/news.ifeng/ scripts/markdown/html2md.js

	python scripts/ai/process_dir.py markdown/news.ifeng/ ready/news.ifeng/ scripts/ai/prompt/clean.template

.PHONY: news.sina
news.sina:
	python scripts/config/old_config.py raw/sina.cn/results.json raw/sina.cn/page.yml
	python scripts/config/add_meta.py raw/sina.cn/page.yml

	python scripts/batch.py  raw/sina.cn cleaned/sina.cn/ ./scripts/cleaner/clean_cheerio.js HTML_CLEANER_CONFIG=./scripts/cleaner/configs/sina.cn.json 
	python scripts/batch.py  cleaned/sina.cn/ markdown/sina.cn/ scripts/markdown/html2md.js

	python scripts/ai/process_dir.py markdown/sina.cn/ ready/sina.cn/ scripts/ai/prompt/clean.template

.PHONY: thepaper.cn
thepaper.cn:
	python scripts/config/new_config.py raw/thepaper.cn/results.json raw/thepaper.cn/page.yml
