.PHONY: ifeng.com
ifeng.com:
	python scripts/config/old_config.py raw/ifeng.com/results.json raw/ifeng.com/page.yml
	python scripts/config/add_meta.py raw/ifeng.com/page.yml

	python scripts/batch.py  raw/ifeng.com/ cleaned/ifeng.com/ ./scripts/cleaner/clean_cheerio.js HTML_CLEANER_CONFIG=./scripts/cleaner/configs/ifeng.com.json 
	python scripts/batch.py  cleaned/ifeng.com/ markdown/ifeng.com/ scripts/markdown/html2md.js

	python scripts/ai/process_dir.py markdown/ifeng.com/ ready/ifeng.com/ scripts/ai/prompt/clean.template

.PHONY: sina.cn
sina.cn:
	python scripts/config/old_config.py raw/sina.cn/results.json raw/sina.cn/page.yml
	python scripts/config/add_meta.py raw/sina.cn/page.yml

.PHONY: thepaper.cn
thepaper.cn:
	python scripts/config/new_config.py raw/thepaper.cn/results.json raw/thepaper.cn/page.yml
