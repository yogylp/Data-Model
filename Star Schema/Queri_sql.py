# create Table

Playlist_create = "CREATE TABLE IF NOT EXIST playlist (playlist_id text, Tahun Release Timestamp, ID User text, Level text, Id_lagu int, Id_Artis text)"

User_table_create = "CREATE TABLE IF NOT EXIST User (ID_user int, Nama_depan text, Nama_belakang text, Jenis_kelamin text)"

Lagu_tabel_create = "CREATE TABLE IF NOT EXIST Lagu (Id_lagu int, Judul_lagu text, Id_artis text, Durasi int)"

Artis_table_create = "CREATE TABLE IF NOT EXIST Artis (Id_artis int, Nama text, Lokasi text)"

lama_lagu_table_create = "CREATE TABLE IF NOT EXIST Lama_lagu(Tahun_release int, Tanggal int, Bulan int)"

# Insert Record

Playlist_insert = "INSERT INTO playlist (playllist_id, Tahun_release, ID_User, Level, Id_Lagu, Id_Artis) VALUES (%s, %s, %s, %s, %s, %s)"

User_insert = "INSERT INTO User (ID_user, Nama_depan, Nama_belakang, Jenis_Kelamin) VALUES (%s, %s, %s, %s)"

Lagu_insert = "INSERT INTO Lagu (ID_Lagu, Judul_lagu, Id_artis, Durasi) VALUES (%s, %s, %s, %s)"

Artis_insert = "INSERT INTO Artis(ID_artis, Nama, Lokasi) VALUES (%s, %s, %s)"

Lama_lagu_inser = "INSERT INTO Lama_lagu (Tahun_Release, tanggal, Bulan) VALUES (%s, %s, %s)"

# Find Song

pilih_lagu = "SELECT lagu.Id_Lagu, artis.Id_artis FROM Lagu JOiN Artis ON Lagu.Id_Artis = Artis.Id_artis WHERE Lagu.Judul = %s AND Artis.Nama = %s AND lagu.Durasi = %s"
