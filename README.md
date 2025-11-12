Komandas dalībnieki: Sudmalis, Berbeņovs

Projekta nosaukums: Videospēļu datubāzes sistēma "GameSite"

Lietotnes apraksts: GameSite ir tīmekļa lietotne, kas ļauj lietotājiem:  

Apskatīt videospēļu katalogu ar detalizētu informāciju;  
Meklēt un filtrēt spēles pēc dažādiem kritērijiem;  
Pārvaldīt spēļu saturu (izstrādātājiem un administratoriem).  

Instalēšanas instrukcijas:  

Lejupielādēt projektu kā ZIP failu no GitHub;  
Atzipot mapi lietotājam ērtā lokācijā;  
Pārbaudīt, vai ir instalētas visas nepieciešamās programmas: python, git, uv, kā arī Django.   
Ja tās nav instalētas, nepieciešams tās uzinstalēt, aplūkojot attiecīgo dokumentāciju.  
Atvērt cmd;  
Izmantojot python venv moduli, izveidot jaunu virtuālo vidi: python -m venv <virtuālās_vides_lokācija>  
Palaist komandu cd <virtuālās_vides_lokācija>\Scripts\Activate  
Palaist komandu cd <atzipotās_mapes_lokācija>\game_site-main\game_site_django  
Palaist komandu python manage.py makemigrations  
Palaist komandu python manage.py migrate  
Palaist komandu python manage.py runserver  
Web aplikāciju iespējams lietot, pārlukprogrammā atverot URL 127.0.0.1:8000 vai localhost:8000  

Ekrānšāviņi un īss apraksts:

<img width="2560" height="940" alt="image" src="https://github.com/user-attachments/assets/012dde6f-92b1-45b5-b727-8fdd0f881d4d" />
Galvenais "GameSite" skats ar meklēšanas un filtrēšanas iespējām.
<img width="2560" height="1321" alt="image" src="https://github.com/user-attachments/assets/3dc52235-64d3-4eb1-8aec-dbfbd2517fcb" />
Jaunas spēles pievienošanas skats.
<img width="2560" height="1160" alt="image" src="https://github.com/user-attachments/assets/3fb1dd1f-af64-48cd-ad68-480874a21ec0" />
Izdzēstas spēles skats.
<img width="2560" height="370" alt="image" src="https://github.com/user-attachments/assets/9a9b9943-9667-4472-91e7-206c09de9d70" />
Pieslēgšanās kontam skats.
<img width="2560" height="634" alt="image" src="https://github.com/user-attachments/assets/053c4140-07b5-4556-8e1f-aecc6547f98a" />
Jauna lietotāja reģistrācijas skats.

Izmantoto bibliotēku saraksts:

Projektā nav izmantotas trešo pušu bibliotēkas, taču ir izmantoti vairāki Django moduļi, piemēram, django.contrib.admin, django.urls, django.http u.c. Izmantoti arī standarta moduļi, kā datetime, uuid un os. Priekš grafiskā interfeisa, izmantots Bootstrap, kas ielādēts caur CDN.

Arhitektūras diagramma un apraksts:

<img width="759" height="400" alt="image" src="https://github.com/user-attachments/assets/273303c3-1145-49e6-9e59-b054b406d9fa" />  
Šajā diagrammā attēloti galvenie sistēmas moduļi, kas izpilda atbilstošās prasības. Kopumā sistēmā ir 9 šādi moduļi, kas katrs atbild par savu funkcionalitāti, piemēram, modulis P1.1 "Lietotāja konta reģistrācija" atbild par jauna lietotāja reģistrāciju un pievienošanu datu bāzes Users tabulai, bet modulis P2.3 "Spēles dzēšana" atbild par jau eksistējošas spēles izdzēšanu no datu bāzes.

Idejas nākotnes uzlabojumiem:

Spēļu salīdzināšana - ļaut veikt vairāku spēļu salīdzināšanu side-by-side,
Diagrammu pievienošana - dažādus spēļu datus parādīt diagrammu veidā,
Izmantot reālus datus - izmantojot Steam vai kādu citu API iegūt reālus spēļu datus.
