# MODIS_EarthData_Download
A very short script to download MODIS data with a list of EarthData links and a webbrowser.

You first need to go to the earthdata website (https://search.earthdata.nasa.gov/search), register or log in and search for satellite imagery. 
![image](https://user-images.githubusercontent.com/92572325/155529106-3b5f9666-d129-47dc-aa2b-7bcb2cdae2c2.png)
Then, click on the type of images you need.
![image](https://user-images.githubusercontent.com/92572325/155529681-576d05d7-1a33-4f78-80d7-a1aeb7c0bbca.png)
Select Direct Download
![image](https://user-images.githubusercontent.com/92572325/155529766-bb245401-504e-4427-b3ee-7fd930a3e143.png)
and click on direct download
![image](https://user-images.githubusercontent.com/92572325/155529838-4f17e3d2-910b-480e-9c5a-1aef21a9e551.png)
You have to save this list of url as it is in a text file.
Then open and modify the python script MODIS_Earthdata_Download to get access to the txt file containing the URLs and to select an output folder. The downloading will be made through your default webbrowser.
