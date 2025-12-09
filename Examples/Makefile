TARGET = $(patsubst %.py,%.ts,$(wildcard *.py))

all: folders default

folders:
	mkdir -p PY
	mkdir -p TS

default: $(TARGET)

clean:
	rm -fr __pycache__ 

.SUFFIXES : .py .ts

.py.ts:
	python3 ../main.py --pretty $*.py > PY/$*.py
	python3 ../main.py --check $*.py PY/$*.py
# 	python3 ../main.py $*.py > TS/$*.ts
