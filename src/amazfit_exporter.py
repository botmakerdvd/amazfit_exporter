#!/usr/bin/python3
import sqlite3 as lite
import sys
import datetime
import os
def db_to_gpx(db,dest):
	con = lite.connect(db)

	with con:
	    
		cur = con.cursor()    
		cur.execute('SELECT track_id, start_time from sport_summary where type=2 or type=1')
		running_sessions = cur.fetchall()
		for running_session in running_sessions:
			track_id=running_session[0]
			tiempo_init=running_session[1]
			cur.execute('SELECT location_data.latitude, location_data.longitude, location_data.altitude, location_data.timestamp from location_data, sport_summary where location_data.track_id=' + str(track_id) + ' and sport_summary.type=2 ')
			datos = cur.fetchall()
			year=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%Y')
			month=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%m')
			day=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%d')
			hour=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%H')
			minute=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%M')
			second=datetime.datetime.fromtimestamp(running_session[1]/1000).strftime('%S')
			try:
				os.remove(dest+'/'+year+month+day+'_'+hour+minute+second+'.gpx')
			except OSError:
				pass
			with open(dest+'/'+year+month+day+'_'+hour+minute+second+'.gpx', 'a') as out:	
				out.write('<?xml version="1.0" encoding="UTF-8"?>' + '\r\n')
				out.write('<gpx version="1.1" creator="Amazfit_export by dvd_ath" xsi:schemaLocation="http://www.topografix.com/GPX/1/1' + '\r\n')
				out.write('                                 http://www.topografix.com/GPX/1/1/gpx.xsd' + '\r\n')
				out.write('                                 http://www.garmin.com/xmlschemas/GpxExtensions/v3' + '\r\n')
				out.write('                                 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd' + '\r\n')
				out.write('		                            http://www.garmin.com/xmlschemas/TrackPointExtension/v1' + '\r\n')
				out.write('                                 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd" xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' + '\r\n')
				out.write(' <metadata>'  + '\r\n')
				out.write('  <link href="https://github.com/botmakerdvd/amazfit_exporter">'+ '\r\n')
				out.write('    <text>Amazfit exporter</text>'+ '\r\n')
				out.write('  </link>'+ '\r\n')
				out.write('  <time>'+year+'-'+month+'-'+day+'T'+hour+':'+minute+':'+second+'.000Z</time>'+ '\r\n')
				out.write(' </metadata>'+ '\r\n')
				out.write(' <trk>'+ '\r\n')
				out.write('  <trkseg>'+ '\r\n')
				for dato in datos:
					latitud=str(dato[0])
					longitud=str(dato[1])
					altitud=str(round(dato[2],1))
					time=((dato[3]+tiempo_init)/1000)
					year=datetime.datetime.fromtimestamp(time).strftime('%Y')
					month=datetime.datetime.fromtimestamp(time).strftime('%m')
					day=datetime.datetime.fromtimestamp(time).strftime('%d')
					hour=datetime.datetime.fromtimestamp(time).strftime('%H')
					minute=datetime.datetime.fromtimestamp(time).strftime('%M')
					second=datetime.datetime.fromtimestamp(time).strftime('%S')			
					cur.execute('SELECT rate from heart_rate where time=' + str(round(time)*1000))
					rate=cur.fetchone()
					out.write('   <trkpt lon="'+longitud+'" lat="'+latitud+'">'+ '\r\n')
					out.write('    <ele>'+altitud+'</ele>'+ '\r\n')
					out.write('    <time>'+year+'-'+month+'-'+day+'T'+hour+':'+minute+':'+second+'.000Z</time>'+ '\r\n')
					if rate is not None:
						out.write('    <extensions>'+ '\r\n')
						out.write('     <gpxtpx:TrackPointExtension>'+ '\r\n')
						out.write(' 	 <gpxtpx:hr>'+str(int(rate[0]))+'</gpxtpx:hr>'+ '\r\n')
						out.write('     </gpxtpx:TrackPointExtension>'+ '\r\n')
						out.write('    </extensions>'+ '\r\n')
					out.write('   </trkpt>'+ '\r\n')
				out.write('  </trkseg>'+ '\r\n')
				out.write(' </trk>'+ '\r\n')
				out.write('</gpx>'+ '\r\n')
				out.close()
