% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA & ATURAN
penyakit("Insomnia").
penyakit("Sleep Apnea").
penyakit("Narkolepsi").
penyakit("Restless Leg Syndrome").

gejala(sulit_tidur, "Insomnia").
gejala(sering_terbangun, "Insomnia").
gejala(lelah_di_pagi, "Insomnia").

gejala(ngorok, "Sleep Apnea").
gejala(sulit_bernapas_saat_tidur, "Sleep Apnea").
gejala(mengantuk_berlebihan, "Sleep Apnea").

gejala(tidur_tiba_tiba, "Narkolepsi").
gejala(lemas_saat_emosi, "Narkolepsi").
gejala(hilang_kontrol_otot, "Narkolepsi").

gejala(gatal_di_kaki, "Restless Leg Syndrome").
gejala(keinginan_gerak_kaki, "Restless Leg Syndrome").
gejala(sulit_tidur_karena_kaki, "Restless Leg Syndrome").

pertanyaan(sulit_tidur, Y) :- Y = "Apakah Anda kesulitan untuk tidur di malam hari?".
pertanyaan(sering_terbangun, Y) :- Y = "Apakah Anda sering terbangun di malam hari?".
pertanyaan(lelah_di_pagi, Y) :- Y = "Apakah Anda merasa lelah saat bangun pagi?".

pertanyaan(ngorok, Y) :- Y = "Apakah Anda ngorok saat tidur?".
pertanyaan(sulit_bernapas_saat_tidur, Y) :- Y = "Apakah Anda kesulitan bernapas saat tidur?".
pertanyaan(mengantuk_berlebihan, Y) :- Y = "Apakah Anda sering mengantuk di siang hari secara berlebihan?".

pertanyaan(tidur_tiba_tiba, Y) :- Y = "Apakah Anda pernah tiba-tiba tertidur saat beraktivitas?".
pertanyaan(lemas_saat_emosi, Y) :- Y = "Apakah Anda merasa lemas saat mengalami emosi kuat?".
pertanyaan(hilang_kontrol_otot, Y) :- Y = "Apakah Anda pernah kehilangan kontrol otot secara tiba-tiba?".

pertanyaan(gatal_di_kaki, Y) :- Y = "Apakah Anda merasa gatal atau tidak nyaman di kaki saat istirahat?".
pertanyaan(keinginan_gerak_kaki, Y) :- Y = "Apakah Anda merasa ingin terus menggerakkan kaki saat malam hari?".
pertanyaan(sulit_tidur_karena_kaki, Y) :- Y = "Apakah kesulitan tidur Anda disebabkan oleh sensasi di kaki?".
