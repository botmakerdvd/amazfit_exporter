# amazfit_exporter
This python script helps you to export your huami Amazfit activities to other platforms like Strava,Runtastic...

At current version the script can be used in both CLI or GUI modes:

For CLI:
- python3 amazfit_exporter_cli.py sport_data.db /path/to/destination/folder

For GUI:
- python3 amazfit_exporter_gui.py

The sport_data.db file has to be get from the Amazfit by ADB, there are two methods for this
- connect amazfit to pc
- adb backup -f /export_data.ab -noapk com.huami.watch.sport
- java -jar abe.jar unpack export_data.ab export_data.tar (abe is android backup extractor which is included inside tools folder)
- extract the tar file using winrar
- navigate to export_data\apps\com.huami.watch.sport\db folder and copy sport_data.db


or if you have a rooted rom , just execute command

adb pull /data/data/com.huami.watch.sport/databases/sport_data.db

#CHANGELOG
-V1.0 generates .gpx file for each activity
-V1.1 Added GUI