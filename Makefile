.PHONY: all upload

all: generate

clear:
	rm -rf out nopea_ssg/__pycache__

generate: content static templates
	./nopea_ssg/nopea_ssg.py generate

upload:
	rsync -h --stats -ri out/* server:/var/www/ruzickajakub.eu/html
