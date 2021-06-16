Lon_min=-75
Lon_Max=-45
Lat_min=20
Lat_max=30
depth_min=0 
depth_max=70 
year_start=2011 
year_end=2012
source=argovis

run_server: viz1 viz2
	@python -m http.server 8080

viz1: temp_plot.py argo_data.csv
	@echo "Running Task-01 visualization script"
	@python temp_plot.py

argo_data.csv: data_load.py
	@echo "Running Task-01 computation script"
	@python data_load.py $(Lon_min) $(Lon_max) $(Lat_min) $(Lat_max) $(depth_min) $(depth_max) $(year_start) $(year_end) $(source) 

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
