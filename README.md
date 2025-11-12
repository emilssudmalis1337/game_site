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

Atver google un ievadit: http://localhost:8000/, 
augšējā labajā stūrī būs poga “log-in”. Nospižit reģistrācijas pogu un esiet gamer vai developer bet ja uzrakstits primitivs parole tad account netiek izveidots.
Ja izveidojat kontu kā spēlētājs, varat meklēt spēli, atlasīt to pēc kategorijas un saglabāt sarakstā, un, ja izveidojat kontu kā izstrādātājs, varat pievienot spēli (augšējā kreisajā stūrī parādīsies poga) vai mainīt vecu spēli vai izdzēst to.

Izmantoto bibliotēku saraksts:



Arhitektūras diagramma un apraksts:



Idejas nākotnes uzlabojumiem:

Spēļu salīdzināšana - ļaut veikt vairāku spēļu salīdzināšanu side-by-side,
Diagrammu pievienošana - dažādus spēļu datus parādīt diagrammu veidā,
Izmantot reālus datus - izmantojot Steam vai kādu citu API iegūt reālus spēļu datus.
