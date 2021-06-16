#all: say_hello generate run_server

#default: report.pdf
#.PHONY: default

#report.pdf: main.tex
#	latexmk -pdf

run_server: viz1 viz2
	@python -m http.server 8080

viz1: temp_plot.py argo_data.csv
	@echo "Running Task-01 visualization script"
	@python temp_plot.py

argo_data.csv: data_load.py
	@echo "Running Task-01 computation script"
	@python data_load.py

viz2: sspeed_plot.py SSpeed_data.csv
	@echo "Running Task-02 visualization script"
	@python sspeed_plot.py

SSpeed_data.csv: sspeed_calculation.py
	@echo "Running Task-02 computation script"
	@python sspeed_calculation.py


install:
	@./install.sh

clean:
	@echo "Cleaning up..."
	rm *.png
	rm *.csv
