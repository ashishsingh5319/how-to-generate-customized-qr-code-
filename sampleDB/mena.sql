Drop database if exists menagerie;
CREATE DATABASE menagerie;
USE menagerie;
SOURCE C:\DATA\college\python\sampleDB\menagerie-db\cr_pet_tbl.sql
LOAD DATA LOCAL INFILE 'C:\DATA\college\python\sampleDB\menagerie-db\pet.txt' INTO TABLE pet;
SOURCE C:\DATA\college\python\sampleDB\menagerie-db\ins_puff_rec.sql
SOURCE C:\DATA\college\python\sampleDB\menagerie-db\cr_event_tbl.sql
LOAD DATA LOCAL INFILE 'C:\DATA\college\python\sampleDB\menagerie-db\event.txt' INTO TABLE pet;