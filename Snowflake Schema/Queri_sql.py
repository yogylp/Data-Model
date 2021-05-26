# create Table

Platform_create = "CREATE TABLE IF NOT EXIST plaform (platform_key int)"

Video_start_create = "CREATE TABLE IF NOT EXIST Video_Start (Date_time int, Platform_key int, Video_key int, site_key int, Event text)"

Video_create = "CREATE TABLE IF NOT EXIST Video (Video_key int)"

Site_create = "CREATE TABLE IF NOT EXIST Site (Site_key int)"

Date_create = "CREATE TABLE IF NOT EXIST Date (Date_time int, Tahun int, Bulan int, Tanggal int)"

# Insert Record

Platform_insert = "INSERT INTO Platform (Platform_key) VALUES (%s)"

Video_Start_insert = "INSERT INTO Video (date_time, platform_key, video_key, site_key, Event) VALUES (%s, %s, %s, %s, %s)"

Video_insert = "INSERT INTO Video (video_key) VALUES (%s)"

site_insert = "INSERT INTO site (site_key) VALUES (%s)"

Date_inser = "INSERT INTO Date (date_time, Tahun, Bulan, Tanggal) VALUES (%s, %s, %s, %s)"
