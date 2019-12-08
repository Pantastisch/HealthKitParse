# HealthKitParse

 A simple Apple Health Kit export data parser

## How to export your Apple Health Kit data

1. Create an input folder inside the main folder ('/input')

    ![Picture of folder structure](doc/export/inputFolder.png)

2. Open Health App

    ![Picture of app symbol](doc/export/healthApp.png)

3. Tap on your picture or icon (Top right)

    ![Picture of user profile selection](doc/export/userProfileSelection.png)

4. Scroll down and tap on "Alle Gesundheitsdaten exportieren" (German)

    ![Picture of export button](doc/export/exportButton.png)

5. Tap export and accept exporting

    ![Picture of export query](doc/export/dataExport.png)

6. Wait till the export is finished and the form disapears

    ![Picture of export process](doc/export/wait.png)

7. Store the export somewhere, where you can move it onto your computer
8. Shift the 'Export.zip' file in the folder created in step 1

    ![Picture of finished export](doc/export/finishedExport.png)

9. Now [HealthkitParse.py](HealthkitParse/HealthkitParse.py) is able to work with the exported data
